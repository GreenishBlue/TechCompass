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

    q = session.query(Company).all()
    companies = []
    for company in q:
        companies.append(company.company_name)

    company_query = request.args.get('company')
    if not company_query:
        results = (session.query(Buddy, ApprenticeshipProgramme, Company)
              .filter(Buddy.apprenticeship == ApprenticeshipProgramme.id)
              .filter(ApprenticeshipProgramme.company == Company.id)
              .all())
    else:
        results = (session.query(Buddy, ApprenticeshipProgramme, Company)
              .filter(Buddy.apprenticeship == ApprenticeshipProgramme.id)
              .filter(ApprenticeshipProgramme.company == Company.id)
              .filter(Company.company_name.like("%" + company_query + "%"))
              .all())

    return render_template('index.html', results=results, company=company_query, 
        companies=companies)


if __name__ == '__main__':
    app.run(debug=True, port=8081)