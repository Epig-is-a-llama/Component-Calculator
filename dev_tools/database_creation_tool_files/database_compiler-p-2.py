# deletes the temporary file which is used to house the database while it is being put into the database installer
os.remove('C:/Component-Calculator/dev_tools/database_creation_tool_files/database.zip')
# tells the user the .exe file has been made and tells them they may now close the program
print('\n.EXE installer for the database created with the name set as: `'+database_name+' installer` when run this will automaticly install the database onto the computer if they have the base program already installed if it does not it will direct them to do so to use this database.\n')
input('Now that the database has been fully processed and saved to the compiled database folder you may now press enter to exit: ')
