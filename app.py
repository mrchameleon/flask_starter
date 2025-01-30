import secrets
from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from database import db
from flask_cors import CORS
from models import *
from routes import route_blueprint


DB_NAME = 'local.db'

def create_app():
    """initializing the flask application"""
    application = Flask(
        __name__,
        static_url_path='', 
        static_folder='static',
        template_folder='templates'
    )
    application.register_blueprint(route_blueprint)
    # prevent sorting behavior, so our preferred ordering is retained
    application.json.sort_keys = False

    application.config['CORS_HEADERS'] = 'Content-Type'
    CORS(application, resources={r"/*": {"origins": "http://localhost:5173"}})

    with application.app_context():
        application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DB_NAME
        application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(application)
        db.create_all()

    return application

app = create_app()
secret_key = secrets.token_urlsafe(16)
app.config['SECRET_KEY'] = secret_key

# themes reference: https://bootswatch.com/3/
app.config['FLASK_ADMIN_SWATCH'] = 'united'
# admin reference: https://flask-admin.readthedocs.io/en/stable/introduction/#getting-started
admin = Admin(app, name='flask_starter', template_mode='bootstrap3')

class AdminModelView(ModelView):

    column_searchable_list = ['name']
    page_size = 100

admin.add_view(AdminModelView(User, db.session))

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
