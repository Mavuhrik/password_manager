# Password Manager CLI

A command-line password manager built with Python. It allows users to securely store, view, search, update, and delete website credentials from the terminal.

I initially built this project using a procedural approach and later refactored it using object-oriented programming. The refactor helped me better understand classes, objects, encapsulation, class methods, properties, and how to separate responsibilities across different parts of an application.

## Features

- Master password authentication
- Master password hashing with bcrypt
- Password encryption and decryption using Fernet
- Add new website credentials
- View saved credentials with masked passwords
- Reveal a selected password
- Search credentials by website
- Select between multiple accounts belonging to the same website
- Update usernames and passwords
- Delete saved credentials
- Password-strength checking utility
- Persistent JSON storage
- Copy passwords to the clipboard

## Technologies Used

- Python
- Object-Oriented Programming
- JSON
- bcrypt
- cryptography
- Fernet
- pyperclip
- Git and GitHub

## Project Structure

```text
password_manager/
│
├── main.py
├── auth.py
├── crypto_utils.py
├── storage.py
├── utils.py
│
├── models/
│   ├── __init__.py
│   ├── credential.py
│   └── password_manager.py
│
├── .gitignore
└── README.md
```

### File Responsibilities

- `main.py` — Handles the command-line interface and user interaction.
- `auth.py` — Handles master password setup and login.
- `crypto_utils.py` — Handles password encryption and decryption.
- `storage.py` — Handles file paths and storage-related operations.
- `utils.py` — Contains reusable utility functions, including password-strength checking.
- `models/credential.py` — Defines the `Credential` class.
- `models/password_manager.py` — Defines the `PasswordManager` class and manages the credential collection.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Mavuhrik/password_manager.git
```

### 2. Navigate into the project directory

```bash
cd password_manager
```

### 3. Install the required dependencies

```bash
pip install bcrypt cryptography pyperclip
```

### 4. Run the application

```bash
python main.py
```

## Usage

When the application starts, you will be prompted to create or enter your master password.

After a successful login, you can choose from the following options:

```text
1. Add new password
2. View password
3. Search password
4. Update password
5. Delete password
6. Exit
```

When searching for a website with multiple saved accounts, the application displays the matching usernames so you can select the specific account you want to access.

## Security Notes

- The master password is stored as a bcrypt hash rather than plaintext.
- Website passwords are encrypted before being stored in the JSON file.
- The encryption key is stored locally.
- Credential data, the master-password file, and the encryption key should not be uploaded to GitHub.
- This project is intended for learning and personal use and has not been professionally audited for security.

## Future Improvements

- Hide password input using `getpass`
- Improve password-strength analysis
- Add automatic password generation
- Add unit tests
- Improve error handling
- Improve the terminal interface
- Implement more secure key management
- Package the application for easier installation

## What I Practiced

Through this project, I practiced:

- Python functions and modules
- File handling
- JSON serialization and deserialization
- Password hashing
- Encryption and decryption
- Object-oriented programming
- Classes and objects
- Encapsulation
- Properties
- Class methods
- Separation of responsibilities
- Git and GitHub