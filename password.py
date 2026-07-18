import pyperclip
from storage import save_credentials, load_credentials

def add_password():
    website = input("Enter website name: ").lower()
    username = input("Enter website username: ")
    password = input("Enter website password: ")
    strength = password_strength(password)
    if strength == "weak":
        print("Website password is weak.you should consider changing it.")

    credentials = {
        "website":website,
        "username":username,
        "password":password
    }
    credentials_data = load_credentials()
    credentials_data.append(credentials)
    save_credentials(credentials_data)
    print("Password added successfully")
    return credentials

def password_strength(password):
    length_check = len(password) >= 8
    digit_check = any(char.isdigit() for char in password)
    uppercase_check = any(char.isupper() for char in password)
    lowercase_check = any(char.islower() for char in password)
    if (length_check and digit_check and uppercase_check and lowercase_check):
        return "strong"
    else:
        return "weak"

def view_password():
    credentials_data = load_credentials()
    if not credentials_data:
        print("You don't have any saved password.")
        return
    passwords = credentials_data
    if not passwords:
        return None
    
    for i, credentials in enumerate(passwords, start=1):
        masked_password = "*" * len(credentials["password"])
        print(f"{i}.Website - {credentials['website']} | Username - {credentials['username']} | Password - {masked_password}\n")
    while True:
        reveal = input("Would you like to reveal password(y/n): ").strip().lower()
        if reveal not in ('y', 'n'):
            print("Invalid input.Enter only y or n")
            continue
        if reveal == 'y':
            try:
               choice = int(input("Choose account(numbers only): "))
            except ValueError:
                print("Enter numbers only")
                continue
            if not 1 <= choice <= len(passwords):
                print("Invalid choice.")
                continue
            selected = passwords[choice - 1]
            print(f"Website - {selected['website']}\n Username - {selected['username']}\n Password - {selected['password']}\n")
            break
        if reveal == 'n':
            break

def update_password():
    credentials_data = load_credentials()
    if not credentials_data:
        print("You don't have any saved password.")
        return
    website_name = input("Enter website name: ")

    selected = select_password(website_name, credentials_data)
    if selected:   
        print(f"Website - {selected['website']}\n Username - {selected['username']}\n Password - {selected['password']}\n")

        new_username = input("Enter new username(leave blank to keep current username): ")
        new_password = input("Enter new password(leave blank to keep current password): ")
        
        if new_username:
            selected["username"] = new_username
        if new_password:
            selected["password"] = new_password

        save_credentials(credentials_data)
        print("Password updated successfully")
        return
    print("Does not exist")


def delete_password():
    credentials_data = load_credentials()
    if not credentials_data:
        print("No saved password.")
        return
    website_name = input("Enter website name: ")

    selected = select_password(website_name, credentials_data)
    if selected:
        credentials_data.remove(selected)
        print("Password deleted successfully")
        save_credentials(credentials_data)
        return      
    print("Does not exist")

def select_password(website_name, credentials_data):
    matches = []
    for credentials in credentials_data:
        if website_name == credentials["website"]:
           matches.append(credentials)

    if not matches:
       return None

    while True:
        for i, credentials in enumerate(matches, start=1):
            print(f"{i}.{credentials['website']} | {credentials['username']}")
        
        try:
            choice = int(input("choose account: "))
        except ValueError:
            print("Invalid choice.")
            continue
        if not 1 <= choice <= len(matches):
            print("Invalid choice.")
            continue

        selected = matches[choice - 1]
        return selected

def search_password():
    credentials_data = load_credentials()
    website_name = input("Enter website name: ")
    if not credentials_data:
        print("No saved password.") 
        return
    selected = select_password(website_name, credentials_data)
    if selected:
        print(f"Website: {selected['website']}\n Username: {selected['username']}\n Password: {selected['password']}")
        while True:
            copy = input("Copy password to clipboard.(Y/N): ").strip().lower()
            if copy not in ('y', 'n'):
                print("Invalid input.Enter y or n")
                continue
            if copy == "y":
                pyperclip.copy(selected['password'])
                print("Password copied to clipboard.")
                return
            if copy == "n":
               return
    else:
        print("Does not exist")
