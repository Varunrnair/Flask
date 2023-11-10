from flask import Blueprint, render_template
from flask_login import login_required, current_user
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from website.models import User, Note
from website.db import db

#admin_bp = Blueprint('admin', __name__)
admin = Admin()
admin_bp = Blueprint('admin', __name__)
"""
@admin.route('/admin')
@login_required
def admin_home():
"""

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Note, db.session))
 #   return render_template('admin/admin_home.html', user=current_user)

