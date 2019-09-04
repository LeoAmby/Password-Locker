import unittest 
import pyperclip
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
        self.new_credentials = Credentials("Instagram","!£$%67nghe")

    def test_init(self):
        '''
        test_init test proper initialization of the credential objects or instances
        '''

        self.assertEqual(self.new_credentials.app_name,"Instagram")
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
    
    
    def delete_credentials(self):
        '''
        delete_credentials will delete identified instances of the credentials
        '''

        Credentials.credentials_details.remove(self)

if __name__ == '__main__':
    unittest.main()