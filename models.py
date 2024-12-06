from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Country(Base):
    __tablename__ = "country"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    continent = Column(String, nullable=False)
    capital = Column(String, nullable=True)
    domain = Column(String, nullable=True)
    language = Column(String, nullable=False)
    currency = Column(String, nullable=True)
    driving_side = Column(String, nullable=True)
    license_plate = Column(String, nullable=True)
    bollard = Column(String, nullable=True)
    chevron = Column(String, nullable=True)
    utility_pole = Column(String, nullable=True)
    curb = Column(String, nullable=True)
    guardrail = Column(String, nullable=True)
    lanes = Column(String, nullable=True)
    stop_sign = Column(String, nullable=True)
    pedestrian_sign = Column(String, nullable=True)
    direction_sign = Column(String, nullable=True)
    road_number = Column(String, nullable=True)
    road_sign = Column(String, nullable=True)
    sign_traffic_post = Column(String, nullable=True)
    architecture = Column(String, nullable=True)
    landscape = Column(String, nullable=True)
    google_car = Column(String, nullable=True)
    follow_car = Column(String, nullable=True)
    street = Column(String, nullable=True)
    rift = Column(String, nullable=True)
    camera_gen = Column(String, nullable=True)
    miscellaneous = Column(String, nullable=True)
    create_date = Column(DateTime, nullable=False)
