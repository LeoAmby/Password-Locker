#!/usr/bin/env python3.6
from user import User

def create_user(appname,userid,email):
    '''
    we are creating a new user_detail with this function
    '''
    new_user = User(appname,userid,email)
    return new_user

def save_users(user):
    '''
    A method to save user
    '''
    user.save_user()

def del_user(user):
    '''
    Deleting function
    '''
    user.delete_user