from hashlib import blake2s
from exceptions import *
from user import *


class Authenticator:
    users = User.users

    def __repr__(self):
        n = input('** Welcome! "sign up" or "log in" or "nothing" ** \n').strip()
        print()
        if n == "sign up":
            return f'{self.add_user()}'
        elif n == "log in":
            return f'{self.login()}'
        elif n == "nothing":
            return f''
        else:
            print('" Sorry! Just input the words "sign up" or "log in" or "nothing". "')
            print()
            return f'{Authenticator()}'

    @staticmethod
    def add_user():
        try:
            print('* You\'re signing up. If you want to go back to the main menu, write "back". *\n')
            new_username = input('enter username: ')
            print()
            if new_username == 'back':
                return Authenticator()
            new_userpass = input('enter password: ')
            if new_username in Authenticator.users:
                raise UsernameAlreadyExists('This username has already taken.')
            elif len(new_userpass) < 8:
                raise PasswordTooShort('Your password should consist of at least 8 character.')
            else:
                User(new_username, blake2s(new_userpass.encode()).hexdigest())
                with open("users and passwords.txt", "a+") as fi:
                    fi.write(f'{new_username}, {blake2s(new_userpass.encode()).hexdigest()}\n')
                return Authenticator()
        except AuthException as err:
            print()
            print(err)
            return Authenticator.add_user()

    @staticmethod
    def login():
        global username, password
        print('* You can log in. If you want to go back to the main menu, write "back". *\n')
        username = input('username: ')
        print()
        if username == 'back':
            return Authenticator()
        password = input('password: ')
        return Authenticator.is_logged_in()

    @staticmethod
    def is_logged_in():
        try:
            if username not in Authenticator.users:
                raise InvalidUsername("You've entered an invalid username.")
            elif blake2s(password.encode()).hexdigest() != Authenticator.users[username]:
                raise InvalidPassword("You've entered an invalid password.")
            else:
                User.is_logged_in = True
                print(f'User "{username}", Logging in status: {User.is_logged_in}')
                print()
                return Authenticator()
        except AuthException as err:
            print(err)
            User.is_logged_in = False
            print(f'User "{username}", Logging in status: {User.is_logged_in}')
            print()
            return Authenticator.login()
