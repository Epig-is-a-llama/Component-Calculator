print('\nLoading...\n')

# declares and sets global variables
global output_list
output_list = list()
global database_name
global user_input_list
global sorted_output_list
global database_settings

def searching_system(wanted_items,raw_output):
    types_of_needed_items_dobble = len(wanted_items)
    types_of_needed_items = types_of_needed_items_dobble/2
    # as the items and number of those items are on seperated items we neeed to half the length of the `whanted_items` list
    item_on = -2
    # sets a variable the loop will need to run itself
    while types_of_needed_items >= item_on:
        item_on = item_on+2
        # goes up in twos as each entry takes two lines
        current_item = whanted_items[item_on]
        current_item_number = whanted_items[item_on + 1]
        # gets the number of items and what items out of the whanted items list
        print('Searching database for entry of : ',current_item)
        # gives the user info mation as to what the progarm is doing
        item_needed = current_item
        current_item = 'C:\Slimefun-Calultator/premade_databases/',database_name,'/Entry-'+current_item+'.txt'
        # makes a varible which will be what the file's name will be so the progarm can propery find it and read the entry
        for x in range(0,current_item_number):
            # loops the apporitate number of times to get the correct number of resorses
            try:
                data_file = open(filename,'rt')
                # trys to open a file as if it fails that means the progarm has reached the end of what it can calulate in that chain
            except Exception as e:
                # goes to the function that writes the raw materials
                raw_output.append(item_needed)
                # makes sure its always entered to a seperate location in the list
                print('\nAdded the following entry to the output file: ',item_needed)
            else:
                data_file = open(filename,'rt')
                # if an entry can be found however it then reads it and sees what it needed to compleate that entry and will repeat the process until it gets to just the raw materials
                entry_data = data_file.read().splitlines()
                data_file.close()
                raw_output.append(searching_system(entry_data,raw_output))
        return raw_output

def database_selection_system():
    print('\nPlease input the name of the database you wish to use.')
    database_name = input('Please put the name here: ')
    # gets the name of the database the user wishes to use then returns it
    return database_name

def database_settings_system(database_name):
    settings_file_location = 'C:\Slimefun-calculator/premade_databases/'+database_name+'/database_settings_file.txt'
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
        user_input = input('Please input the item here : ')
        if user_input != 'End':
            # appends the infomation after the if statement to avoid it writing 'End' into the requested items
            user_input_list.append(user_input)
            # finds out how many of the most recently requested item is needed and then adds it to the list
            user_input_list.append(input('Please input the number of those items you whant to have here : '))
    # returns the requested items
    return user_input_list

def output_system(raw_output):
    print('\nYour calulations are now done the progarm will now convert the output into a readable form\n')
    unsorted_output = output_list
    # prepares to sort the unsorted output which is in an almost impossible to read format
    unsorted_output_len = len(unsorted_output)
    # by doing this command outside of the loop it doesn't have to run it every time the loop runs therefore speeding up the progarm
    not_done == 'Yes'
    output_sort_runs = 0
    # sets these variables to start the loop
    while not_done == 'Yes':
        sorted_output_list_len = len(sorted_output_list)
        sorted_output_list_final_num = sorted_output_list_len - 1
        matching_runs = 0
        while no_match_found == 'Yes':
            if unsorted_output[output_sort_runs] == sorted_output_list[matching_runs]:
                # if the progarm finds an existing entry with this name it will add 1 to it and move on
                number_of_existing_entrys = sorted_output_list[matching_runs+1]
                number_of_existing_entrys = int(number_of_existing_entrys)
                new_number_of_entrys = number_of_existing_entrys + 1
                sorted_output_list[matching_runs+1] = str(new_number_of_entrys)
                no_match_found = 'No'
            elif matching_runs == sorted_output_list_final_num:
                # however if the progarm is unable to find a maching entry it will create a new entry
                sorted_output_list.append(unsorted_output[output_sort_runs])
                sorted_output_list[sorted_output_list_len + 1] = '1'
            matching_runs = matching_runs + 1
        if output_sort_runs == unsorted_output_len:
            not_done = 'No'
            # when its done going thogth the unsorted list it will automaticly brake the loop
        output_sort_runs = output_sort_runs + 1
    if database_settings[1] == 'Yes':
        # will only run this system if its enabled in the database settings and will run it according to how those settings dictate
        not_done = 'Yes'
        line_on = 1
        stack_size = database_settings_file[3]
        stack_size_int = int(stack_size)
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
            stack_count_str = str(stack_count)
            new_number_str = str(new_number)
            # formats the output to include the newley caulualated values
            new_line_contents = current_number+'       ( '+stack_count_str+' stacks and '+new_number+' Items ) '
            sorted_output_list[line_on] = new_line_contents
            line_on = line_on + 2
    # adds the end result to a .txt file and then prints the output to screen
    sorted_output_file = open('sorted_output_file.txt','wt')
    sorted_output_file.write(sorted_output_list)
    sorted_output_file.close()
    print('\nThis is your final output:\n',sorted_output_list)
    # the input is so the progarm doesn't just close when its done
    input('Press enter to close this window and open the output in a .txt file')
    exit()

# tells the user the loading is done
print('\nLoading done!\n')
# runs the function to select the database which is to be used for this calulation
database = database_selection_system()
# runs the function to retrive the settings for the chosen database
settings = database_settings_system(database)
# runs the function to get the requested items from the user
requested_items = input_system(database)
# tells the user their calulations will begin shortly
print('\nYour calulations will begin shortly.\n')
# creates the list which will contain the raw output
unsorted_output = list()
# runs the function to start working out the needed items
unsorted_output = searching_system(requested_items,unsorted_output)
