from pydantic import BaseModel, HttpUrl

class URLCreate(BaseModel):
    original_url: HttpUrl

class URLInfo(BaseModel):
    original_url: HttpUrl
    short_code: str

    class Config:
        orm_mode = True
