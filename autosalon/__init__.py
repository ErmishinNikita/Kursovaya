import os

from flask import Flask
from autosalon.config import Config

app = Flask(__name__)

app.config.from_object(Config)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'f_ivt.db')))
from autosalon import routes