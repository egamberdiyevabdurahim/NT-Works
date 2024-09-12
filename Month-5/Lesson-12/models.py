import sqlalchemy
from sqlalchemy import Column, Integer, String, Boolean

from database import metadata


users = sqlalchemy.Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("full_name", String),
    Column("age", Integer)
)


to_do = sqlalchemy.Table(
    "to_do",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("task", String),
    Column("is_completed", Boolean, default=False),
    Column("number", Integer)
)
