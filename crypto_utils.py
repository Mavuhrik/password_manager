from cryptography.fernet import Fernet
def generate_key():
    return Fernet.generate_key()
print(generate_key())