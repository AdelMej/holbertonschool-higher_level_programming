#!/usr/bin/python3
"""
Script for deleting all states containing the letter a
"""
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}@localhost:3306/{}".format(
            argv[1],
            argv[3]
        ),
        connect_args={'password': argv[2]}
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(State.name.like("%a%")).all()
    for state in query:
        session.delete(state)

    session.commit()

    session.close()
