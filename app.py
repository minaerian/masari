from flask import Flask, request, jsonify, render_template
#from crypto import decrypt_password  # Import decrypt_password instead of decrypt
from cryptography.hazmat.primitives.kdf.pbkdf2 import InvalidKey
from cryptography.exceptions import InvalidSignature
from crypto import encrypt, decrypt_password


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt_route():
    try:
        data = request.json
        words = data.get('words')
        passphrase = data.get('passphrase')
        
        # Ensure inputs are not empty or invalid
        if not words or not passphrase:
            return jsonify(result="Error: Words or passphrase cannot be empty"), 400
        
        # Perform encryption
        encrypted_value = encrypt(words, passphrase)
        
        return jsonify(result=encrypted_value)
    except Exception as e:
        app.logger.error(f"An error occurred: {e}")
        return jsonify(result=f"Error: {str(e)}"), 500


@app.route('/decrypt', methods=['POST'])
def decrypt_route():
    try:
        data = request.json
        encrypted_value = data.get('encrypted_value')
        passphrase = data.get('passphrase')
        
        # Perform decryption using the correct function
        decrypted_value = decrypt_password(encrypted_value, passphrase)
        
        return jsonify(result=decrypted_value)
    except InvalidKey:
        return jsonify(result="Error: Incorrect passphrase"), 400
    except InvalidSignature:
        return jsonify(result="Error: Decryption failed due to invalid signature or padding (likely an incorrect passphrase)"), 400
    except ValueError:
        return jsonify(result="Error: Decryption failed due to padding issues (likely an incorrect passphrase)"), 400
    except Exception as e:
        app.logger.error(f"An error occurred: {e}")
        return jsonify(result=f"Error: {str(e)}"), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
