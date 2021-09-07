class User:
    is_logged_in = None
    users = {}

    def __init__(self, username, password):
        self.username = username
        self.password = password
        User.users[self.username] = self.password

    # def __repr__(self):
    #     return f'User "{self.username}", Logging in status: {User.is_logged_in}'


with open("users and passwords.txt") as f:
    for line in f:
        user_pass = line.split(', ')
        User(user_pass[0], user_pass[1].strip())
