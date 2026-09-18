from .credential import Credential
import json
class PasswordManager:
    def __init__ (self):
        self.credentials = []

    def add_credential(self, website, username, password):
        credential = Credential(website, username, password)
        self.credentials.append(credential)
        return True

    def delete_credential(self, website, username):
       found = False
       for credential in self.credentials:
           if credential.website == website and credential.username == username:   
              self.credentials.remove(credential)
              found = True
              break
       return found

    def search_credential(self, website, username):
        for credential in self.credentials:
            if credential.website == website and credential.username == username:
                return credential    
        return None 

    def find_credential(self, website):
        matches = []
        for credential in self.credentials:
            if credential.website == website:
                matches.append(credential)
        return matches
    
    def update_credential(self, 
                          website, 
                          username,
                          new_username =  None,
                          new_password = None):
        
        credential = self.search_credential(website, username) 
        if not credential:
           return False

        if new_username is not None:
            credential.username = new_username

        if new_password is not None:
           credential.update_password(new_password)
        return True

    def save_to_json(self, filename):
        data = []
        for credential in self.credentials:
            data.append(credential.to_dict())
        try:
            with open(filename, "w" ) as file:
                json.dump(data, file, indent=4)
                return True
        except(OSError, TypeError):
            return False

    def load_json(self, filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
            loaded_credentials = []   
            for item in data:
                credential = Credential.from_dict(item)
                loaded_credentials.append(credential)
            self.credentials = loaded_credentials
            return True
        except(OSError, json.JSONDecodeError):
                return False
