from typing import Optional
from datetime import datetime

from sqlmodel import Field, SQLModel, create_engine


class ScrapingSession(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    date: datetime 
    status: str
    items_scraped: int
    name: str
    error_name: Optional[str] = None


db_path = "bd_play/statistics.db"
engine = create_engine(f"sqlite:///{db_path}", echo=True)
SQLModel.metadata.create_all(engine)