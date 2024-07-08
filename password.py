# password.py
from crypto import encrypt, decrypt

def encrypt_password(password, passphrase):
    return encrypt(password, passphrase)

def decrypt_password(encrypted_password, passphrase):
    return decrypt(encrypted_password, passphrase)