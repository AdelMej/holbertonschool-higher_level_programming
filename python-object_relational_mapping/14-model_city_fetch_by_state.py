#!/usr/bin/python3
"""
Script that fetch all cities and their states
"""
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1],
            argv[2],
            argv[3]
        )
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(City).order_by(City.id.asc()).all()
    for city in query:
        print(f"{city.state.name}: ({city.id}) {city.name}")

    session.close()
