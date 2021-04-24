import sqlalchemy
# noinspection PyUnresolvedReferences
from .db_session import SqlAlchemyBase


class Subject(SqlAlchemyBase):
    __tablename__ = 'subjects'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True, index=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True, unique=True, index=True)
