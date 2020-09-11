from database_read_code import *

# tells the user the loading is done
print('\nLoading done!\n')
# runs the function to select the database which is to be used for this calulation
database = database_selection_system()
# runs the function to retrive the settings for the chosen database
settings = database_settings_system(database)
# runs the function to get the requested items from the user
input_items = input_system(database)
# tells the user their calulations will begin shortly
print('\nYour calulations will begin shortly.\n')
# runs the function to start working out the needed items
searching_system(input_items,database)
# calls the function to give the user their results
output_system(raw_output,settings)
