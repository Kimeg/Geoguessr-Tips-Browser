from fastapi import APIRouter

from database import SessionLocal
from domain import data_schema
from models import Country

router = APIRouter(
    prefix="/api/data",
)


@router.get("/", response_model=data_schema.DataList)
def get_all_data():
    db = SessionLocal()
    _data = db.query(Country)
    _data = _data.order_by(Country.create_date).all()
    db.close()
    return {"data_list": _data}


@router.get("/{country}", response_model=data_schema.Country)
def get_country_data(country: str):
    db = SessionLocal()
    _data = db.query(Country)
    _data = _data.order_by(Country.create_date).filter(Country.name == country).all()[0]
    db.close()
    return _data


@router.get("/{country}/{field}", response_model=data_schema.Field)
def get_field_data(country: str, field: str):
    db = SessionLocal()
    _data = db.query(Country)
    _data = (
        _data.order_by(Country.create_date.desc())
        .filter(Country.name == country)
        .all()[0]
    )

    _field = _data.__dict__[field].split(",")

    db.close()
    return {"field": _field}
