class User:
    '''
    This is a class in which we shall create new instances for the user
    '''
    user_details = []
    def __init__(self,app_name,user_id,email):

        self.app_name = app_name
        self.user_id = user_id
        self.email = email
    
    user_details = []
    
    def save_user(self):

        '''
        save_user is our function in which we use to save our user items into the user_list writen above
        '''

        User.user_details.append(self)

    
    @classmethod
    def user_exist(cls,email):
        '''
        validating the existance of an instance of the user_details
        
        Args:
            email: search the existance of the entered email
        Returns:
            Boolean: True or false depending on the existance of the user_detail of email
        '''
        for user in cls.user_details:
            if user.email == email:
                    return True

        return False 

    def delete_user(self):

        '''
        delete_user will remove the identified user from the user_details
        '''

        User.user_details.remove(self)