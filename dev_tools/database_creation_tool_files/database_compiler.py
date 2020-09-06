import os
# imports the os module for
import shutil
# imports the module for usage in zipping the compleated database and for part of the .exe creation

def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        pass

un_complied_database_name = input('Please input the name of the .txt file which contains the raw database: ')
un_complied_database_location = 'C:/Component-Calculator/dev_tools/un-complied_databases/'+un_complied_database_name+'.txt'
file_to_sort = open(un_complied_database_location,'rt')
# opens the databse it needs to sort
unsorted_database = file_to_sort.read().splitlines()
# reads the contents of the databse it needs to sort
file_to_sort.close()
total_lines = len(unsorted_database)
# calulates the number of the final index number of the unsorted databse
database_name = input('Please input a name for your database to be given when it is compleated: ')
create_folder('C:/Component-Calculator/dev_tools/compiled_databases/database-to-pack/'+database_name)
# creates the folder which will contain the database once its done sorting
final_entry = total_lines - 1
done = 'No'
line_on = -1
# sets varibles to start the loop
while done == 'No':
    line_on = line_on + 1
    current_line = unsorted_database[line_on]
    if current_line[0] == 'E' and current_line[1] == 'n' and current_line[2] == 't' and current_line[3] == 'r' and current_line[4] == 'y' and current_line[5] == '-':
        # cheacks the first 6 caracters of the line indicate its the start of a new entry
        start_of_entry = line_on
        end_of_entry_not_found = 'Yes'
        while end_of_entry_not_found == 'Yes':
            line_on = line_on + 1
            if unsorted_database[line_on] == 'End of entry':
                end_of_entry = line_on
                # marks the end of the entry
                end_of_entry_not_found = 'No'
        run = 0
        entry_own_file = list()
        for x in range(start_of_entry,end_of_entry):
            entry_own_file.append(unsorted_database[run+start_of_entry])
            run = run + 1
        new_filename = 'C:/Component-Calculator/dev_tools/compiled_databases/database-to-pack/'+database_name+'/'+unsorted_database[start_of_entry]+'.txt'
        new_file = open(new_filename,'wt')
        run = 1
        for x in range(1,len(entry_own_file)):
            # writes the entry into the file
            new_file.write(entry_own_file[run])
            new_file.write('\n')
            run = run + 1
        new_file.close()
        # writes to its own file therefore sorting that bit of data
    if line_on == final_entry:
        done = 'Yes'
print('\nThe databse has now been sorted now the database configuration file must be setup.')
config_template = open('C:/Component-Calculator/dev_tools/database_creation_tool_files/config_template.txt','rt')
# opens reads into a list then closes the config template file
config_template_contents = config_template.read().splitlines()
config_template.close()
config_list = list()
# sets vars in preperation for the loop
runs = 0
total_config_options = int(len(config_template_contents) / 2)
for x in range (0,total_config_options):
    # loops once per config setting (as each setting takes two lines with one as the tile and one as the value)
    print('\nFor the setting of: ',config_template_contents[runs],' what would you like to set for this setting?')
    # asks the user what value they want to set each setting in the config to
    setting = input('Please answer here: ')
    config_list.append(config_template_contents[runs])
    # appends the setting title and then the setting value to the list which will be later writen to the new config file
    config_list.append(setting)
    # increases by two at a time as each setting takes two lines
    runs = runs + 2
runs = 0
new_config_file = open('C:/Component-Calculator/dev_tools/compiled_databases/database-to-pack/'+database_name+'/database_settings_file.txt','wt')
for x in range (0,len(config_list)):
    # writes what the user chose as the config options to the config file
    new_config_file.write(config_list[runs])
    new_config_file.write('\n')
    runs = runs + 1
# once its done writing it closes the file
new_config_file.close()
print('\nConfig file created and saved.')
# tells the user the config has been created and saved and then begins to zip the database
print('\nCreating a zip file containing the database...\n')
database_location = 'C:/Component-Calculator/dev_tools/compiled_databases/database-to-pack/'
# works out the location of the folder containing the database and then executes the code to zip it then notifies the user
shutil.make_archive('database', 'zip', database_location)
original = 'database.zip'
target = 'C:/Component-Calculator/dev_tools/compiled_databases/'+database_name+'.zip'
shutil.copyfile(original, target)
shutil.rmtree('C:/Component-Calculator/dev_tools/compiled_databases/database-to-pack/'+database_name)
print('\nDatabase zipped into a .zip file with the name of the database as its name.')
print('\nCreating a .EXE installer for the database...')
# opens the exe config file and puts in the apporitate infomation to ensure the database installer works correcntly
exe_config_file = open('C:/Component-Calculator/dev_tools/database_creation_tool_files/pack_installer_config.SED','r+')
exe_config_list = exe_config_file.read().splitlines()
exe_config_file.close()
exe_config_file = open('C:/Component-Calculator/dev_tools/database_creation_tool_files/pack_installer_config.SED','wt')
exe_config_list[26] = 'TargetName=C:/Component-Calculator/dev_tools/compiled_databases/'+database_name+'-database-installer.EXE'
runs = 0
for x in range(0, len(exe_config_list)):
    exe_config_file.write(exe_config_list[runs])
    exe_config_file.write('\n')
    runs = runs + 1
exe_config_file.close()
os.system('cmd /c "iexpress /N C:\Component-Calculator\dev_tools\database_creation_tool_files\pack_installer_config.SED"')
# deletes the temporary file which is used to house the database while it is being put into the database installer
os.remove('database.zip')
# tells the user the .exe file has been made and tells them they may now close the program
print('\n.EXE installer for the database created with the name set as: `'+database_name+' installer` when run this will automaticly install the database onto the computer if they have the base program already installed if it does not it will direct them to do so to use this database.\n')
input('Now that the database has been fully processed and saved to the compiled database folder you may now press enter to exit: ')
