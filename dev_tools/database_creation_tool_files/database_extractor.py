from zipfile import ZipFile
#create a zipfile object and load zip in it
with ZipFile('database.zip', 'r') as zipObj:
    #extract all the contents of zip file into current directory
    zipObj.extractall(path = 'C:/Component-Calculator/databases/')
    zipObj.close()
print('\nDone!\n')
