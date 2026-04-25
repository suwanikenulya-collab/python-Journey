# A password encoding/decoding program

import base64

def encrypt_pass(password):
    encoded_bytes = base64.b64encode(password.encode())
    print(encoded_bytes.decode())   # show as readable string


user_password = input("Enter your password: ")
encrypt_pass(user_password)

print("Just in case you need to decode your passwords, use the program below.")

def decode_password(password):
    decoded_bytes = base64.b64decode(password.encode())   # FIXED here
    decoded_data = decoded_bytes.decode()
    print(f"Decoded password: {decoded_data}")


encode_string = input("Enter your password to be decoded: ")
decode_password(encode_string)