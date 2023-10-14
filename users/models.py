import datetime
from db.database import Base
from sqlalchemy import Column, Integer, String, DateTime


class DbUser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    wallet_id = Column(String)
    name = Column(String)
    last_name = Column(String)
    sex_type = Column(String)
    dni = Column(String)
    birth_date = Column(DateTime)
    created_at = Column(DateTime, default=datetime.datetime.now())
