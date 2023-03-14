import sqlite3 as sl
import os
import fnmatch

class db_operations:
    def __init__(self, folder):
        self.dbpathname = "db/riffarange.db" 
        self.db = sl.connect(self.dbpathname)
        self.tablenames = "audiofiles", "songs", "folders", "binder"
        self.folder = folder

    def db_verify(self):
        for tablename in self.tablenames:
            with self.db:
                s = self.db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='"+tablename+"'").fetchall()
                if s == []:
                    verify = False
                else:
                    verify = True
        return(verify)

    def db_createNew(self):
        with self.db:
            self.db.execute("""
                CREATE TABLE audiofiles (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    filename TEXT,
                    path TEXT,
                    name TEXT,
                    description TEXT,
                    tuning TEXT,
                    lock INTEGER,
                    hide INTEGER
                );
            """)

            self.db.execute("""
                CREATE TABLE songs (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    description TEXT,
                    tuning TEXT,
                    lock INTEGER,
                    hide INTEGER
                );
            """)

            self.db.execute("""
                CREATE TABLE folders (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    path TEXT,
                    name TEXT,
                    description TEXT,
                    hide INTEGER
                );
            """)

            self.db.execute("""
                CREATE TABLE binder (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    song_id INTEGER NOT NULL,
                    audiofile_id INTEGER NOT NULL,
                    position INT,
                    tuning TEXT,
                    lock INTEGER,
                    hide INTEGER
                );
            """)

    def db_insertFileList(self, folder):
        filenames = []
        filedata = []
        for file in os.listdir(self.folder):
            if fnmatch.fnmatch(file, '*.wav') or fnmatch.fnmatch(file, '*.mp3') or fnmatch.fnmatch(file, '*.ogg'):
                filenames.append(file)

        if len(filenames) == 0:
            print("No files found in '"+folder+"'")
        else:
            sql = 'INSERT INTO AUDIOFILES (filename, path, lock, hide) values(?, ?, ?, ?)'
            for filename in filenames:
                e = self.db_checkFilenameExists(self.folder, filename)
                if e == 0:
                    filedata.append([filename, folder, 0, 0])
            with self.db:
                self.db.executemany(sql, filedata)

    def db_checkFilenameExists(self, folder, filename):
        with self.db:
            s = self.db.execute("SELECT count(*) AS j FROM AUDIOFILES WHERE filename='"+filename+"' AND path='"+folder+"'").fetchall()
            return(s[0][0])



                
                

def getFileList(folder):
    filez = []
    for file in os.listdir(folder):
        if fnmatch.fnmatch(file, '*.wav') or fnmatch.fnmatch(file, '*.mp3') or fnmatch.fnmatch(file, '*.ogg'):
            filez.append(file)

    if len(filez) == 0:
        print("No files found in '"+folder+"'")
    return(filez)






# class audiofile():
#     def __init__(self, id, filename, name, description, tuning, lock, hide):
#         self.id = id
#         self.filname = filename
#         self.name = name
#         self.description = description
#         self.tuning = tuning
#         self.lock = lock
#         self.hide = hide
        
