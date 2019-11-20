import os
from flask import Flask, render_template

from db import TCDatabaseSQLite
from models import *


DB_FILENAME = "tc.db"
DB_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), DB_FILENAME)


db = TCDatabaseSQLite(DB_PATH)


app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=8081)