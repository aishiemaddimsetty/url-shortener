from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, SessionLocal, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/shorten", response_model=schemas.URLInfo)
def shorten_url(payload: schemas.URLCreate, db: Session = Depends(get_db)):
    return crud.create_short_url(db, payload.original_url)

@app.get("/original/{short_code}", response_model=schemas.URLCreate)
def get_url(short_code: str, db: Session = Depends(get_db)):
    db_url = crud.get_original_url(db, short_code)
    if db_url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    return {"original_url": db_url.original_url}
