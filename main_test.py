import sqlite3 as sl
import os


class dbOperations:
    def __init__(self):
        self.dbpathname = "db/riffarange.db" 
        self.db = sl.connect(self.dbpathname)

    def checkDb(self):
        dbfile = os.path.isfile(self.dbpathname)
        if dbfile:
            print('check db: database exists...skipping')
        else:
            print('check db: database not found, creating')
            self.createNewDb()

    
    def createNewDb(self):
        with self.db:
            self.db.execute("""
                CREATE TABLE USER (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    age INTEGER
                );
            """)
        
    def testDatainsert(self):
        sql = 'INSERT INTO USER (id, name, age) values(?, ?, ?)'
        data = [
            (1, 'Alice', 21),
            (2, 'Bob', 22),
            (3, 'Chris', 23)
        ]
        with self.db:
            self.db.executemany(sql, data)


    def readTestData(self):
        with self.db:
            data = self.db.execute("SELECT * FROM USER")
            for row in data:
                print(row)

    # def editData(self):





j =dbOperations()
j.checkDb()
# j.testDatainsert()
j.readTestData()



# if __name__ == "__main__":
#     while True:
