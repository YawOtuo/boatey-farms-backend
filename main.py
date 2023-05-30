from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware


import controllers, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to specific origins if needed
    allow_credentials=True,
    allow_methods=["*"],  # You can restrict this to specific HTTP methods
    allow_headers=["*"],  # You can restrict this to specific headers
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/records/")
def createRecord(record: schemas.RecordCreate, db: Session = Depends(get_db)):
    dbRecord = controllers.createRecord(db, record=record)
    if dbRecord:
        return dbRecord


@app.post("/records/{record_id}")
def updateRecord(record_id: int,
                 record: schemas.RecordBase, db: Session = Depends(get_db)):
    dbRecord = controllers.updateRecord(db, record_id=record_id, record=record)
    if dbRecord:
        return dbRecord

@app.get('/')
def index():
    return "SErver running"

@app.get("/records/", response_model=list[schemas.Record])
def read_records(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    records = controllers.get_records(db, skip=skip, limit=limit)
    return records

@app.get("/records/sheep", response_model=list[schemas.Record])
def getAllSheep(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    records = controllers.getAllSheep(db, skip=skip, limit=limit)
    return records

@app.get("/records/goats", response_model=list[schemas.Record])
def getAllGoats(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    records = controllers.getAllGoats(db, skip=skip, limit=limit)
    return records

@app.get("/records/cattle", response_model=list[schemas.Record])
def getAllCattle(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    records = controllers.getAllCattle(db, skip=skip, limit=limit)
    return records



@app.get("/records/{record_id}", response_model=schemas.Record)
def read_Record(record_id: int, db: Session = Depends(get_db)):
    dbRecord = controllers.getOneRecord(db, record_id=record_id)
    if dbRecord is None:
        raise HTTPException(status_code=404, detail="Record not found")
    return dbRecord


# @app.post("/Records/{Record_id}/items/", response_model=schemas.Item)
# def create_item_for_Record(
#     Record_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return controllers.create_Record_item(db=db, item=item, Record_id=Record_id)


# @app.get("/items/", response_model=list[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = controllers.get_items(db, skip=skip, limit=limit)
#     return items