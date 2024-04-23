#!/usr/bin/python3
"""
Script to print all City objects from the database hbtn_0e_14_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

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

    # Query to retrieve all City objects and their corresponding State objects
    cities = session.query(City, State).join(State).order_by(City.id).all()

    # Print results
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()
