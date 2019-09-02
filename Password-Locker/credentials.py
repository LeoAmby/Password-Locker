class Credentials:
    '''
    This is a class that helps generate new instances of the user credentials
    '''
    credentials_details = []
    def __init__(self,account_type,login,password):
        self.account_type = account_type
        self.login = login
        self.password = password
        
    def save_credentials(self):

        '''
        save_credentials meant to save the user's provided instances of the credentials_details
        '''