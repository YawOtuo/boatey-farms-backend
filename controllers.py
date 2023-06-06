from sqlalchemy.orm import Session
from fastapi import HTTPException


import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_records(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Record).offset(skip).limit(limit).all()

def getAllSheep(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Record).filter(models.Record.type == 'sheep').offset(skip).limit(limit).all()

def getAllGoats(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Record).filter(models.Record.type == 'goats').offset(skip).limit(limit).all()

def getAllCattle(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Record).filter(models.Record.type == 'cattle').offset(skip).limit(limit).all()

def getOneRecord(db: Session, record_id: int, skip: int = 0, limit: int = 100):
    record =  db.query(models.Record).filter(models.Record.id == record_id).offset(skip).limit(limit).first()
    # print(record.sire)
    # print(record.dam_children.id)
    # print(record.s_parent)
    return record
def createRecord(db: Session, record: schemas.RecordCreate):
    # fake_hashed_password = user.password + "notreallyhashed"
    db_record = models.Record(
        name = record.name,
        type = record.type,
        tag_colour = record.tag_colour,
        number_of_kids = record.number_of_kids,
        colour = record.colour,
        castrated = record.castrated,
        health_condition = record.health_condition,
        remarks = record.remarks
                )
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return "SUCCESSFULLY CREATED RECORD OF " + record.name

def updateRecord(db: Session, record_id : int, record: schemas.RecordUpdate):

    dbRecord = db.query(models.Record).get(record_id)
    if dbRecord:
        # Update the record with the new values
        update_data = {k: v for k, v in record.dict().items() if v is not None}
        print(update_data)
        db.query(models.Record).filter(models.Record.id == record_id).update(update_data)
        db.commit()
        db.refresh(dbRecord)
        return {"message": f"Item {record_id} has been updated"}
    else:
        return {"message": f"Item {record_id} not found"}

def getNumberOfCattle(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Record).filter(models.Record.type == 'cattle').count()

def getNumberOfGoats(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Record).filter(models.Record.type == 'goats').count()

def getNumberOfSheep(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Record).filter(models.Record.type == 'sheep').count()

def searchforRecord(db: Session, record_type: str, query: str ,skip: int = 0, limit: int = 100):
    print(query)
    
    if record_type == 'any':
        result =  db.query(models.Record).filter(
        models.Record.name.ilike(f"%{query}%")).all()
    else: 
        result =  db.query(models.Record).filter(
        models.Record.name.ilike(f"%{query}%") &  models.Record.type.ilike(f"%{record_type}%") ).all()
   
    if result: 
        print(result)
        return result
    else:
        raise HTTPException(status_code=404, detail="No result found")



def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


