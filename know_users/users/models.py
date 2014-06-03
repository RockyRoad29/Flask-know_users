from flask import current_app, request
from flask.ext.login import UserMixin

# No database here, for now we use a simple (no-persistent) dict

all_users = {}

class User(UserMixin):
    def __init__(self, username, email, password):
        self.id = username
        self.email = email
        self.password = password

    @classmethod
    def get(cls, user_id):
        """
        Retrieve a user from his login name.

        :param user_id: unicode ID of a user, as store by Flask-Login in session.
        :return: the corresponding user object, or `None` if user_id is not valid
        """
        return all_users.get(user_id)

    @classmethod
    def add(cls, user):
        assert isinstance(user, User)
        user_id = user.get_id()
        assert(user_id not in all_users)
        all_users[user_id] = user

        if request:
            current_app.logger.info("User %r added", user_id)

    def is_valid_password(self, password):
        # TODO encrypt password when persisted
        return password and self.password == password

User.add(User('admin','admin@example.com', 'default'))