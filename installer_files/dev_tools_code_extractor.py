import os
# imported for the folder creation system
try:
    if not os.path.exists('C:/Component-Calculator/dev_tools'):
        # if the folder doesn't already exist it is created
        os.makedirs('C:/Component-Calculator/dev_tools')
except OSError:
    pass
from zipfile import ZipFile
#create a zipfile object and load zip in it
with ZipFile('Dev-Tools-Module-Installer.zip', 'r') as zipObj:
    #extract all the contents of zip file into specified directory
    zipObj.extractall(path = 'C:/Component-Calculator/dev_tools/')
    zipObj.close()
