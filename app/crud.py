from sqlalchemy.orm import Session
from . import models, schemas, utils

def create_short_url(db: Session, original_url: str):
    short_code = utils.generate_short_code()
    db_url = models.URL(original_url=original_url, short_code=short_code)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

def get_original_url(db: Session, short_code: str):
    return db.query(models.URL).filter(models.URL.short_code == short_code).first()
