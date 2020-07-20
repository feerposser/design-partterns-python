import sqlite3


class MetaclassSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        print("Metaclass Singleton", args)
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaclassSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=MetaclassSingleton):
    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursor_obj = self.connection.cursor()
        return self.cursor_obj


db1 = Database()
db2 = Database()

print("db1: ", db1)
print("db2: ", db2)
