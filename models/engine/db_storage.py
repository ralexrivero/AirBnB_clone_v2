#!/usr/bin/python3
"""This module defines a class to manage data base storage for hbnb clone"""
from sqlalchemy import create_engine, MetaData
from os import environ as env
from sqlalchemy.orm import sessionmaker, scoped_session

class DBStorage:
    """This class manages storage of hbnb models on a SQL DB"""
    __engine = None
    __session = None
    def __init__(self):
        """ init """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            env["HBNB_MYSQL_USER"],
            env["HBNB_MYSQL_HOST"],
            env["HBNB_MYSQL_DB"]
            env["HBNB_MYSQL_PWD"],
        ), pool_pre_ping=True)
        if env["HBNB_ENV"] == "test":
            meta = MetaData(self.__engine)
            meta.reflect()
            meta.drop_all()
    
    def all(self, cls=None):
        """ all """
        if cls is None:
            from models.base_model import BaseModel
            from models.user import User
            from models.place import Place
            from models.state import State
            from models.city import City
            from models.amenity import Amenity
            from models.review import Review
            quer = self.__session.query(
                BaseModel,
                User,
                Place,
                State,
                City,
                Amenity,
                Review
            ).all()
        else:
            quer = self.__session.query().all()
        out = {}
        for obj in quer:
            key = "{}.{}".format(obj.__class__.__name__, object.id)
            out[key] = obj
        return out

    def new(self, obj):
        """ new """
        self.__session.add(obj)
    
    def save(self):
        """ save """
        self.__session.commit()
    
    def delete(self, obj=None):
        """ delete """
        if obj is not None:
            self.__session.delete(obj)
    
    def reload(self):
        """ reload """
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(expire_on_commit=False, bind=self.__engine))
        self.__session = Session()

