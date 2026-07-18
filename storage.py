import json
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CREDENTIALS_FILE = os.path.join(BASE_DIR, "credentials.json")
MASTER_PASSWORD_FILE = os.path.join(BASE_DIR, "master_password.json")

def save_credentials(credentials):
    with open(CREDENTIALS_FILE, "w") as file:
        json.dump(credentials, file, indent=4)

def load_credentials():
    try:
         with open(CREDENTIALS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return[] 
    

def save_master_password(master_password):
    with open(MASTER_PASSWORD_FILE, "w") as file:
        json.dump(master_password, file, indent=4)

def load_master_password():
    try:
        with open(MASTER_PASSWORD_FILE, "r") as file:
            master_password =json.load(file)
            return master_password["master_password"]
    except (FileNotFoundError, json.JSONDecodeError):
        return None