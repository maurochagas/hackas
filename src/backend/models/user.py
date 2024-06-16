from sqlalchemy import Table, Column, Integer, String # type: ignore
from db import metadata

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String, unique=True),
    Column("email", String, unique=True),
    Column("full_name", String),
)