# By the way, this is a very bad import statement. I only used it because
# I did not want to list all the errors one by one. Never import with * unless
# you are extremely comfortable in what you are doing
from Auth_errors import *
import hashlib


class User:

    def __init__(self, username, password):
        self.username = username
        self.password = self.encrypt(password)
        self.is_logged = False

    def encrypt(self, password):
        password = password.encode('utf8')
        enc_password = hashlib.sha256(password).hexdigest()
        return enc_password

    def check_password(self, password):
        encrypted = self.encrypt(password)
        return encrypted == self.password

    def change_password(self, old_password, new_password):
        if self.check_password(old_password):
            encrypted_new_password = self.encrypt(new_password)
            self.password = encrypted_new_password
            print("Password changed successfully")
        else:
            print("Invalid old password entered")

    def change_username(self, old_username, old_password, new_username):
        if self.check_password(old_password):
            if old_username == self.username:
                self.username = new_username
                print("Username changed successfully")



class Authenticator:

    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        if username in self.users:
            raise UsernameExists(username)
        if len(password) < 8:
            raise PasswordTooShort(username)
        self.users[username] = User(username, password)

    def login(self, username, password):
        # Need to find out whether the person is logged in already
        if User(username, password).is_logged == True:
            raise AlreadyLoggedIn(username)

        try:
            user = self.users[username]
        except KeyError:
            raise InvalidUsername(username)

        if username in self.users:
            if not user.check_password(password):
                raise InvalidPassword()

        user.is_logged = True
        return True

    def is_logged_in(self, username):
        if username in self.users:
            return self.users[username].is_logged
        return False

authenticator = Authenticator()


class Authorizor:

    '''
    This class maps permissions to users
    '''

    def __init__(self, authenticator):
        self.authenticator = authenticator
        self.permissions = {}

    def create_permission(self, permission):
        '''
        Creates a new permission that users can be mapped to
        :param permission:
        :return:
        '''
        try:
            perm_users = self.permissions[permission]
        except KeyError:
            self.permissions[permission] = set()
        else:
            raise PermissionError()

    def give_permission(self, permission, username):
        '''
        Gives user access to a permission
        :param permission:
        :param username:
        :return:
        '''
        try:
            perm_users = self.permissions[permission]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in self.authenticator.users:
                raise InvalidUsername(username)
            perm_users.add(username)

    def revoke_permission(self, permission, username):
        '''
        Revokes permission from the user
        :param permission:
        :param username:
        :return:
        '''
        try:
            self.permissions[permission].remove(username)
        except KeyError as e:
            print("Possibly such permission {} does not exist. First you need to create such permission".format(permission))
            print("The other option is that such user {} was not given permission {} in the first place".format(username, permission))
        else:
            print("User {} does not have permission {}".format(username, permission))

    def check_permission(self, permission, username):
        '''
        Check whether certain user has a permission to perform some sort of task
        :param permission:
        :param username:
        :return:
        '''
        if username not in self.authenticator.users:
            raise InvalidPassword("User {} are not logged in".format(username))
        try:
            perm_users = self.permissions[permission]
        except KeyError:
            raise PermissionError("Permission {} does not exist".format(permission))
        else:
            if username not in perm_users:
                raise UserNotPermitted("User {} is not permitted {}".format(username, permission))
            else:
                return True
