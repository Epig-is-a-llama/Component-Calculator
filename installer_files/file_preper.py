import os
import shutil
# both imported for file and folder manipulation

def create_folder(directory):
    try:
        if not os.path.exists(directory):
            # checks if the folder already exists if it does not it creates it
            os.makedirs(directory)
    except OSError:
        pass

def create_version_folder(version_num):
    base_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    create_folder(base_directory+'/installers/'+version_num)
    # creates the version folder
    create_folder(base_directory+'/installers/'+version_num+'/databases')
    # creates the database folder
    create_folder(base_directory+'/installers/'+version_num+'/databases/exe-installers')
    # creates the exe database installer
    create_folder(base_directory+'/installers/'+version_num+'/databases/uncompiled')
    # creates the folder to contain uncompiled databases
    create_folder(base_directory+'/installers/'+version_num+'/databases/zip-files')
    # creates the folder to contain the ziped compiled databases

version_num = input('Please input the version number for the version you are building the installer for: (MAJOR.MINOR.PATCH) ')
# asks the user for the version number of the version that they are creating
print(' ')
# puts in a space to seperate the two inputs as `\n` cannot be used in input request strings
last_version_num = input('Please input the version number for the version that preceded the current one: ')
# asks the user for the last version number this can be used to pull installers which haven't had the modules they contain updated forwards to avoid extra work being done to create new installers
create_version_folder(version_num)
# creates the folder to contain the installers for the new version

dev_tools_got_update = 'Null'
# sets the variable to a blank string to avoid an error relating to the var not being declared
while dev_tools_got_update != 'Y' and dev_tools_got_update != 'N':
    # if the user answers with either 'Y' or 'N' the loop is broken
    print(' ')
    # puts in a blank line
    dev_tools_got_update = input('Did the dev tools module recive any changes? (Y/N): ')
    # asks the user if the dev tools module was updated

new_dev_tools_installer_location = 'C:/Component-Calculator/installers/'+version_num+'/dev_tools_module_installer.EXE'
# works out the location the dev tools module needs to be put when it is created or copyied

if dev_tools_got_update == 'Y':
    # if the user says changes have occured to the dev tools module the program will create a new installer for it
    shutil.make_archive('Dev-Tools-Module-Installer', 'zip', 'C:/Component-Calculator/dev_tools')
    # creates a zip file containing the dev tools folder
    os.system('cmd /c "iexpress /N dev_tools_installer_config.SED"')
    # creates the .EXE installer for the
    shutil.copyfile('C:/Component-Calculator/installer_files/Dev-Tools-Module-Installer.EXE', new_dev_tools_installer_location)
    # moves the newly created installer to the correct location
    os.remove('C:/Component-Calculator/installer_files/Dev-Tools-Module-Installer.EXE')
    # delates the original copy of the installer now it has been moved

elif dev_tools_got_update == 'N':
    # if the user says no changed have been made to the dev tools module the program will just bring the installer from the preivous version forwards
    last_dev_tools_installer_location = 'C:/Component-Calculator/installers/'+last_version_num+'/dev_tools_module_installer.EXE'
    # works out the installer location for the dev tools module in the last version
    shutil.copyfile(last_dev_tools_installer_location, new_dev_tools_installer_location)
    # copys the last dev tools installer to the location the new one should be located

else:
    print('\nError with the program determining if the dev tools module got an update please restart this program')
    # if the loop has been borken but the answer is not Y or N the program will alert the user of the issue and then close
    input('Press enter to close the program: ')
    exit()

launch_exe_updated = 'Null'
# preps the variable to start the loop
while launch_exe_updated != 'Y' and dev_tools_got_update != 'N':
    # when the user answers with 'Y' or 'N' the loop is broken
    print(' ')
    # adds a clear line
    launch_exe_updated = input('Did launch.cmd get changed? (Y/N): ')
    # asks the user if the launch.cmd file recived any changes

if launch_exe_updated == 'Y':
    pass

elif launch_exe_updated == 'N':
    pass

else:
    print('\nError with the program determining if the launch.cmd file got an update please restart this program')
    # if the loop has been borken but the answer is not Y or N the program will alert the user of the issue and then close
    input('Press enter to close the program: ')
    exit()

shutil.copytree()
