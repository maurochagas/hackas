from sqlalchemy import create_engine, MetaData # type: ignore
from databases import Database # type: ignore

DATABASE_URL = "sqlite:///./database/relational/database.db"

database = Database(DATABASE_URL)
metadata = MetaData()

engine = create_engine(DATABASE_URL)