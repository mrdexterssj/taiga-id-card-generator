from base64 import b64encode, b64decode
from pathlib import Path
import traceback
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey
from main import PUBLIC_KEY, PRIVATE_KEY, CARD_BACK, CARD_FRONT
import re
from qrcode import make
from qrcode.image import svg

class Card():
    def __init__(self, data: dict):
        self.data = data

    def gen_svg_card(self, ofld: Path, front: bool=True, back: bool=True):
        

        if front:
            with open(f"{str(ofld)}/card_front.svg", "wt") as output_file:
                card_front_formatted = CARD_FRONT.format(
                    pfp=self.data["pfp"], 
                    pfp_small=self.data["pfp_small"], 
                    b64_qrcode=self.data["qrcode"], 
                    barcode=self.data["barcode"], 
                    mc_username=self.data["mc_username"], 
                    id_number=self.data["id_number"],
                    alias=self.data["alias"],
                    city=self.data["city"],
                    occupation=self.data["occupation"],
                    gender=self.data["gender"],
                    valid_date=self.data["valid_date"],
                    issue_date=self.data["issue_date"]
                )
                try:
                    print(f"Saving to: {str(ofld)}/card_front.svg")
                    output_file.write(card_front_formatted)
                except Exception as e:
                    traceback.print_exc()
                    print(str(e))

        if back:
            with open(f"{str(ofld)}/card_back.svg", "wt") as output_file:
                card_back_formatted = CARD_BACK.format(
                    username=self.data["contact_username"], 
                    platform=self.data["contact_platform"], 
                    id_image_source=self.data["id_img_source"], 
                    issue_server=self.data["issue_server"], 
                    encryption_code_line_1='self.data["mc_username"]', 
                    encryption_code_line_2='self.data["id_number"]',
                    encryption_code_line_3='self.data["alias"]'
                )
                try:
                    print(f"Saving to: {str(ofld)}/card_back.svg")
                    output_file.write(card_back_formatted)
                except Exception as e:
                    traceback.print_exc()
                    print(str(e))

    def sign_card(self) -> str:

        num_id = ""
        for i in re.findall(r'\d+', self.data["id_number"]):
            num_id += i

        unsigned_str = f"{self.data["mc_username"]};{num_id};vdt:{self.data["valid_date"]}"

        #Sign str
        signed_bytes = PRIVATE_KEY.sign(unsigned_str.encode("utf-8"))
        signed_str = b64encode(signed_bytes).decode("utf-8")

        #Construct verification token
        verification_token = unsigned_str + "." + signed_str

        return verification_token

    def gen_qr(self, verification_token):
        qr_code = make(verification_token, image_factory=svg.SvgPathFillImage)
        qr_code.save(Path("~/Downloads/qr_code.svg").expanduser())
        #PENDING: convert directly to b64 to embed

# Tests in /tests