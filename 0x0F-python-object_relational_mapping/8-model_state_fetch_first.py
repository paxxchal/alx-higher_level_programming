#!/usr/bin/python3
"""
Script to print the first State object from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if correct number of arguments provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Retrieve command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Database connection URL
    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database
        )

    # Create engine
    engine = create_engine(db_url, pool_pre_ping=True)

    # Create session class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query to retrieve the first State object
    first_state = session.query(State).order_by(State.id).first()

    # Check if any state is retrieved
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # Close the session
    session.close()
