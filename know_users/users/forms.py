from flask import current_app
from flask.ext.wtf import Form
from wtforms import validators,  ValidationError, BooleanField, StringField, PasswordField
from .models import User



class LoginForm(Form):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])

    # WTForms supports "inline" validators
    # of the form `validate_[fieldname]`.
    # This validator will run after all the
    # other validators have passed.
    def validate_password(form, field):
        user = User.get(form.username.data)
        if user is None:
            raise ValidationError("Unknown user")
        if not user.is_valid_password(form.password.data):
            raise ValidationError("Invalid password")

        # Make the current user available
        # to calling code.
        form.user = user

class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    #username = StringField('Username', [validators.DataRequired()])
    email = StringField('Email Address', [validators.Email()])
    #email = StringField('Email Address', [validators.DataRequired()])
    password = PasswordField('New Password', [
        validators.DataRequired(message='Your password protects you against identity theft'),
        validators.EqualTo('confirm', message='Passwords must match')])
    #password = PasswordField('New Password', [validators.DataRequired()])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS',
                              [validators.AnyOf((True,),
                                    message="You cannot register unless you accept the TOS")])

    def validate_username(self, field):
        user = User.get(self.username.data)
        if user is not None:
            raise ValidationError("This user name is already used")
        return True
