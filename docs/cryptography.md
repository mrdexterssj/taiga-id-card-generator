# How does the server check ID authenticity?

The planned flow uses asymmetric cryptography to sign user data and provide a means of verifying integrity, preventing counterfeits and tampered documents from being used

## Flow

0. During deployment, the server generates a public and private pair of keys. The private key stays hidden in the server, while the public key can be accessed by anyone for verification purposes.
1. During generation, the server takes username, ID Number and expiration date, and combines them into a plain text blob
2. Then the server encrypts that blob using its private key
3. The server then combines together the blob and encrypted code into a single string, and generates a QR code from it
4. The QR code is embedded in the ID card
5. To verify authenticity, the server or external platform decrypts the encrypted code using the server's public key and compares it to the blob. If they match, the card is deemed as authentic. If they don't match, the card is rejected as a counterfeit or a tampered card