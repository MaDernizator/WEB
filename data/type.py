import sqlalchemy
from sqlalchemy import orm
# noinspection PyUnresolvedReferences
from .db_session import SqlAlchemyBase

type_to_subject = sqlalchemy.Table(
    'type_to_subject',
    SqlAlchemyBase.metadata,
    sqlalchemy.Column('type', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('types.id')),
    sqlalchemy.Column('subject', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('subjects.id'))
)


class Type(SqlAlchemyBase):
    __tablename__ = 'types'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True, index=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True, unique=True, index=True)
    subject = orm.relation("Subject", secondary="type_to_subject", backref="type")
