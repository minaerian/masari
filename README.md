# Encrypt/Decrypt Application

This project is a simple web-based application that allows users to encrypt and decrypt text data using a passphrase. The application uses AES-256 encryption in CBC mode and employs the PBKDF2 key derivation function for generating cryptographic keys.

## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [APIs](#apis)
- [Customization](#customization)
- [Known Issues](#known-issues)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Encrypt Text:** Users can input up to 12 or 24 words along with a passphrase to generate an encrypted text.
- **Decrypt Text:** Users can input the encrypted text and the passphrase to retrieve the original text.
- **Validation:** Input words are validated against a predefined list of words (BIP39 word list).
- **Responsive UI:** The application is built with a simple, responsive UI using Bootstrap.

## Technologies

- **Python 3.x**
- **Flask** - for creating the web server and handling HTTP requests.
- **Cryptography** - for encryption and decryption functionalities.
- **Bootstrap** - for responsive design.
- **JavaScript (jQuery)** - for handling client-side validation and AJAX requests.

## Installation

### Prerequisites
- Python 3.x installed on your system.
- Docker (optional but recommended for ease of deployment).

### Setup Instructions

1. **Clone the repository:**
