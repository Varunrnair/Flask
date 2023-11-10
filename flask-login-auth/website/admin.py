from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from .models import Note, User

admin = Admin()

def init_app(app, db):
    admin.init_app(app)
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Note, db.session))
