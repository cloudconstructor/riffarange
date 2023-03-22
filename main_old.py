import functions as fn

testfolder = "copied_audiofiles"

db =fn.db_operations(testfolder)
d = db.db_verify()
# print(d)
if d == False:
    print("db is corrupted or empty...rebuilding")
    db.db_createNew()
    
d = db.db_verify()
if d:
    # print("------------------ GET LIST -------------------")
    # files = fn.getFileList(testfolder)
    # print(files)
    # print("-------------  INSERTING FILES ----------------")
    l = db.db_insertFileList(testfolder)


    







# j.testDatainsert()
# db.readTestData()

# af = fn.audiofile()




# if __name__ == "__main__":
#     while True:
