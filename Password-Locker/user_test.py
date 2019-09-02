import unittest 
from user import User

class TestUser(unittest.TestCase):
    '''
    This is a test class which defines various cases for the user class behaviours.
    Args:
        unittest.TestCase: TestCase class helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Instagram","waiver","mwamtoleo@gmail.com")

    def test_init(self):
        '''
        test_init test proper initialization of the user objects or instances
        '''

        self.assertEqual(self.new_user.account_type,"Instagram")
        self.assertEqual(self.new_user.user_id,"waiver")
        self.assertEqual(self.new_user.email,"mwamtoleo@gmail.com")

    def test_save_user(self):
        '''
        test_save_user test for clarity that the instances of the user are saved and can be found within the object
        '''

        self.new_user.save_user()

        self.assertEqual(len(User.user_details),1)
    
    def tearDown(self):
        '''
        This is our method that will aid in cleaning up every case that has completed running
        '''

        User.user_details = []
    
    def test_save_multiple_user(self):
        '''
        test_save_multiple_user for purposes of ensuring we can save more than one user instances to out user_details
        '''
        self.new_user.save_user()
        test_user = User("Linkedin","littlestar","mwamtoleo@gmail.com")
        test_user.save_user()
        self.assertEqual(len(User.user_details),2)

    def test_delete_user(self):

        '''
        test_delete_user for identifying whether we are in a position to remove or clear a specific user in the available user-details
        '''
        User.user_details.remove(self)


if __name__ == '__main__':
        unittest.main()