from sqlalchemy import Column, Integer, String
from geoalchemy2 import Geometry
from database import Base

# Define To Do class inheriting from Base
# class Attractions(Base):
#     __tablename__ = 'attractions'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(1024))
#     type = Column(String(256))
#     region = Column(String(256))
#     locality = Column(String(256))
#     geolocation = Column(Geometry('POINT'))