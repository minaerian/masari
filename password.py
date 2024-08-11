from cryptography.hazmat.primitives.kdf.pbkdf2 import InvalidKey
from cryptography.hazmat.primitives.padding import InvalidPadding

def decrypt_password(encrypted_password, passphrase):
    try:
        # Decrypt the data using the provided passphrase
        decrypted_string = decrypt(encrypted_password, passphrase)
        words = decrypted_string.split()
        
        # Filter out the passphrase words only if they appear at the end of the decrypted string
        passphrase_words = passphrase.split()
        passphrase_length = len(passphrase_words)

        # Check if the end of the decrypted words matches the passphrase
        if words[-passphrase_length:] == passphrase_words:
            words = words[:-passphrase_length]  # Remove the passphrase words

        # Ensure that only the actual words are shown, excluding the passphrase
        numbered_words = '\n'.join([f"{i+1}. {word}" for i, word in enumerate(words)])
        return numbered_words
    except InvalidKey:
        return "Error: Incorrect passphrase"
    except InvalidPadding:
        return "Error: Decryption failed due to invalid padding (likely an incorrect passphrase)"
    except Exception as e:
        return f"Error: {str(e)}"
