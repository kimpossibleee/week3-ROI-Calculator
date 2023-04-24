# Here, I created a class User, that asks for an email and password. If the email already exists in the system, it redirects the user to the login page.
# This was a good exercise to get used to files(retrieving the list of current user emails) and regular expressions(check if an email is valid or not)

import re
from getpass import getpass

pattern = re.compile('(\w+(-|\.)?(\w+)?)@(\w+).(org|com|edu|gov)$')

class User:
    def __init__(self):
        self.users = set()
        self.user = None

    def sign_up(self):
        with open('day5/user_info.txt') as file:
            contents = file.read()
        for name in contents.split():
            match = pattern.match(name)
            self.users.add(match.group())
        self.user = input('What is your email?: ')
        if self.user in self.users:
            print('Your email already exists. Please log-in.')
            self.log_in()
        else:
            self.check_valid_email(self.user)

    def log_in(self):
        print('Enter your password to log-in (Hint: you can press any key + "enter"): ')
        getpass()
        print('Welcome back!')

    def check_valid_email(self, email):
        match = pattern.match(email)
        if not match:
            print('Please enter a valid email.')
            self.sign_up()
        else:
            with open('day5/user_info.txt', 'a') as file:
                file.write(f'{self.user}\n')
            print('Enter a password')
            getpass()
            print('Thanks for signing up!')
