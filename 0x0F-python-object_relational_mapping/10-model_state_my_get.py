#!/usr/bin/python3
"""Script that lists all objects that contain the a letter from the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    if len(sys.argv) >= 5:
        user = sys.argv[1]
        passwd = sys.argv[2]
        dbname = sys.argv[3]
        stname = sys.argv[4]
        vchr = map(lambda ch: ch.isalpha() or (ch in (' ', '%', '_')), stname)
        if not all(vchr):
            stname = ''
        dburl = f"mysql://{user}:{passwd}@localhost:3306/{dbname}"
        dbengine = create_engine(dburl)
        Base.metadata.create_all(dbengine)
        dbsession = sessionmaker(bind=dbengine)()
        qryres = dbsession.query(State).filter(State.name == stname).first()
        if qryres is None:
            print("Not found")
        else:
            print(f"{qryres.id}")
