import os
from flask import Flask, render_template

from db import TCDatabaseSQLite
from models import *


DB_FILENAME = "tc.db"
DB_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), DB_FILENAME)


db = TCDatabaseSQLite(DB_PATH)


app = Flask(__name__)


results = [
    {
        "buddy_id": 5454,
        "buddy_name": "Cameron Brown",
        "buddy_description": "Hey! I work on the ML Kit team.",
        "photo_url": "https://picsum.photos/330/200",
        "programme_id": 5454,
        "programme_title": "Software Engineering Apprenticeship",
        "programme_description": "Work on a team of Googlers as you study in your 20% time",
        "role": "Apprentice SWE",
        "comany_id": 5435,
        "company_name": "Google",
        "location": "London, UK",
    },
]


@app.route('/')
def home_page():
    return render_template('index.html', results=results)


if __name__ == '__main__':
    app.run(debug=True, port=8081)