#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False)
                      )


class Amenity(BaseModel, Base):
    __table__ = "amenities"
    name = Column(String(128), nullable=False)
    """Place and Amenity many to many relationship """
    place_amenities = relationship("Place", secondary="place_amenity",
                                   back_populates="_amenities")
