from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC, InvalidKey
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import base64

def derive_key(passphrase, salt):
    """Derives a cryptographic key from the passphrase using PBKDF2 HMAC with SHA-256."""
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
    """Applies PKCS7 padding to the data."""
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()
    return padded_data

def unpad(data):
    """Removes PKCS7 padding from the data."""
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    unpadded_data = unpadder.update(data) + unpadder.finalize()
    return unpadded_data

def encrypt(password, passphrase):
    """Encrypts the password using AES-256 in CBC mode with a random salt and IV."""
    salt = os.urandom(16)  # 128-bit salt
    key = derive_key(passphrase, salt)
    iv = os.urandom(16)  # 128-bit IV
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padded_password = pad(password.encode())
    encrypted_password = encryptor.update(padded_password) + encryptor.finalize()
    return base64.b64encode(salt + iv + encrypted_password).decode()

def decrypt(encrypted, passphrase):
    """Decrypts the encrypted password using AES-256 in CBC mode with the provided passphrase."""
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

def decrypt_password(encrypted_password, passphrase):
    try:
        # Decrypt the data using the provided passphrase
        decrypted_string = decrypt(encrypted_password, passphrase)
        words = decrypted_string.split()
        
        # Filter out the passphrase words only if they appear at the end of the decrypted string
        passphrase_words = passphrase.split()
        passphrase_length = len(passphrase_words)

        if words[-passphrase_length:] == passphrase_words:
            words = words[:-passphrase_length]

        # Ensure that only the actual words are shown, excluding the passphrase
        numbered_words = '\n'.join([f"{i+1}. {word}" for i, word in enumerate(words)])
        return numbered_words
    except InvalidKey:
        return "Error: Incorrect passphrase"
    except ValueError as e:
        # This handles padding errors
        return "Error: Decryption failed due to incorrect padding or data corruption"
    except Exception as e:
        return f"Error: {str(e)}"
