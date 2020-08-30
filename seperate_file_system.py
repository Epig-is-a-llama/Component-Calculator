print('\nLoading...\n')

import math
# imported for the math.ceil() function

# creates and makes global the list which will contain the raw output
global raw_output
raw_output = list()

def searching_system(wanted_items,database_name):
    types_of_needed_items = len(wanted_items)
    print('types of needed items: ', types_of_needed_items)
    # works out the amount of items in the `whanted_items` list
    print('wanted items: ', wanted_items)
    item_on = 0
    # sets a variable the loop will need to run itself
    while types_of_needed_items > item_on:
        current_item = wanted_items[item_on]
        current_item_number = int(wanted_items[item_on + 1])
        # gets the number of items and what items out of the whanted items list
        print('\nSearching database for entry of : ',current_item)
        # gives the user info mation as to what the progarm is doing
        item_needed = current_item
        current_item = 'C:/Component-Calculator/databases/'+database_name+'/Entry-'+current_item+'.txt'
        # makes a varible which will be what the file's name will be so the progarm can propery find it and read the entry
        try:
            test_file = open(current_item, 'rt')
            # trys to open a file as if it fails that means the progarm has reached the end of what it can calulate in that chain
        except Exception as e:
            entry_exists = False
            batches_needed = current_item_number
        else:
            entry_exists = True
            data_file = open(current_item,'rt')
            # if an entry can be found however it then reads it and sees what it needed to compleate that entry and will repeat the process until it gets to just the raw materials
            raw_entry_data = data_file.read().splitlines()
            batches_needed = math.ceil(current_item_number / int(raw_entry_data[0]))
        for x in range(0,batches_needed):
            # loops the apporitate number of times to get the correct number of resorses
            if entry_exists == False:
                # writes the raw materials
                raw_output.append(item_needed)
                # makes sure its always entered to a seperate location in the list
                print('\nAdded the following entry to the output file: ',item_needed)
            else:
                runs = 1
                entry_data = list()
                for x in range(1, len(raw_entry_data)):
                    entry_data.append(raw_entry_data[runs])
                    runs = runs + 1
                data_file.close()
                (searching_system(entry_data,database_name))
        item_on = item_on+2
        print('item on: ', item_on)
        # goes up in twos as each entry takes two lines

def database_selection_system():
    print('\nPlease input the name of the database you wish to use.')
    database_name = input('Please put the name here: ')
    # gets the name of the database the user wishes to use then returns it
    return database_name

def database_settings_system(database_name):
    settings_file_location = 'C:/Component-Calculator/databases/'+database_name+'/database_settings_file.txt'
    database_settings_file = open(settings_file_location,'rt')
    database_settings = database_settings_file.read().splitlines()
    # reads the database settings file which can be used to configure the size of stacks and even to run that system the itention is to have it able to manilulate the progarm from this file
    database_settings_file.close()
    # returns the contends of the database settings
    return database_settings

def input_system(database_name):
    # gives the user instctictions on how to input the data in the correct form
    print('\nPlease input the items you would like to calulate the required items for (using the database',database_name,').\nTo stop type the word "End" into the input field and the program will start to calulate.')
    # sets up the variables needed by the list
    user_input = 'Null'
    user_input_list = list()
    while user_input != 'End':
        # adds a clear line in to allow for the user to clearly see the which quanity request matches with which item request
        print(' ')
        # asks the user what item they need
        user_input = input('Please input the item name here : ')
        if user_input != 'End':
            # appends the infomation after the if statement to avoid it writing 'End' into the requested items
            user_input_list.append(user_input)
            # finds out how many of the most recently requested item is needed and then adds it to the list
            user_input_list.append(input('Please input the amount of \''+user_input+'\' you wish to have : '))
    # returns the requested items
    return user_input_list

def output_system(raw_output,database_settings):
    print('\nYour calulations are now done the progarm will now convert the output into a readable form\n')
    unsorted_output = raw_output
    # prepares to sort the unsorted output which is in an almost impossible to read format
    unsorted_output_len = len(unsorted_output)
    # by doing this command outside of the loop it doesn't have to run it every time the loop runs therefore speeding up the progarm
    not_done = 'Yes'
    output_sort_runs = 0
    sorted_output_list = list()
    # sets these variables to start the loop
    while not_done == 'Yes':
        sorted_output_list_len = len(sorted_output_list)
        sorted_output_list_final_num = sorted_output_list_len
        matching_runs = 0
        no_match_found = 'Yes'
        while no_match_found == 'Yes':
            if matching_runs == sorted_output_list_final_num:
                # however if the progarm is unable to find a maching entry it will create a new entry
                sorted_output_list.append(unsorted_output[output_sort_runs])
                sorted_output_list.append('1')
                no_match_found = 'No'
            elif unsorted_output[output_sort_runs] == sorted_output_list[matching_runs]:
                # if the progarm finds an existing entry with this name it will add 1 to it and move on
                number_of_existing_entrys = sorted_output_list[matching_runs+1]
                number_of_existing_entrys = int(number_of_existing_entrys)
                new_number_of_entrys = number_of_existing_entrys + 1
                sorted_output_list[matching_runs+1] = str(new_number_of_entrys)
                no_match_found = 'No'
            matching_runs = matching_runs + 1
            # when its done going thogth the unsorted list it will automaticly brake the loop
        output_sort_runs = output_sort_runs + 1
        if output_sort_runs == unsorted_output_len:
            not_done = 'No'
    if database_settings[1] == 'Yes':
        # will only run this system if its enabled in the database settings and will run it according to how those settings dictate
        not_done = 'Yes'
        line_on = 1
        stack_size = database_settings[3]
        stack_size_int = int(stack_size)
        sorted_output_list_len = len(sorted_output_list)
        stack_system_final_line = sorted_output_list_len + 1
        # sets these varibles for the loop which is on the next line
        while not_done == 'Yes':
            current_number = sorted_output_list[line_on]
            new_number = int(current_number)
            stack_count = 0
            # sets the needed variables out side the loop to improve performance
            while new_number >= stack_size_int:
                new_number = new_number - stack_size_int
                # until the number is below the set stack size it will keep calulating to see how many stacks of each item are needed
                stack_count = stack_count + 1
            current_number_str = str(current_number)
            stack_count_str = str(stack_count)
            new_number_str = str(new_number)
            # formats the output to include the newley caulualated values
            if new_number > 0:
                new_line_contents = current_number_str+'       ( '+stack_count_str+' stacks and '+new_number_str+' items ) '
            else:
                new_line_contents = current_number_str+'       ( '+stack_count_str+' stacks ) '
            sorted_output_list[line_on] = new_line_contents
            line_on = line_on + 2
            if line_on == stack_system_final_line:
                not_done = 'No'
    # adds the end result to a .txt file and then prints the output to screen
    formated_output = "\n".join(sorted_output_list)
    sorted_output_file = open('sorted_output_file.txt','wt')
    sorted_output_file.write(formated_output)
    sorted_output_file.close()
    print('\nThis is your final output:\n',formated_output)
    # the input is so the progarm doesn't just close when its done
    input('Press enter to close this window and open the output in a .txt file: ')

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
