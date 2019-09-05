import random
import string
import getpass

class User:
    '''
    This is a class in which we shall create new instances for the user
    '''
    
    def __init__(self,user_name,email,password):

        self.user_name = user_name
        self.email = email
        self.password = password
    
    user_details = []
    
    def save_user(self):

        '''
        save_user is our function in which we use to save our user items into the user_list writen above
        '''

        User.user_details.append(self)

    
    def delete_user(self):

        '''
        delete_user will remove the identified user from the user_details
        '''

        User.user_details.remove(self)

    
    def user_exists(cls,email):
        '''
        checking the existance of the mail instance
        ee
        Args:
            mail:search existance
        Returns:
            Boolean:
        '''
        for user in cls.user_details:
            if user.email.mail == email:
                        return True
        return False