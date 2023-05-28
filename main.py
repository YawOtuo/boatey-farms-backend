from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import controllers, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/Records/", response_model=schemas.Record)
def create_Record(Record: schemas.RecordCreate, db: Session = Depends(get_db)):
    db_Record = controllers.get_Record_by_email(db, email=Record.email)
    if db_Record:
        raise HTTPException(status_code=400, detail="Email already registered")
    return controllers.create_Record(db=db, Record=Record)

@app.get('/')
def index():
    return "SErver running"

@app.get("/records/", response_model=list[schemas.Record])
def read_records(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    records = controllers.get_records(db, skip=skip, limit=limit)
    return records


@app.get("/Records/{Record_id}", response_model=schemas.Record)
def read_Record(Record_id: int, db: Session = Depends(get_db)):
    db_Record = controllers.get_Record(db, Record_id=Record_id)
    if db_Record is None:
        raise HTTPException(status_code=404, detail="Record not found")
    return db_Record


@app.post("/Records/{Record_id}/items/", response_model=schemas.Item)
def create_item_for_Record(
    Record_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return controllers.create_Record_item(db=db, item=item, Record_id=Record_id)


@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = controllers.get_items(db, skip=skip, limit=limit)
    return items