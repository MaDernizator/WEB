
import sqlalchemy
from sqlalchemy import orm
# noinspection PyUnresolvedReferences
from .db_session import SqlAlchemyBase


pattern_to_type = sqlalchemy.Table(
    'type_to_subject',
    SqlAlchemyBase.metadata,
    sqlalchemy.Column('types', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('types.id')),
    sqlalchemy.Column('subjects', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('subjects.id'))
)


class Type(SqlAlchemyBase):
    __tablename__ = 'types'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True, index=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True, unique=True, index=True)
    subjects = orm.relation("Subjects", secondary="type_to_subject", backref="types")

