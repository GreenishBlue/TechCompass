import os
from flask import Flask, render_template, request

from db import TCDatabaseSQLite
from models import *


DB_FILENAME = "tc.db"
DB_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), DB_FILENAME)


db = TCDatabaseSQLite(DB_PATH)


app = Flask(__name__)


@app.route('/')
def results():
    session = db.new_session()
    results = session.query(Buddy)
    query = request.args.get('q')
    if query:
        results.filter(Buddy.description.like("%" + query + "%"))
    return render_template('index.html', results=results)


if __name__ == '__main__':
    app.run(debug=True, port=8081)