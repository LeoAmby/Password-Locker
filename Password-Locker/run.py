#!/usr/bin/env python3.6
import sys
from user import User
from credentials import Credentials
import getpass



class Final:
    def create_user(appname,userid,email):
        '''
        we are creating a new user_detail with this function
        '''
        new_user = User(app_name,user_id,email)
        return new_user
    
    def create_credentials(appname,login,password):
        '''
        A function for creating the user credentials
        '''
        new_credentials = Credentials(appname,login,password)
        return new_credentials

    def save_user(user):
        '''
        A method to save user
        '''
        User.save_user()

    def save_credentials(credentials):
        '''
        saving of the provided credentials
        '''
        Credentials.save_credentials()

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

    def generate_password():
        '''
        function that aids in password generation
        '''
        return Credentials.generate_password()

    def main():
        print("Greetings, Welcome to the lock-it command line application where we secure all your Passwords for your various appllications. Kindly Provide your name..")
        name = input()
        print(f"Hello {name}, Thank you. Kindly proceed.")
        print('\n')

        print("new user")
        print("."*15)

        print("What is your unique User_ID...")
        userID = input()

        print("Provide your password...")
        password = getpass.getpass()

        print("Your email address...")
        email = input()

        print("Access your account by logging in now...")
        print('\n')

        print("Provide your user-ID")
        user_id = input()

        print("Password..")
        password = getpass.getpass()

        if userID == user_id and password == password:
            print("Welcome... You are now logged in!!")
            print('\n')
        
        else:print("You have either entered a wrong user-id or password!! Try Again")

        while True:
            print("These are abbrevations to the input required from you, kindly use them appropriately: cu - create new_user, du - display user, fu - find user, and ex - exit user details ")
            code_abbreviation = input().lower()


            if code_abbreviation == 'cu':
                    print("New User")
                    print("."*15)

                    print ("app_name")
                    app_name = input()

                    print ("user_id")
                    user_id = input()

                    print("email")
                    email = input()

                    print ("login")
                    login = input()

                    print ("password")
                    password = getpass.getpass()

                    save_user(create_user(app_name,user_id,email)) #create and save the user inputs and details

                    print('\n')
                    print(f"New User {app_name} {user_id} {email}")

                    print('\n')

            elif code_abbreviation == 'du':

                    if display_user():

                        print("These are your details for the application mentioned")

                        print('\n')
                        for user in display_user():
                            print(f"{user.app_name} {user.user_id} {user.email} {user.login}")

                            print('\n')
                    else:

                        print('\n')
                        print("Kindly create some user details for various application to  be able do view under display")

                        print ('\n')

            elif code_abbreviation == 'fu':

                    print("Which email would you like to search for?")

                    search_email = input()
                    if check_existing_user(search_email):
                                
                            search_user = find_user(search_email)

                            print(f"{search_user.user_id} {search_user.login}")

                            print(f"app_name...{search_user.app_name}")

                            print(f"Email address...{search_user.email}")

                    else:
                            print("We cant find a user that matches your details")

            elif code_abbreviation == "ex":
                    print("Adios Amigos, Thank you for your time!")

            else:
                    print("Kindly make use of the code abbreviations provided. Thank you")


    if __name__ == '__main__':
        main()