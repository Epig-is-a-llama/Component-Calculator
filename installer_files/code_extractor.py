import shutil
import os
# both are imported for the shortcut copying system
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

print('\nInstallation of the base program compleate!\nThe program will now open a window which contains all the installers databases which have been uploaded to the github page as well as the devloper tools pack for making databases once you are done with installing all of the modules you wish to or if you do not wish to install any close the folder and the installation of the program will be finalised.')
