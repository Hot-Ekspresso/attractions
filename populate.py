from numpy import genfromtxt, arange
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, REAL
from database import Base
import csv


def Load_Data(file_name):
    #data = genfromtxt(file_name, delimiter=';', skip_header=1, converters={0: lambda s: str(s)}, usecols=arange(0,5))
    # data = genfromtxt(file_name, delimiter=';', skip_header=1, invalid_raise = False)
    # print("load_data")
    # return data.tolist()
    with open(file_name, newline='') as f:
      reader = csv.reader(f, delimiter =';')
      data = list(reader)
    return data[1:]

class Attractions(Base):
    __tablename__ = 'attractions'
    id = Column(Integer, primary_key=True)
    name = Column(String(1024))
    type = Column(String(256))
    region = Column(String(256))
    locality = Column(String(256))
    geolocation = Column(String(256))

if __name__ == "__main__":
    #Create the database
    engine = create_engine('sqlite:///csv_test.db')
    Base.metadata.create_all(engine)

    #Create the session
    session = sessionmaker()
    session.configure(bind=engine)
    s = session()

    #try:
    file_name = "tourist_attractions.csv" #sample CSV file used:  http://www.google.com/finance/historical?q=NYSE%3AT&ei=W4ikVam8LYWjmAGjhoHACw&output=csv

    data = Load_Data(file_name) 

    for index, value in enumerate(data):
        
        geo = value[4].replace('Decimal', '').replace('\'','')
        geo = geo.replace('(','').replace(')','')
        geo = '('+geo+')'

        record = Attractions(**{
            'id' : index, 
            'name' : value[0],
            'type' : value[1],
            'region' : value[2],
            'locality' : value[3],
            'geolocation' : geo
        })
        s.add(record) #Add all the records

    s.commit() #Attempt to commit all the records
    # except Exception:
    #     print("Error while prepopulating db")
    #     s.rollback() #Rollback the changes on error
    # finally:
    #     s.close() #Close the connection