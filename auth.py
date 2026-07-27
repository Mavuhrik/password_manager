from getpass import getpass
from storage import load_master_password, save_master_password
from utils import hash_password, verify_password

def setup_master_password():
    password = getpass("Enter your master password: ")

    confirm_password = getpass("Confirm master password: ")
    if confirm_password != password:
        print("Passwords do not match")
        return False
    hashed_password = hash_password(password)
    master_password = {
        "master_password": hashed_password
    }
    save_master_password(master_password)
    print("Master password created.")
    return True


def login():
    while True:
        access = load_master_password()
        if not access:
           print("====Create master password====")
           if setup_master_password():
              return True
        else:
            enter_password = getpass("Master password: ")
            if verify_password(enter_password, access):
                print("Log in successful")
                return True
            else:
                print("Login failed.Incorrect password")
                continue
     


        