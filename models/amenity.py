#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    __table__ = "amenities"
    name = Column(String(128), nullable=False)
    """Place and Amenity many to many relationship """
    place_amenities = relationship("Place", secondary="place_amenity",
                                   back_populates="_amenities")
