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

### Adding the README to Your Project

1. Create a file named `README.md` in the root of your project directory.
2. Copy and paste the above content into the `README.md` file.
3. Save the file.

Now your project includes a comprehensive README file that explains how to use the application both through the web interface and the command-line interface, as well as the underlying logic of the encryption and decryption process.