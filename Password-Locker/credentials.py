class Credentials:
    '''
    This is a class that helps generate new instances of the user credentials
    '''
    
    def __init__(self,app_name,password):
        self.app_name = app_name
        self.password = password

    credentials_details = []
        
    def save_credentials(self):

        '''
        save_credentials meant to save the user's provided instances of the credentials_details
        '''
        Credentials.credentials_details.append(self)

    def delete_details(self):
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

    