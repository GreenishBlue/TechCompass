# Author: Cameron Brown
# Date: 16/03/2019
# Purpose: Manages the database connection.

from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


"""Manages a generic pets database."""
class TCDatabase:
    def __init__(self, engine, fresh, debug):
        self.engine = engine
        if fresh:
            print("Resetting database! Dropped all tables.")
            Base.metadata.drop_all(self.engine)
        Base.metadata.create_all(self.engine)
        Company.metadata.create_all(self.engine)
        ApprenticeshipProgramme.metadata.create_all(self.engine)
        Buddy.metadata.create_all(self.engine)
        self.sessionmaker = sessionmaker(bind=self.engine)


    """
    Purpose: Create new SQAlchemy session.
    Returns:
        - The session.
    """
    def new_session(self):
        return self.sessionmaker()


"""Manages an SQL-lite TCDatabase."""
class TCDatabaseSQLite(TCDatabase):
    def __init__(self, db_path, fresh=False, debug=False):
        print("Connecting to database (SQLite engine)")
        self.engine = create_engine("sqlite:///" + db_path)
        super().__init__(self.engine, fresh, debug)