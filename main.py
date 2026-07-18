from password import add_password, view_password, search_password, update_password, delete_password
from auth import login

def main():
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
            add_password()
        
        if choice == "2":
            view_password()
        
        if choice == "3":
            search_password()
        
        if choice == "4":
            update_password()
        
        if choice == "5":
            delete_password()
        
        if choice == "6":
            print("Goodbye")
            return

if __name__ == "__main__":
    if login():
       main()
