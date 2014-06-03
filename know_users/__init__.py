from flask import Flask
from auth import login_manager
from users.views import bp as bp_users

app = Flask(__name__)


app.config.from_object('config')
app.config.from_envvar('PLAYGROUND_SETTINGS', silent=True)

@app.context_processor
def provide_constants():
    return {"constants": {"APP_NAME": "KnowUsers"}}

#db.init_app(app)

login_manager.init_app(app)

app.register_blueprint(bp_users, url_prefix='/user')
import views
