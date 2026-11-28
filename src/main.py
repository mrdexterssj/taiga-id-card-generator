# This is the app's entrypoint
# It sets up env vars and loads config, then launches the GUI

from PySide6.QtWidgets import QApplication
from setup_ui import MainWindow
import sys
import argparse
from base64 import b64decode, b64encode
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey, Ed25519PrivateKey
from dotenv import load_dotenv
from pathlib import Path
import traceback
from os import getenv
from ui.card_bin import CARD_BACK_B64, CARD_FRONT_B64

#Setup argument parser
argparser = argparse.ArgumentParser()
argparser.add_argument("--private-key", type=str, help="Input the private key to be used for card signing")
argparser.add_argument("--public-key", type=str, help="Input the public key to be used for card validation")
argparser.add_argument("--env", type=str, help="Path where the .env file is located")
args = argparser.parse_args()

if args.env == None:
    env_path = "../.env"
else:
    try:
        env_path = str(Path(args.env).expanduser().resolve())
    except Exception as e:
        traceback.print_exc()
        print(f"Bad argument: --env: {args.env}")
        print(str(e))

#=====Detect private (and public) key=====

#Detect from args
b64_private_key = args.private_key
b64_public_key = args.public_key

#Detect from .env
if b64_private_key == None or b64_public_key == None:
    try:
        load_dotenv(env_path)
        print(f"env path:{env_path}")
        b64_public_key = getenv("TAIGA_PUBLIC_KEY")
        b64_private_key = getenv("TAIGA_PRIVATE_KEY")
    except:
        print("No .env file found or couldn't load.")

#Detect from env vars
if b64_private_key == None or b64_public_key == None:
    b64_public_key = getenv("TAIGA_PUBLIC_KEY")
    b64_private_key = getenv("TAIGA_PRIVATE_KEY")

#Final check
if b64_public_key == None or b64_public_key == None:
    raise TypeError("Some of your keys weren't properly set or retrieved, please make sure you specify both through the same method")

#=========================================

#Decrypt and reconstruct Private and Public keys
PRIVATE_KEY = Ed25519PrivateKey.from_private_bytes(b64decode(b64_private_key))
PUBLIC_KEY  = Ed25519PublicKey.from_public_bytes(b64decode(b64_public_key))

#Decode and load card .svg files
try:
    CARD_FRONT = b64decode(CARD_FRONT_B64).decode('utf-8')
    CARD_BACK = b64decode(CARD_BACK_B64).decode('utf-8')
except:
    traceback.print_exc()
    raise RuntimeError("Error decoding card .svg files")

#Launch GUI
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(app)
    window.show()

    sys.exit(app.exec())