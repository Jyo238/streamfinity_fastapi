import os
import pytest
from sqlmodel import SQLModel
from streamfinity_fastapi.db import engine
os.environ["TESTING"] = "1"

@pytest.fixture(scope="session",autouse = True)
def creat_test_database():
    SQLModel.metadata.create_all(engine)

    yield

    SQLModel.metadata.drop_all(engine)