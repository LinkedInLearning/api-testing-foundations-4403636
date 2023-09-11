import os
from enum import Enum
from typing import List, Optional

from sqlalchemy import ForeignKey, Integer, MetaData, UniqueConstraint, create_engine
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
    sessionmaker,
)


class Base(DeclarativeBase):
    pass


class Status(Enum):
    DRAFT = "draft"
    IN_PROGRESS = "in progress"
    COMPLETE = "complete"


meta = MetaData()


class Task(Base):
    __tablename__ = "task"

    id = mapped_column(Integer, primary_key=True)

    description: Mapped[str]
    status: Mapped[Status]
    created_by: Mapped[int] = mapped_column(ForeignKey("profile.username"))


class User(Base):
    __tablename__ = "profile"
    __table_args__ = (UniqueConstraint("username"),)

    id = mapped_column(Integer, primary_key=True)

    username: Mapped[str]
    hashed_password: Mapped[str]
    email: Mapped[Optional[str]]
    full_name: Mapped[Optional[str]]
    disabled: Mapped[Optional[bool]]
    tasks: Mapped[List["Task"]] = relationship()


uri = os.getenv("DATABASE_URL")  # or other relevant config var
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
engine = create_engine(uri)

print(Base.metadata.tables.values())
meta.drop_all(engine)
# meta.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# # create user 1
# db_user = User(
#     username="user1",
#     hashed_password=create_password_hash("12345"),
#     email="user1@test.com",
#     full_name="user one",
#     disabled=False,
# )
# session.add(db_user)
session.commit()
