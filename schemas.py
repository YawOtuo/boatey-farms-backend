
from pydantic import BaseModel
from datetime import date


class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class RecordBase(BaseModel):
    name: str | None = None
    sire: int | None = None
    dam: int | None = None
    type: str | None = None
    gender: str | None = None
    tag_colour: str | None = None
    date_of_birth: date | None = None
    date_purchased: date | None = None
    weight: int | None = None
    number_of_kids: int | None = None
    colour: str | None = None
    castrated: bool | None = None
    alive: bool | None = None
    sold: bool | None = None
    health_condition: str | None = None
    vaccination_info: str | None = None
    remarks: str | None = None

    class Config:
        orm_mode = True

class Record(RecordBase):
    id: int | None = None

class RecordCreate(RecordBase):
    name: str 

class RecordUpdate(RecordBase):
    id : int 

class SearchRequest(BaseModel):
    query: str
