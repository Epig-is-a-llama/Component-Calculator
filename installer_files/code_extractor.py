import shutil
import os
# both are imported for file manipulation
try:
    shutil.rmtree('C:/Component-Calculator')
except Exception as e:
    pass
# old contents of the program folder are cleared which the user is warned of before the installation takes place
from zipfile import ZipFile
#create a zipfile object and load zip in it
with ZipFile('files.zip', 'r') as zipObj:
    zip.printdir()
    #extract all the contents of zip file into the specified directory
    zipObj.extractall(path = 'C:/')
    zipObj.close()

shutil.copy('launch.cmd' , 'C:/Component-Calculator/launch.cmd')
