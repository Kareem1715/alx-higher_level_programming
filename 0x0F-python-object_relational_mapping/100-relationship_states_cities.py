#!/usr/bin/python3
'''This script creates the State “California” with the City
“San Francisco” from the database hbtn_0e_100_usa'''
from relationship_state import State
from relationship_city import City, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    # To add the structure of table to the database
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='California')
    new_city = City(name='San Francisco')

    new_state.cities.append(new_city)

    session.add(new_state)
    session.add(new_city)

    session.commit()
    session.close()
