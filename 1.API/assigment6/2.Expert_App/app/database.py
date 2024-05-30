from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
import os
import urllib


SQLALCHEMY_DATABASE_URL = "postgresql://sa:123@localhost:5432/class"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

#connection_string = "DRIVER={ODBC Driver 17 for SQL Server};TrustServerCertificate=yes;Database=class;SERVER=.;UID=sa;PWD=GHH1400@"
#connection_string = urllib.parse.quote_plus(connection_string) 
#connection_string = "mssql+pyodbc:///?odbc_connect=%s" % connection_string



#engine = create_engine(connection_string)
#con=engine.connect()


#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Base = declarative_base()