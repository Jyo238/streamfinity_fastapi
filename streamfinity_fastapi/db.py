from sqlalchemy import create_engine
from typing import Any, Generator

from sqlmodel import Session
engine = create_engine('sqlite:///data/database.db',echo=True,connect_args={"check_same_thread":False})

def get_session()->Generator[Session,Any,None]:
    with Session(engine) as session:
        yield session