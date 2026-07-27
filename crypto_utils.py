import os
from cryptography.fernet import Fernet
from cryptography.fernet import Fernet, InvalidToken

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KEY_FILE = os.path.join(BASE_DIR, "key.key")

def generate_key():
    return Fernet.generate_key()

def save_key():
    key = generate_key()
    with open(KEY_FILE, "wb") as file:
         file.write(key)

def load_key():
    with open(KEY_FILE, "rb") as file:
        return file.read()
    
def get_cipher():
    key = load_key()
    return Fernet(key)

def encrypt_password(password):
    cipher = get_cipher()
    try:
        password_bytes = password.encode("utf-8")
        encrypted_password = cipher.encrypt(password_bytes)
        return encrypted_password.decode("utf-8")
    except InvalidToken:
        return None

def decrypt_password(password):
    cipher = get_cipher()
    encrypted_password = password.encode("utf-8")
    decrypted_password = cipher.decrypt(encrypted_password)
    return decrypted_password.decode("utf-8")