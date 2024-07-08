from crypto import encrypt, decrypt
from cryptography.hazmat.primitives.kdf.pbkdf2 import InvalidKey

def encrypt_password(words, passphrase):
    concatenated_words = ' '.join(words.split())
    return encrypt(concatenated_words, passphrase)

def decrypt_password(encrypted_password, passphrase):
    try:
        decrypted_string = decrypt(encrypted_password, passphrase)
        # Split words and ensure the passphrase is not included in the output
        words = decrypted_string.split()
        # Filter out the passphrase from the list of words
        words = [word for word in words if word != passphrase]
        numbered_words = '\n'.join([f"{i+1}. {word}" for i, word in enumerate(words)])
        return numbered_words
    except InvalidKey:
        return "Error: Incorrect passphrase"