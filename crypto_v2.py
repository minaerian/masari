import os
import base64
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def derive_key(passphrase: str, salt: bytes) -> bytes:
    """Derive a secret key from the passphrase using scrypt."""
    kdf = Scrypt(
        salt=salt,
        length=32,
        n=2**14,
        r=8,
        p=1,
    )
    return kdf.derive(passphrase.encode())


def encrypt(text: str, passphrase: str) -> str:
    """Encrypt text using AES-GCM with a key derived from the passphrase."""
    salt = os.urandom(16)
    key = derive_key(passphrase, salt)
    iv = os.urandom(12)
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(iv, text.encode(), None)
    return base64.b64encode(salt + iv + ciphertext).decode()


def decrypt(token: str, passphrase: str) -> str:
    """Decrypt text previously encrypted with :func:`encrypt`."""
    data = base64.b64decode(token.encode())
    salt = data[:16]
    iv = data[16:28]
    ciphertext = data[28:]
    key = derive_key(passphrase, salt)
    aesgcm = AESGCM(key)
    plaintext = aesgcm.decrypt(iv, ciphertext, None)
    return plaintext.decode()


def decrypt_password(encrypted_password: str, passphrase: str) -> str:
    """Decrypt and nicely format the recovered words."""
    plaintext = decrypt(encrypted_password, passphrase)
    words = plaintext.split()
    passphrase_words = passphrase.split()
    if words[-len(passphrase_words):] == passphrase_words:
        words = words[:-len(passphrase_words)]
    return "\n".join(f"{i+1}. {word}" for i, word in enumerate(words))
