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

- Python 3.10 or later
- `pip` for installing dependencies

### Installing Dependencies

1. Clone the repository and navigate to the project directory:

   ```bash
   git clone <repository_url>
   cd MASARI
   ```

2. Install required packages:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

#### Web Interface

1. Start the Flask server:

   ```bash
   python app_v2.py
   ```

2. Open your browser and navigate to `http://localhost:5000` to encrypt or decrypt text.

#### Command-Line Interface (CLI)

Run the CLI directly:

```bash
python cli_v2.py
```

Follow the prompts to encrypt or decrypt text.

### Packaging with PyInstaller

To create a stand‑alone executable (replace `:` with `;` on Windows):

```bash
pyinstaller --onefile --add-data "templates:templates" --add-data "static:static" app_v2.py
```

The executable will be placed in the `dist` directory. Run it to launch the web interface without needing Python installed.

## How It Works

### Encryption and Decryption Logic

1. **Key Derivation Function (KDF):**
   - `scrypt` derives a 32‑byte key from the passphrase and a randomly generated salt.
   - A unique salt ensures a different key for each encryption.

2. **Encryption:**
   - The text is encrypted using AES‑GCM with the derived key and a 12‑byte IV.
   - AES‑GCM provides both confidentiality and integrity; no padding is required.
   - The encrypted text, salt, and IV are concatenated and base64 encoded for storage or transmission.

3. **Decryption:**
   - The base64 string is decoded to obtain the salt, IV, and ciphertext.
   - The same passphrase and salt derive the key again.
   - The ciphertext is decrypted using AES‑GCM, verifying its integrity automatically.
