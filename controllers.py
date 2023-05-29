from sqlalchemy.orm import Session

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
    return db.query(models.Record).filter(models.Record.type == 'goat').offset(skip).limit(limit).all()

def getAllCattle(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Record).filter(models.Record.type == 'cattle').offset(skip).limit(limit).all()


def getOneRecord(db: Session, record_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Record).filter(models.Record.id == record_id).offset(skip).limit(limit).first()

def create_user(db: Session, user: schemas.RecordCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item