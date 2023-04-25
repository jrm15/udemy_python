from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, create_engine

from sqlalchemy.orm import sessionmaker
from datetime import datetime
import psycopg2


engine = create_engine('postgresql://jrm15@localhost/pythondb')
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    #creamos los argumentos de nuestra tabla e indicamos su tipo:

    #primary key indica la clave principal de la tabla
    id = Column(Integer(), primary_key=True)
    #el numero de la clase string indica el numero de caracteres permitidos, nullable indicamos si permitimos valores nulos y unique hace unico ese valor
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    #con el modulo datetime capturamos la fecha exacta de creacion

    def __str__(self):
        return self.username


Session = sessionmaker(engine)
session = Session()




