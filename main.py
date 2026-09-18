from models.password_manager import PasswordManager
from utils import password_strength
from auth import login
from storage import CREDENTIALS_FILE
import pyperclip

def select_credential(manager, website):
    matches = manager.find_credential(website)

    if not matches:
        return None
    
    while True:
        for i, credential in enumerate(matches, start=1):
            print(
                f"{i}.{credential.website} | "
                f"{credential.username}"
            )
        try:
            choice = int(input("Choose account: "))
        except ValueError:
            print("Invalid choice.")
            continue
        if not 1 <= choice <= len(matches):
            print("Invalid choice.")
            continue
        return matches[choice - 1]
    
def main():
    manager = PasswordManager()
    manager.load_json(CREDENTIALS_FILE)
    while True:
        print("""===Password Manager===
            1.Add new password
            2.View password
            3.Search password
            4.Update password
            5.Delete password
            6.Exit
            """)
        choice = input("What would it be: ")
        if not choice.isdigit():
            print("Enter numbers only")
            continue

        if choice not in ('1', '2', '3', '4', '5', '6'):
            print("enter number 1-6 only")
            continue
        
        if choice == "1":
            website = input("Enter website name: ")
            username = input("Enter website username: ")
            password = input("Enter Password: ")
            strength = password_strength(password)
            print(f"Password strength: {strength}")
            success = manager.add_credential(website, username, password)
            if success:
                manager.save_to_json(CREDENTIALS_FILE)
                print("Password Added successfully ")
                continue
                
        if choice == "2":
           if not manager.credentials:
               print("You don't have a saved password")
               continue
           for i, credential in enumerate(manager.credentials, start=1):
               masked_password = "*" * 8
               print(f"{i}.Website - {credential.website}|"
                     f"Username - {credential.username}|"
                     f"Password - {masked_password}"
                     )
           while True:
                reveal = input("Would you like to reveal password (y/n): ").strip().lower()

                if reveal not in ('y', 'n'):
                    print("Invalid input. Enter only y or n")
                    continue
                if reveal == 'y':
                    try:
                        choice = int(
                            input("Choose account (numbers only): ")
                        )
                    except ValueError:
                        print("Enter numbers only")
                        continue
                    if not 1 <= choice <= len(manager.credentials):
                        print("Invalid choice.")
                        continue
                    credential = manager.credentials[choice - 1]
                    print(f"Website - {credential.website}\nUsername - {credential.username}\nPassword - {credential.password}\n")
                break

        if choice == "3":
           website = input("Enter website name: ").lower()

           if not manager.credentials:
              print("No saved password.")
              continue
           credential = select_credential(manager, website)
           if credential:
              print(f"Website: {credential.website}\nUsername: {credential.username}\nPassword: {credential.password}")
              while True:
                    copy = input("Copy password to clipboard (Y/N): ").strip().lower()
                    if copy not in ('y', 'n'):
                        print("Invalid input. Enter y or n")
                        continue
                    if copy == "y":
                        pyperclip.copy(credential.password)
                        print("Password copied to clipboard.")
                    break 
            
        if choice == "4":
            website = input("Enter website name: ").lower()
            credential = select_credential(manager, website)
            if not credential:
                print("Does not exist")
                continue
            print(
                    f"Website - {credential.website}\n"
                    f"Username - {credential.username}\n"
                    f"Password - {credential.password}\n"
            )
            new_username = input("Enter new username (leave blank to keep current username): ").strip()
            new_password = input("Enter new password (leave blank to keep current password): ").strip()
            success = manager.update_credential(credential.website,
                                                credential.username,
                                                new_username = new_username or None,
                                                new_password = new_password or None)
            if not new_username and not new_password:
                print("No changes made.")
                continue
            
            if success:
                manager.save_to_json(CREDENTIALS_FILE)
                print("Password update successful")
            else:
                print("Does not exist")

        if choice == "5":
           if not manager.credentials:
              print("No saved password.")
              continue
           website = input("Enter website name: ").lower()

           credential = select_credential(manager, website)

           if not credential:
              print("Does not exist")
              continue
           success = manager.delete_credential(credential.website, credential.username)
           if success:
              manager.save_to_json(CREDENTIALS_FILE)
              print("Password deleted successfully")

        if choice == "6":
            print("Goodbye")
            return

if __name__ == "__main__":
    if login():
       main()
