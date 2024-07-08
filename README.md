### README.md

```markdown
# MASARI Encryption/Decryption Application

This project provides an interactive application for encrypting and decrypting text using a passphrase. The application includes both a web interface and a command-line interface (CLI).

## Project Structure

```plaintext
MASARI/
├── Dockerfile
├── requirements.txt
├── crypto.py
├── main.py
├── password.py
├── decrypt.py
└── app.py
```

## Getting Started

### Prerequisites

- Docker must be installed on your system.

### Building the Docker Image

1. Clone the repository and navigate to the project directory:

   ```bash
   git clone <repository_url>
   cd MASARI
   ```

2. Build the Docker image:

   ```bash
   docker build -t my_python_app .
   ```

### Running the Application

#### Web Interface

1. Run the Docker container, mapping a port from your host to the container (e.g., 5001):

   ```bash
   docker run -it --rm -p 5001:5000 my_python_app
   ```

2. Open your browser and navigate to `http://localhost:5001`.

3. Use the web interface to encrypt or decrypt text by entering the required information and clicking the corresponding button. The result will be displayed on the same page.

#### Command-Line Interface (CLI)

1. Run the Docker container and specify the `main.py` script to use the CLI:

   ```bash
   docker run -it --rm my_python_app python main.py
   ```

2. Follow the prompts to encrypt or decrypt text:
   - Select (E)ncrypt or (D)ecrypt.
   - Enter the text or encrypted value.
   - Enter the passphrase.
   - The result will be displayed in the terminal.

## How It Works

### Encryption and Decryption Logic

1. **Key Derivation Function (KDF):**
   - The KDF uses PBKDF2 with SHA-256 to derive a 32-byte key from the passphrase and a randomly generated salt.
   - This ensures that even if the same passphrase is used, the derived key will be different for each encryption due to the unique salt.

2. **Padding:**
   - The text to be encrypted is padded to ensure it is a multiple of the AES block size (16 bytes).

3. **Encryption:**
   - The text is encrypted using AES in CBC mode with the derived key and a randomly generated initialization vector (IV).
   - The encrypted text, salt, and IV are concatenated and base64 encoded for storage or transmission.

4. **Decryption:**
   - The base64 encoded string is decoded to extract the salt, IV, and ciphertext.
   - The same passphrase and extracted salt are used to derive the AES key.
   - The ciphertext is decrypted using AES in CBC mode with the derived key and IV.
   - The decrypted text is then unpadded to retrieve the original text.
```
# Encrypt/Decrypt Application

This application allows users to encrypt and decrypt text using a passphrase. The text can consist of multiple words, and the number of words can be selected by the user. The encrypted text can be easily copied for storage or transfer.

## Features

- Encrypt text using a user-defined passphrase.
- Decrypt text using the same passphrase.
- Select either 12 or 24 words to encrypt.
- User-friendly web interface.
- Terminal support for encryption and decryption.

## Prerequisites

- Docker installed on your machine.
- Python 3.10 installed.
- Required Python packages listed in `requirements.txt`.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/your-username/encrypt-decrypt-app.git
    cd encrypt-decrypt-app
    ```

2. Build the Docker image:

    ```sh
    docker build -t my_python_app .
    ```

## Running the Application

### Web Interface

1. Run the Docker container:

    ```sh
    docker run -it --rm -p 5000:5000 my_python_app
    ```

2. Open your web browser and go to `http://localhost:5000`.

3. Follow the instructions on the page:
    - Select the number of words (12 or 24).
    - Enter the words in the provided fields.
    - Enter the passphrase.
    - Click "Encrypt" to encrypt the text.
    - The encrypted text will be displayed in the "Encrypted Result" box. Use the "Copy" button to copy it to your clipboard.
    - To decrypt, enter the encrypted text and the passphrase in the respective fields and click "Decrypt".
    - The decrypted result will be displayed in the "Decrypted Result" box.

### Terminal Interface

1. Run the Docker container with a bash terminal:

    ```sh
    docker run -it --rm my_python_app /bin/bash
    ```

2. Use the following Python script for encryption and decryption:

    ```python
    # encrypt_decrypt.py
    from password import encrypt_password, decrypt_password

    def main():
        choice = input("Do you want to (e)ncrypt or (d)ecrypt? ")
        if choice.lower() == 'e':
            words = input("Enter the words (space-separated): ")
            passphrase = input("Enter the passphrase: ")
            encrypted = encrypt_password(words, passphrase)
            print(f"Encrypted: {encrypted}")
        elif choice.lower() == 'd':
            encrypted_value = input("Enter the encrypted text: ")
            passphrase = input("Enter the passphrase: ")
            decrypted = decrypt_password(encrypted_value, passphrase)
            print(f"Decrypted: {decrypted}")
        else:
            print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")

    if __name__ == "__main__":
        main()
    ```

3. Run the script:

    ```sh
    python encrypt_decrypt.py
    ```

4. Follow the prompts in the terminal to encrypt or decrypt text.

## Project Structure

- `app.py`: Flask application code.
- `password.py`: Contains the `encrypt_password` and `decrypt_password` functions.
- `crypto.py`: Encryption and decryption logic using AES.
- `requirements.txt`: List of Python dependencies.
- `templates/index.html`: HTML file for the web interface.
- `static/lock.jpg`: Image used in the web interface.
- `Dockerfile`: Docker configuration file.

## Logic Explanation

### Encryption Process

1. **User Input**:
    - The user selects the number of words (12 or 24) and enters them into the provided fields.
    - The user provides a passphrase for encryption.

2. **Concatenation**:
    - The entered words are concatenated into a single string.

3. **Salt Generation**:
    - A unique salt is generated for each encryption operation to ensure that the same input does not produce the same output, enhancing security.

4. **Key Derivation**:
    - The passphrase and salt are combined and processed using the PBKDF2 (Password-Based Key Derivation Function 2) with SHA-256 to derive a secure key for AES encryption.
    - This process involves multiple iterations to increase the complexity and security of the derived key.

5. **AES Encryption**:
    - The derived key is used to encrypt the concatenated string using AES (Advanced Encryption Standard) in GCM (Galois/Counter Mode).
    - AES-GCM provides both confidentiality and integrity, ensuring that the encrypted text cannot be tampered with.

6. **Output**:
    - The encrypted result, along with the salt and other necessary metadata, is encoded and displayed to the user.

### Decryption Process

1. **User Input**:
    - The user enters the encrypted text and the passphrase used for encryption.

2. **Extract Metadata**:
    - The salt and other necessary metadata are extracted from the encrypted text.

3. **Key Derivation**:
    - The passphrase and extracted salt are combined and processed using PBKDF2 with SHA-256 to derive the same secure key used during encryption.

4. **AES Decryption**:
    - The derived key is used to decrypt the encrypted text using AES-GCM.

5. **Split Words**:
    - The decrypted string is split back into individual words, and each word is displayed in the correct order.

### Security Considerations

- **Salt**:
    - A unique salt is generated for each encryption operation to ensure that the same input does not produce the same output.
    - This adds an additional layer of security by making it harder for attackers to use precomputed hashes (rainbow tables) to crack the encryption.

- **Key Derivation**:
    - PBKDF2 with SHA-256 is used to derive a secure key from the passphrase and salt.
    - The use of multiple iterations increases the complexity and security of the derived key.

- **AES-GCM**:
    - AES in Galois/Counter Mode (GCM) is used for encryption, providing both confidentiality and integrity.
    - GCM ensures that any modification to the encrypted text can be detected, preventing tampering.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.