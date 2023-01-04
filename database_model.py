from sqlalchemy import Column, Integer, String, Table, MetaData

meta = MetaData()

Users = Table(
    "users",
    meta,
    Column("id", Integer, primary_key=True),
    Column("username", String),
    Column("hashedPass", String)
)