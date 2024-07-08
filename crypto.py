from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os
import base64

def derive_key(passphrase, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # AES-256 requires a 32-byte key
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(passphrase.encode())
    return key

def pad(data):
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()
    return padded_data

def unpad(data):
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    unpadded_data = unpadder.update(data) + unpadder.finalize()
    return unpadded_data

def encrypt(password, passphrase):
    salt = os.urandom(16)  # 128-bit salt
    key = derive_key(passphrase, salt)
    iv = os.urandom(16)  # 128-bit IV
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padded_password = pad(password.encode())
    encrypted_password = encryptor.update(padded_password) + encryptor.finalize()
    return base64.b64encode(salt + iv + encrypted_password).decode()

def decrypt(encrypted, passphrase):
    encrypted = base64.b64decode(encrypted.encode())
    salt = encrypted[:16]
    iv = encrypted[16:32]
    ciphertext = encrypted[32:]
    key = derive_key(passphrase, salt)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_padded_password = decryptor.update(ciphertext) + decryptor.finalize()
    decrypted_password = unpad(decrypted_padded_password)
    return decrypted_password.decode()