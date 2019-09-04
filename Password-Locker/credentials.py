import random
import string
import getpass
from user import User

class Credentials:
    '''
    This is a class that helps generate new instances of the user credentials
    '''
    
    def __init__(self,app_name,userId,password):
        
        self.app_name = app_name
        self.userId = userId
        self.password = password


    credentials_details = []
        
    def save_credentials(self):

        '''
        save_credentials meant to save the user's provided instances of the credentials_details
        '''
        Credentials.credentials_details.append(self)

    
    def delete_credentials(self):
        '''
        A method method for clearing unwanted information
        '''
        Credentials.credentials_details.remove(self)



    @classmethod
    def generate_password(cls):
        '''
        A function for password generation
        '''
        password = string.ascii_lowercase
        return "".join(random.choice(password)for i in range (12))

    def display_credentials(cls,userId):
        '''
        a function for displaying the provided credential details
        '''
        credentials_details = [] 
        for credentials in cls.credentials_details:
                if credentials.userId == userId:
                        credentials_details.append(credentials)
        return credentials_details