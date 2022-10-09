from sqlalchemy import Column, String, Integer, Float
from .database import Base


class Emp(Base):
    __tablename__ = "EMP"

    EMPLOYEE_NUMBER = Column(Integer, primary_key=True, index=True)
    EMPLOYEE_NAME = Column(String)
    ORGANISATION = Column(String)
    LOCATION = Column(String(15), index=True)
    SALARY = Column(Float)
