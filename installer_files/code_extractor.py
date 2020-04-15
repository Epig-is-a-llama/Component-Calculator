from zipfile import ZipFile
#create a zipfile object and load zip in it
with ZipFile('game_files.zip', 'r') as zipObj:
    zip.printdir()
    #extract all the contents of zip file into current directory
    zipObj.extractall(path = 'c:\')
    zipObj.close()
print('\nDone!\n')
