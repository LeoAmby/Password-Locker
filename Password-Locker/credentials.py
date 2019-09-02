class Credentials:
    '''
    This is a class that helps generate new instances of the user credentials
    '''
    credentials_details = []
    def __init__(self,account_type,login,password):
        self.account_type = account_type
        self.login = login
        self.password = password