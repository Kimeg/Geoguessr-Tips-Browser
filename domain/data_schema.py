from pydantic import BaseModel, field_validator


class Country(BaseModel):
    id: int
    name: str
    continent: str
    capital: str | None
    domain: str | None
    currency: str | None
    language: str | None
    driving_side: str | None
    license_plate: str | None
    bollard: str | None
    chevron: str | None
    utility_pole: str | None
    curb: str | None
    guardrail: str | None
    lanes: str | None
    stop_sign: str | None
    pedestrian_sign: str | None
    direction_sign: str | None
    road_number: str | None
    road_sign: str | None
    sign_traffic_post: str | None
    architecture: str | None
    landscape: str | None
    google_car: str | None
    follow_car: str | None
    street: str | None
    rift: str | None
    camera_gen: str | None
    miscellaneous: str | None


class DataList(BaseModel):
    data_list: list[Country] = []


class Field(BaseModel):
    field: list[str] = []
