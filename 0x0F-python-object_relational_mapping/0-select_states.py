#!/usr/bin/python3
"""
Script to list all states from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Check if correct number of arguments provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Retrieve command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
        )

    # Create a cursor object
    cursor = db.cursor()

    # Execute SQL query to select all states and fetch results
    cursor.execute("SELECT * FROM states ORDER BY id")

    # Fetch all rows
    results = cursor.fetchall()

    # Print results
    for row in results:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
