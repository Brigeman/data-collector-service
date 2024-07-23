from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URI = 'postgresql+psycopg2://your_db_user:your_db_password@localhost/real_estate_db' # TODO change example 
Base = declarative_base()

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()


class RealEstateListing(Base):
    __tablename__ = 'listings'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(String)
    location = Column(String)
    link = Column(String)

Base.metadata.create_all(engine)