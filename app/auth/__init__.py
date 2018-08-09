from flask import Flask
from flask import Blueprint

bp = Blueprint('auth', __name__)

from app.auth import routes
####Michael: don't really need to import email or forms, the main thing this whole bp thing affects is the routing stuff

####Michael: note need to make sure add all the auth/ in front of the template files and change ALL url_for to url_for('auth.xxx')