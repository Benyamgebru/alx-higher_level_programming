#!/usr/bin/python3
""" prints the State object with the name passed as argument from the database"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysqldb://{}@localhost:3306/{}'
                            .format(sys.argv[1]. sys.argv[2]. sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind-engine)
    Session = Session()
    instance = session.query(State).fliter(State.name == (sys.argv[4].))
    try:
        print(instance[0].id)
    except IndexError:
        print("Not found")
