from models import Country
from datetime import datetime
from database import SessionLocal

import pandas as pd



db = SessionLocal()

q = db.query(Country).all()
print(q[0].capital)