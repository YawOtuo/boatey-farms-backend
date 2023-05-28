
from pydantic import BaseModel


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
    id: int


class RecordCreate(RecordBase):
    password: str


class Record(RecordBase):
    name: str | None = None
    type: str | None = None
    tag_colour: str | None = None
    number_of_kids: int | None = None
    colour: str | None = None
    castrated: bool | None = None
    health_condition: str | None = None
    remarks: str | None = None

    class Config:
        orm_mode = True