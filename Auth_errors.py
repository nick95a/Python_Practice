class AuthException(Exception):

    def __init__(self, username = "", user = None):
        super().__init__(username, user)
        self.username = username
        self.user = user


class UsernameExists(AuthException):
    def __init__(self, username):
        super().__init__(username)
        print("Username {} already exists".format(username))

class PasswordTooShort(AuthException):
    def __init__(self, username):
        super().__init__(username)
        print("Please provide another password for this {} user as this one is too short".format(username))
        print("Password needs to have at least 8 symbols")

class AlreadyLoggedIn(AuthException):
    def __init__(self, username):
        print("No need to login twice, {} my friend".format(username))

class InvalidPassword(AuthException):
    pass

class InvalidUsername(AuthException):
    def __init__(self, username):
        super().__init__(username)
        print("You have entered an invalid username {}".format(username))

class PermissionError(AuthException):
    pass

class UserNotPermitted(AuthException):
    pass