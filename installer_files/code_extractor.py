import shutil
import os
# both are imported for the shortcut copying system
from zipfile import ZipFile
#create a zipfile object and load zip in it
with ZipFile('files.zip', 'r') as zipObj:
    zip.printdir()
    #extract all the contents of zip file into the specified directory
    zipObj.extractall(path = 'C:/')
    zipObj.close()

print('Would you like to create a desktop shortcut for the program? (Please answer in the form Y/N)')
shortcut_ans = input('Please answer here: ')
if shortcut_ans == 'Y':
    original = r'C:/Component-Calculator/Component-Calultator.EXE'
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    target = desktop
    # creates a copy of the shortcut for the .EXE verion of the launch.bat
    shutil.copyfile(original, target)

print('\nInstallation compleate!\nPlease remember the base version of the program comes with no databases installed to get them you must either create your own or download them from the Github page where this program came from (https://github.com/Epig-is-a-llama/Component-Calculator).')
