import os
import shutil
# both imported for file and folder manipulation

base_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# works out and sets the var base_directory as the directory of the component-calculator folder the program is being run out of

def major_version(input_version):
    runs = 0
    # starts the runs variable at 0 so the system starts at 0 working out the version number
    output = str()
    # sets the output to be blank as the system appends to it meaning it requires a base string which in this case needs to be clear

    while input_version[runs] != '.':
        # until it reaches the first point in the version number string it will continute to add to the output
        output = output + input_version[runs]
        runs = runs + 1

    return output
    # once the system has worked out the final output it returns it

def create_folder(directory):
    try:
        if not os.path.exists(directory):
            # checks if the folder already exists if it does not it creates it
            os.makedirs(directory)
    except OSError:
        pass

def ask_yn(input_string):
    output = 'Null'
    # sets the variable to a blank string to avoid an error relating to the var not being declared
    while output != 'Y' and output != 'N':
        # if the user answers with either 'Y' or 'N' the loop is broken
        print(' ')
        # puts in a blank line to make it easyer for the user to read the outputs and input prompts
        output = input(input_string)
        # asks the user the question

    return output
    # returns the output

def create_version_folder(version_num):
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

if os.path.exists('C:/Component-Calculator-TEMP'):
    shutil.rmtree('C:/Component-Calculator-TEMP')
    # if the folder already exists it will delate it to ensure that no files are left behind from a previous run of the program if it was stopped before the program had a chance to clear the folder
create_folder('C:/Component-Calculator-TEMP')
# creates a folder to house the files being used by the program for creating the installers

version_num = input('Please input the version number for the version you are building the installer for: (MAJOR.MINOR.PATCH): ')
# asks the user for the version number of the version that they are creating
print(' ')
# puts in a space to seperate the two inputs as `\n` cannot be used in input request strings
last_version_num = input('Please input the version number for the version that preceded the current one: ')
# asks the user for the last version number this can be used to pull installers which haven't had the modules they contain updated forwards to avoid extra work being done to create new installers
create_version_folder(version_num)
# creates the folder to contain the installers for the new version

new_dev_tools_installer_location = base_directory+'/installers/'+version_num+'/dev_tools_module_installer.EXE'
# works out the location the dev tools module needs to be put when it is created or copyied

dev_tools_got_update = ask_yn('Did the dev tools module recive any changes? (Y/N): ')

if dev_tools_got_update == 'Y':
    # if the user says changes have occured to the dev tools module the program will create a new installer for it
    shutil.make_archive('Dev-Tools-Module-Installer' , 'zip' , base_directory+'/dev_tools')
    # creates a zip file containing the dev tools folder
    shutil.copy(base_directory+'/installer_files/Dev-Tools-Module-Installer.zip' , 'C:/Component-Calculator-TEMP/Dev-Tools-Module-Installer.zip')
    shutil.copy(base_directory+'/installer_files/dev_tools_code_extractor.py' , 'C:/Component-Calculator-TEMP/dev_tools_code_extractor.py')
    shutil.copy(base_directory+'/installer_files/dev_tools_installer.cmd' , 'C:/Component-Calculator-TEMP/dev_tools_installer.cmd')
    # creates copys of all the files needed for the installer in the temp folder
    shutil.copyfile(base_directory+'/installer_files/Dev-Tools-Module-Installer.zip' , base_directory+'/installers/'+version_num+'/Dev-Tools-Data.zip')
    # copys the dev tools zip file to the version folder
    os.remove(base_directory+'/installer_files/Dev-Tools-Module-Installer.zip')
    # delates the orginal copy of the zip file as a copy has now been made and placed in the correct place
    os.system('cmd /c "iexpress /N dev_tools_installer_config.SED"')
    # creates the .EXE installer for the dev tools module
    shutil.copyfile('C:/Component-Calculator-TEMP/Dev-Tools-Module-Installer.EXE' , new_dev_tools_installer_location)
    # copies the newly created installer to the correct location

elif dev_tools_got_update == 'N':
    # if the user says no changed have been made to the dev tools module the program will just bring the installer from the preivous version forwards
    last_dev_tools_installer_location = base_directory+'/installers/'+last_version_num+'/dev_tools_module_installer.EXE'
    # works out the installer location for the dev tools module in the last version
    shutil.copyfile(last_dev_tools_installer_location , new_dev_tools_installer_location)
    # copys the last dev tools installer to the location the new one should be located

else:
    print('\nError with the program determining if the dev tools module got an update please restart this program')
    # if the loop has been borken but the answer is not Y or N the program will alert the user of the issue and then close when the user presses enter
    input('Press enter to close the program: ')
    exit()

shutil.rmtree('C:/Component-Calculator-TEMP')
# removes then recreates the temp folder to clear all data out of it
create_folder('C:/Component-Calculator-TEMP')

if major_version(version_num) == major_version(last_version_num):
    if os.path.exists(base_directory+'/Module-Installers'):
        shutil.rmtree(base_directory+'/Module-Installers')
        # only trys to remove the folder if it exists
    # if the major version number (the first part of the version number) has not changed the program will import the databases from the last version the user is then notified of this
    shutil.copytree(base_directory+'/installers/version_num/databases/exe-installers' , base_directory+'/Module-Installers')
    print('\nAs the format for the databases has not changed all databases from the preivous versions have been pulled forwards.\n')
    os.remove(base_directory+'/Module-Installers/Dev-tools-module-installer.EXE')
    # removes the old version of the dev tools module so only the databases are pulled forwards

else:
    create_folder(base_directory+'/Module-Installers')
    # if the major version number has changed (which would signify a change in the database formats) no databases will be pulled forwardsa as the change would prevent them from working with the new version
    # the user is then alerted to this
    print('\nAs the format for the databases has changed no databases have been pulled forwards.\n')

shutil.copy(new_dev_tools_installer_location , base_directory+'/Module-Installers/Dev-tools-module-installer.EXE')
# creates a copy of the dev tools
shutil.make_archive('Module-Installers' , 'zip' , base_directory+'/Module-Installers')
# creates a zip file containing the module installer folder
shutil.copy('Module-Installers.zip' , base_directory+'/installers/'+version_num+'/Module-Installers.zip')
# copys the module installers zip to the right location
os.remove('Module-Installers.zip')
# removes the orginal copy of the module installers zip as there is now a copy in the right location
shutil.make_archive('Other-files' , 'zip' , base_directory+'/other-dependencys')
# creates a zip file containing the other dependencys
shutil.copy('Other-files.zip' , base_directory+'/installers/'+version_num+'/Other-files.zip')
# copys the other files zip to the right location
os.remove('Other-files.zip')
# removes the orginal copy of the other files zip as there is now a copy in the right location

shutil.copy(base_directory+'/installers/'+version_num+'/Module-Installers.zip' , 'C:/Component-Calculator-TEMP/Module-Installers.zip')
shutil.copy(base_directory+'/installer_files/installer.cmd' , 'C:/Component-Calculator-TEMP/installer.cmd')
shutil.copy(base_directory+'/installer_files/code_extractor.py' , 'C:/Component-Calculator-TEMP/code_extractor.py')
shutil.copy(base_directory+'/installers/'+version_num+'/Other-files.zip' , 'C:/Component-Calculator-TEMP/Other-files.zip')
shutil.copy(base_directory+'/installer_files/python_installed_test.py' , 'C:/Component-Calculator-TEMP/python_installed_test.py')
shutil.copy(base_directory+'/installer_files/python_installed_test_result.txt' , 'C:/Component-Calculator-TEMP/python_installed_test_result.txt')
shutil.copy(base_directory+'/installer_files/license_copy.txt' , 'C:/Component-Calculator-TEMP/license.txt')
shutil.copy(base_directory+'/installer_files/python-3.8.1-amd64-webinstall.exe' , 'C:/Component-Calculator-TEMP/python-3.8.1-amd64-webinstall.exe')
# copys the files needed to make the installer to the temp folder

os.system('cmd /c "iexpress /N full_installer_config.SED"')
# runs the command to create the .exe installer for the full program

shutil.copy('C:/Component-Calculator-TEMP/full_installer.EXE' , base_directory+'/installers/'+version_num+'/'+version_num+'-Component-Calculator-Installer.EXE')
# copys the full installer from the temp folde to the correct the location and renames it in the process

shutil.rmtree('C:/Component-Calculator-TEMP')
# removes the temp folder and all its contents as it is now no longer needed

print('The version has now been created to the specifications with the installer files put in the correct places.')
input('Please press enter to exit: ')
