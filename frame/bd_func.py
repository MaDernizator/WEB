from data import db_session
from data.subject import Subject
from data.type import Type
from data.patterndb import PatternDb


def get_subjects():
    db_session.global_init("../db/blogs.db")
    db_sess = db_session.create_session()
    subjects = db_sess.query(Subject).all()
    return [[subject.id, subject.name] for subject in subjects]


def get_types(subjects=None) -> list:
    db_session.global_init("../db/blogs.db")
    db_sess = db_session.create_session()
    types = db_sess.query(Type).all()
    res = []
    for type in types:
        if subjects:
            correct = False
            for subject in type.subject:
                if subject.id in subjects:
                    correct = True
            if not correct:
                continue
        res.append([type.id, type.name])
    return res


def get_patterns(types=None) -> list:
    db_session.global_init("../db/blogs.db")
    db_sess = db_session.create_session()
    patterns = db_sess.query(PatternDb).all()
    res = []
    for pattern in patterns:
        if types:
            correct = False
            for type in pattern.type:
                if type.id in types:
                    correct = True
            if not correct:
                continue
        res.append([pattern.id, pattern.content])
    return res
