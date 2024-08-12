from decouple import config # connects to the .env file
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URL = config('DB_URL')

engine = create_engine(DB_URL, pool_pre_ping=True) # pool_pre_ping=True: this argument checks if the database is connected sucessful before doing anything. If it's not, it returns an error.
session = sessionmaker() 
