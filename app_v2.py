from flask import Flask, request, jsonify, render_template
from crypto_v2 import encrypt, decrypt_password

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt_route():
    data = request.json
    words = data.get('words')
    passphrase = data.get('passphrase')
    if not words or not passphrase:
        return jsonify(result="Error: Words or passphrase cannot be empty"), 400
    encrypted_value = encrypt(words, passphrase)
    return jsonify(result=encrypted_value)

@app.route('/decrypt', methods=['POST'])
def decrypt_route():
    data = request.json
    encrypted_value = data.get('encrypted_value')
    passphrase = data.get('passphrase')
    try:
        decrypted_value = decrypt_password(encrypted_value, passphrase)
        return jsonify(result=decrypted_value)
    except Exception as e:
        return jsonify(result=f"Error: {str(e)}"), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
