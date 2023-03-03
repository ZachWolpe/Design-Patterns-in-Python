

import unittest

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    

class Database(metaclass=Singleton):
    # Load data to memory
    def __init__(self) -> None:
        self.data = {
            'omega':    112,
            'gamma':    554,
            'theta':    232
        }


class SingletonQuery:
    def total_values(self, keys):
        res = 0
        for k in keys:
            res += Database().data[k]
        return res
    

class SingletonQuery2:
    def __init__(self, db) -> None:
        self.db = db
    
    def total_values(self, keys):
        res = 0
        for k in keys:
            res += self.db.data[k]
        return res


class SingletonTest(unittest.TestCase):
    def test_is_singleton(self):
        db  = Database()
        db2 = Database()
        self.assertEqual(db, db2)

    def test_singleton_properties(self):
        db = Database()
        sq1 = SingletonQuery()
        sq2 = SingletonQuery2(db)
        self.assertEqual(
            sq1.total_values(['omega','gamma','theta']),
            sq2.total_values(['omega','gamma','theta'])
        )


if __name__ == '__main__':
    unittest.main()