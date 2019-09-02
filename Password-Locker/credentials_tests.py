import unittest 
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    '''
    This is a test class which defines various cases for the credential class behaviours.
    
    Args:
        unittest.TestCase: TestCase class helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("Instagram","photogenic","!£$%67nghe")

    def test_init(self):
        '''
        test_init test proper initialization of the credential objects or instances
        '''

        self.assertEqual(self.new_credentials.account_type,"Instagram")
        self.assertEqual(self.new_credentials.login,"photogenic")
        self.assertEqual(self.new_credentials.password,"!£$%67nghe")

    def test_save_credentials(self):
        '''
        test_save_credentials test for clarity that the instances of the credentials are saved and can be found within the object
        '''

        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_details),1)
    
    def tearDown(self):
        '''
        This is our method that will aid in cleaning up every case that has completed running
        '''

        Credentials.credentials_details = []
    
    
    def test_delete_credentials(self):

        '''
        test_delete_credentials for identifying whether we are in a position to remove or clear a specific credentials
        '''
        Credentials.credentials_details.remove(self)


if __name__ == '__main__':
    unittest.main()