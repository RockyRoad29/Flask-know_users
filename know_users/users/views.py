from flask import Blueprint, redirect, flash, render_template, request, url_for, current_app
from flask.ext.login import login_user, login_required, logout_user
from know_users.users.forms import RegistrationForm, LoginForm
from know_users.users.models import User, all_users

bp = Blueprint('users', __name__,
                  template_folder='templates',
                  static_folder='static')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # login and validate the user...
        login_user(form.user)
        flash("Logged in successfully.")
        return redirect(url_for('index'))
    return render_template("login.html", form=form)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    current_app.logger.info("Form loaded: %r", form)
    if form.validate_on_submit():
        current_app.logger.info("Form validated for %r", form)
        user = User(form.username.data, form.email.data,
                    form.password.data)
        User.add(user)
        flash('Thanks for registering')
        return redirect(url_for('.users_list'))
    return render_template('register.html', form=form)

@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')


@bp.route("/settings")
@login_required
def settings():
    return render_template('settings.html')

@bp.route("/list")
#@login_required
def users_list():
    current_app.logger.info('%d users registered', len(all_users))
    return render_template('users_list.html', all_users=all_users)