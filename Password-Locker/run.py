#!/usr/bin/env python3.6
import sys
from user import User
from credentials import Credentials
import getpass

mycreds = []



def create_user(username,email,password):
    '''
    we are creating a new user_detail with this function
    '''
    new_user = User(username,email,password)
    return new_user


def save_user(user):
    '''
    A method to save user
    '''
    User.save_user(user)


def del_user(user):
    '''
    Deleting function
    '''
    user.delete_user


def check_existing_users(email):
    '''
    a function that helps in finding the existance of a user through the email and returns a boolean
    '''
    return User.user_exist(email)


def create_credentials(appname,userId,password):
    '''
    A function for creating the user credentials
    '''
    new_credentials = Credentials(appname,userId,password)
    return new_credentials


def save_credentials():
    '''
    saving of the provided credentials
    '''
    Credentials.save_credentials(mycreds)


def delete_credentials(self):
    '''
    Funtion for removing unwanted credentials
    '''
    Credentials.credentials_details.remove(self)


def generate_password():
    '''
    function that aids in password generation
    '''
    return Credentials.generate_password()

def display_credentials(cls,userId):
    '''
    Function to list existing details of the available credentials
    '''
    credentials_details = []
    for credentials in cls.credentials_details:
            if credentials.userId == userId:
                    credentials_details.append(credentials)
    return credentials_details

def find_credentials(appname):
    '''
    Finding user existance by use of the appname
    '''
    return Credentials.find_by_appname(appname)


def main():
        print("Greetings, Welcome to the lock-it command line application where we secure all your Passwords for your various appllications. Kindly Provide your name.")
        name = input()
        print(f"Hello {name}, Thank you. Kindly proceed.")
        print('\n')

        print("sign-up for Lock-It")
        first_name = input('Your First Name? ')
        last_name = input('Your Last name? ')
        username = input('Your Username? ')
        # password = input('Your Password? ')
        password = getpass.getpass()
        save_user(create_user(first_name, last_name, username))
        print(f'Dear {first_name} {last_name} your Lock-It account has been created')
        print('\n')

        print('Please Login to add create, change or update credetials of your accounts')
        print('\n')
        username = input('Enter your Lock-It username ')
        password = getpass.getpass()
       
        print('\n')
        print(f'Welcome {username}!!')
        print('\n')

        while True:
                print('Choose an abbreviated code to continue:  cc - create credentials')
                abb_code = input('Your code choice:')
                print('cc - Create Credentials; fc - Find Credentials; dc - Delete Credentials ')
                print("."*15)

                if abb_code == 'cc':
                    print('Provide your credentials: ')
                    print('\n')
                    appname = input('What\'s the name of the Application? ')
                    userId = input('Provide your desired User-ID - ')
                    mycreds.append(appname)
                    mycreds.append(userId)

                if True:
                        print('\n')
                        print('')
                        password = getpass.getpass()
                        

                        #   save_credentials(create_credentials(appname,userId,password))
                        print('\n')
                        print(f'Credentials for {appname} is created and saved')


                if abb_code == 'fc': #Find Credentials
                    print('Enter the Application name you want to search for: ')

                    app_name = input()
                    if check_existing_users(appname):
                            credentials = find_credentials(appname)
                            print(f'The list of Credentials for {appname} are: ')
                            print('\n')

                    else:
                            print('\n')
                            print('Sorry we couldn\'t find the credentials for your Application')

                elif abb_code == 'dc': #for deleting Credentials
                    print('\n')
                    print('Which Appliction credentials do you want to delete? ')
                    print('\n')

                    appname = input('Enter the Appname- ')

                    if find_credentials(appname):
                            credentials = find_credentials(appname)
                            credentials.delete_credentials()
                            

                    else:
                            print('\n')
                            print('We couldn\'t credentials for the entered Application')
        
        
                    # else abb_code == 'ex':
                    # break
            

if __name__ == '__main__':
        main()