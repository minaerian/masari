# password.py
from crypto import encrypt, decrypt
from cryptography.fernet import InvalidToken

def encrypt_password(password, passphrase):
    return encrypt(password, passphrase)

def decrypt_password(encrypted_password, passphrase):
    try:
        return decrypt(encrypted_password, passphrase)
    except InvalidToken:
        return "Error: Incorrect passphrase"