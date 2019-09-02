class User:
    '''
    This is a class in which we shall create new instances for the user
    '''
    user_details = []
    def __init__(self,account_type,user_id,email):

        self.account_type = account_type
        self.user_id = user_id
        self.email = email
    
    user_details = []
    def save_user(self):

        '''
        save_user is our function in which we use to save our user items into the user_list writen above
        '''

        User.user_details.append(self)

    def user_exist(self):