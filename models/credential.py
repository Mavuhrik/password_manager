from crypto_utils import encrypt_password, decrypt_password
class Credential:
    @classmethod
    def from_dict(cls, data):
        return cls(
                        
                          data["website"],
                          data["username"],
                          data["password"],
                          encrypted = True

                          )    
    
    def __init__(self, website, username, password, encrypted = False):
        self.website = website
        self.username = username
        if encrypted:
            self.__password = password
        else:
            self.update_password(password)
        
    def update_password(self, password):
        encrypted = encrypt_password(password)
        self.__password = encrypted

    @property
    def password(self):
        return decrypt_password(self.__password)
       

    def to_dict(self):
        return {
                 "website" : self.website,
                 "username" : self.username,
                 "password" : self.__password
        }

