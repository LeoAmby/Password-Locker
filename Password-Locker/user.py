class User:
    '''
    This is a class in which we shall create new instances for the user
    '''
    user_details = []
    def __init__(self,account_name,user_id,email):

        self.account_name = account_name
        self.user_id = user_id
        self.email = email