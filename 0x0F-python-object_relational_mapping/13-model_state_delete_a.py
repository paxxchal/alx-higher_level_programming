#!/usr/bin/python3
"""
Script to delete all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
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
    db_url = f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'

    # Create engine
    engine = create_engine(db_url, pool_pre_ping=True)

    # Create session class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query to retrieve all State objects with a name containing the letter 'a'
    states_with_a = session.query(State).filter(State.name.like('%a%')).all()

    # Delete the retrieved State objects
    for state in states_with_a:
        session.delete(state)

    # Commit the session to the database
    session.commit()

    # Close the session
    session.close()
