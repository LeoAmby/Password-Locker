import unittest 
from credentials import Credentials

class TestUser(unittest.TestCase):

    '''
    This is a test class which defines various cases for the credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class helps in creating test cases
    '''

    #Check if items are being instantiated corectly

    def setUp(self):
        '''
        run before each test cases
        '''

        self.new_credentials = Credentials("Instagram", "waiver", mwamtoleo@gmail.com)