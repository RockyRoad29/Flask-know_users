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
    #username = StringField('Username', [validators.Length(min=4, max=25)])
    username = StringField('Username')
    #email = StringField('Email Address', [validators.Length(min=6, max=35)])
    email = StringField('Email Address')
    #password = PasswordField('New Password', [
    #password = PasswordField('New Password')
    #confirm = PasswordField('Repeat Password')
    #accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

    #def validate