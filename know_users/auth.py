from flask.ext.login import LoginManager

# In order to avoid circular imports we setup the login extension
# in its own top-level module named auth:
from .users.models import User

login_manager = LoginManager()

login_manager.login_view = "users.login"

@login_manager.user_loader
def load_user(user_id):
    """
    We need to provide a user_loader callback.
    This callback is used to reload the user object from the user ID
    stored in the session.

    It should take the unicode ID of a user, and
    return the corresponding user object. For example:
    """
    return User.get(user_id)