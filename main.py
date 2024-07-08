# main.py
from password import encrypt_password, decrypt_password

def main():
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()
    
    if choice == 'E':
        password = input("Enter the text to encrypt: ")
        passphrase = input("Enter the passphrase: ")
        encrypted = encrypt_password(password, passphrase)
        print(f"Encrypted: {encrypted}")
    elif choice == 'D':
        encrypted_value = input("Enter the encrypted text: ")
        passphrase = input("Enter the passphrase: ")
        decrypted = decrypt_password(encrypted_value, passphrase)
        print(f"Decrypted: {decrypted}")
    else:
        print("Invalid choice. Please enter 'E' for encrypt or 'D' for decrypt.")

if __name__ == "__main__":
    main()