from random import choice
from time import time
import numpy
import math
from data import db_session
from data.patterndb import PatternDb

class Pattern:
    def __init__(self, id, count):
        self.id, self.count = id, count

    def get_count(self):
        return self.count

    def get_pattern(self):
        db_session.global_init("db/blogs.db")
        db_sess = db_session.create_session()
        pattern = db_sess.query(PatternDb).filter(PatternDb.id == self.id).first()
        return pattern.content





class TaskGenerator:
    def __init__(self, pattern, test_mode=False):
        self.test_mode = test_mode
        self.pattern = pattern
        self.text = None
        self.generate()

    def get_text(self):
        return self.text if self.text else False

    def write(self):
        self.text = (eval(f'f\"{self.pattern.split(";")[0]}\"'), answer)

    def check(self):
        for i in self.pattern.split(";")[3:]:
            try:
                if not eval(i.strip()):
                    return False
            except ZeroDivisionError:
                return False
        return True

    def generate(self):
        global answer
        flag = False
        start_time = time()
        error = False
        while not flag:
            if time() - start_time > (5 if not self.test_mode else 2):
                error = True
                break
            for _i, symbol_num in enumerate([i for i, a in enumerate(self.pattern) if a == '{']):
                _s = self.pattern[symbol_num + 1:][:self.pattern[symbol_num + 1:].index('}')]
                exec(f'{_s} = choice({self.pattern.split(";")[1].split("  ")[_i].strip()})',
                     locals(), globals())
            try:
                answer = eval(self.pattern.split(";")[2].strip())
                answer = int(answer) if int(answer) == answer else answer
            except ZeroDivisionError:
                continue
            flag = self.check()
        if not error:
            self.write()

    def __call__(self):
        return self.get_text()
