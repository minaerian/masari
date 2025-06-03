from crypto_v2 import encrypt, decrypt_password


def main():
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()
    if choice == 'E':
        text = input("Enter the text to encrypt: ")
        passphrase = input("Enter the passphrase: ")
        encrypted = encrypt(text, passphrase)
        print(f"Encrypted:\n{encrypted}")
    elif choice == 'D':
        encrypted_text = input("Enter the encrypted text: ")
        passphrase = input("Enter the passphrase: ")
        try:
            decrypted = decrypt_password(encrypted_text, passphrase)
            print(f"Decrypted:\n{decrypted}")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Invalid choice. Please enter 'E' or 'D'.")


if __name__ == "__main__":
    main()
