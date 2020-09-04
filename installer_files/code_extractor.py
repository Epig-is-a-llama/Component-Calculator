import shutil
import os
# both are imported for file manipulation

from zipfile import ZipFile
# imported for the unziping funcionality

def unzip(zip_file , location_to_unzip_to):
    with ZipFile(zip_file, 'r') as zipObj:
        # create a zipfile object and load the zip into it
        zipObj.extractall(path = location_to_unzip_to)
        # extract all the contents of zip file into the specified directory
        zipObj.close()

def create_folder(directory):
    try:
        if not os.path.exists(directory):
            # checks if the folder already exists if it does not it creates it
            os.makedirs(directory)
    except OSError:
        pass

try:
    shutil.rmtree('C:/Component-Calculator')
except Exception as e:
    pass
# old contents of the program folder are cleared which the user is warned of before the installation takes place
create_folder('C:/Component-Calculator')
# creates the folder to install to

create_folder('C:/Component-Calculator/Module-Installers')
# creates the folder for the module installers to be unziped into
unzip('Addon-Installers.zip' , 'C:/Component-Calculator/Module-Installers')
# unzips the module installers zip file into the correct location

create_folder('C:/Component-Calculator/other-dependencys')
# creates the folder for the other dependencys to be unziped to
unzip('Other-Files.zip' , 'C:/Component-Calculator/other-dependencys')
# unzips the other dependencys into the correct folder

shutil.copy('launch.cmd' , 'C:/Component-Calculator/launch.cmd')
# creates a copy of the launch file in the base directory of the program
