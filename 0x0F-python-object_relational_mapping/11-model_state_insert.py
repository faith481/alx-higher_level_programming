#!/usr/bin/python3
"""Script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    if len(sys.argv) >= 4:
        user = sys.argv[1]
        passwd = sys.argv[2]
        dbname = sys.argv[3]
        dburl = f"mysql://{user}:{passwd}@localhost:3306/{dbname}"
        dbengine = create_engine(dburl)
        Base.metadata.create_all(dbengine)
        dbsession = sessionmaker(bind=dbengine)()
        newst = State(name='Louisiana')
        dbsession.add(newst)
        try:
            dbsession.flush()
            dbsession.refresh(newst)
            if newst.id is not None:
                print(f"{newst.id}")
        except Exception:
            dbsession.rollback()
        finally:
            dbsession.commit()
