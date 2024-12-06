from database import SessionLocal
from models import Country

db = SessionLocal()
db.query(Country).delete()

db.commit()
