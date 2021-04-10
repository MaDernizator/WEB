
import sqlalchemy
from sqlalchemy import orm
# noinspection PyUnresolvedReferences
from .db_session import SqlAlchemyBase

pattern_to_type = sqlalchemy.Table(
    'pattern_to_type',
    SqlAlchemyBase.metadata,
    sqlalchemy.Column('patterns', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('patterns.id')),
    sqlalchemy.Column('types', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('types.id'))
)



pattern_to_user = sqlalchemy.Table(
    'pattern_to_user',
    SqlAlchemyBase.metadata,
    sqlalchemy.Column('patterns', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('patterns.id')),
    sqlalchemy.Column('users', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('users.id'))
)


class Pattern(SqlAlchemyBase):
    __tablename__ = 'patterns'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True, index=True)
    # subject = sqlalchemy.Column(sqlalchemy.String, nullable=True)  #  если лень возится со связями
    # type = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True, unique=True, index=True)
    content = sqlalchemy.Column(sqlalchemy.String, nullable=True, unique=True)
    types = orm.relation("Types", secondary="pattern_to_type", backref="patterns")

