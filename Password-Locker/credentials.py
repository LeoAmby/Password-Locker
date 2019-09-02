class Credentials:
    '''
    This is a class that helps generate new instances of the user credentials
    '''
    credentials_details = []
    def __init__(self,app_name,password):
        self.app_name = app_name
        self.password = password
        
    def save_credentials(self):

        '''
        save_credentials meant to save the user's provided instances of the credentials_details
        '''
        Credentials.credentials_details.append(self)

    # def delete_credentials
    #     '''
    #     This method clears the credentials entered
    #     '''
    #     Credentials.credentials_details.remove  