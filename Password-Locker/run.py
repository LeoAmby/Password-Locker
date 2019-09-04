#!/usr/bin/env python3.6
import sys
from user import User
from credentials import Credentials
import getpass




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


def verify_user(username,password):
    '''
    Checks if the user already exists before recreating another one
    '''
    check_user = Credentials.check_user(username,password)
    return check_user


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


def save_credentials(credentials):
    '''
    saving of the provided credentials
    '''
    Credentials.save_credentials()


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


def main():
        print("Greetings, Welcome to the lock-it command line application where we secure all your Passwords for your various appllications. Kindly Provide your name..")
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

        # print("new user")
        # print("."*15)

        # print("What is your unique User_ID...")
        # userID = input()

        # print("Provide your password...")
        # password = getpass.getpass()

        # print("Your email address...")
        # email = input()

        # print("Access your account by logging in now...")
        # print('\n')

        # print("Provide your user-ID")
        # user_id = input()

        # print("Password..")
        # password = getpass.getpass()

        # if userID == user_id and password == password:
        #     print("Welcome... You are now logged in!!")
        #     print('\n')
        
        # else:print("You have either entered a wrong user-id or password!! Try Again")

        # while True:
        #     print("These are abbrevations to the input required from you, kindly use them appropriately: cu - create new_user, du - display user, fu - find user, and ex - exit user details ")
        #     code_abbreviation = input().lower()


        #     if code_abbreviation == 'cu':
        #             print("New User")
        #             print("."*15)

        #             print ("app_name")
        #             app_name = input()

        #             print ("user_id")
        #             user_id = input()

        #             print("email")
        #             email = input()

        #             print ("login")
        #             login = input()

        #             print ("password")
        #             password = getpass.getpass()

        #             # save_user(create_user(app_name,user_id,email)) #create and save the user inputs and details

        #             print('\n')
        #             print(f"New User {app_name} {user_id} {email}")

        #             print('\n')

        #     elif code_abbreviation == 'du':

        #             if display_user():

        #                 print("These are your details for the application mentioned")

        #                 print('\n')
        #                 for user in display_user():
        #                     print(f"{user.app_name} {user.user_id} {user.email} {user.login}")

        #                     print('\n')
        #             else:

        #                 print('\n')
        #                 print("Kindly create some user details for various application to  be able do view under display")

        #                 print ('\n')

        #     elif code_abbreviation == 'fu':

        #             print("Which email would you like to search for?")

        #             search_email = input()
        #             if check_existing_user(search_email):
                                
        #                     search_user = find_user(search_email)

        #                     print(f"{search_user.user_id} {search_user.login}")

        #                     print(f"app_name...{search_user.app_name}")

        #                     print(f"Email address...{search_user.email}")

        #             else:
        #                     print("We cant find a user that matches your details")

        #     elif code_abbreviation == "ex":
        #             print("Adios Amigos, Thank you for your time!")

        #     else:
        #             print("Kindly make use of the code abbreviations provided. Thank you")


if __name__ == '__main__':
        main()