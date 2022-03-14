from numpy import genfromtxt, arange
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, REAL
from geoalchemy2 import Geometry
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
      print(data)
    # for i in range(len(data)):
    #     data[i] = data[i].split(";")
    return data

class Attractions(Base):
    __tablename__ = 'attractions'
    # id = Column(Integer, primary_key=True)
    name = Column(String(1024), primary_key=True)
    type = Column(String(256))
    region = Column(String(256))
    locality = Column(String(256))
    #geo1 = Column(REAL)
    #geo2 = Column(REAL)
    geolocation = Geometry('point')

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
    
    print("ok")

    data = Load_Data(file_name) 

    print("ok")

    for i in data:
        print(i)
        record = Attractions(**{
            'name' : i[0],
            'type' : i[1],
            'region' : i[2],
            'locality' : i[3],
            'geolocation' : i[4]
            #'geo1': i[5],
            #'geo2': i[6]
        })
        s.add(record) #Add all the records

    s.commit() #Attempt to commit all the records
    # except Exception:
    #     print("Error while prepopulating db")
    #     s.rollback() #Rollback the changes on error
    # finally:
    #     s.close() #Close the connection