# app.py
from flask import Flask, request, jsonify, render_template
from password import encrypt_password, decrypt_password

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    password = request.form['password']
    passphrase = request.form['passphrase']
    encrypted = encrypt_password(password, passphrase)
    return jsonify(result=encrypted)

@app.route('/decrypt', methods=['POST'])
def decrypt():
    encrypted_value = request.form['encrypted_value']
    passphrase = request.form['passphrase']
    decrypted = decrypt_password(encrypted_value, passphrase)
    return jsonify(result=decrypted)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)