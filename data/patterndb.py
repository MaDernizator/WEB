import sqlalchemy
from sqlalchemy import orm
# noinspection PyUnresolvedReferences
from .db_session import SqlAlchemyBase

pattern_to_type = sqlalchemy.Table(
    'pattern_to_type',
    SqlAlchemyBase.metadata,
    sqlalchemy.Column('pattern', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('patterns.id')),
    sqlalchemy.Column('type', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('types.id'))
)

pattern_to_user = sqlalchemy.Table(
    'pattern_to_user',
    SqlAlchemyBase.metadata,
    sqlalchemy.Column('pattern', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('patterns.id')),
    sqlalchemy.Column('user', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('users.id'))
)


class PatternDb(SqlAlchemyBase):
    __tablename__ = 'patterns'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True, index=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True, unique=True, index=True)
    content = sqlalchemy.Column(sqlalchemy.String, nullable=True, unique=True)
    type = orm.relation("Type", secondary="pattern_to_type", backref="pattern")
    author = orm.relation("User", secondary="pattern_to_user", backref="pattern")
