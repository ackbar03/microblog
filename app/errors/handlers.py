from flask import render_template
from app.errors import bp
from app import db ###Michael: db still initialized in the _init_ under the app, a lot of things still are, its
#### mostly only the routing

@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@bp.app_errorhandler(500) ###Michael: note that this matters, the app_errorhandler instead of errorhandler.
def internal_error(error):
    db.session.rollback()
    return render_template('errors/500.html'), 500
