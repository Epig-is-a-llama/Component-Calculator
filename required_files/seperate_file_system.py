print('\nLoading...\n')

#from tkinter import *

global output_run_times
output_run_times = 0
global output_list
global user_input_list
global sorted_output_list

def startup():
    print('\nLoading done!\n')
    input_system()
    print('\nYour calulations will begin shortly.\n')
    read_input_file()

def read_input_file():
    wanted_items = user_input_list
    searching_system(wanted_items)

def searching_system(wanted_items):
    types_of_needed_items_dobble = len(wanted_items)
    types_of_needed_items = types_of_needed_items_dobble/2
    item_on = -2
    while types_of_needed_items >= item_on:
        item_on = item_on+2
        current_item = whanted_items[item_on]
        print('Searching database for entry of : ',current_item)
        item_needed = current_item
        current_item = 'Entry-'+current_item+'.txt'
        entry_located(current_item,item_needed)

def entry_located(filename,item_needed):
    try:
        data_file = open(filename,'r')
    except Exception as e:
        write_needed_item(item_needed)
    else:
        data_file = open(filename,'r')
        entry_data = data_file(readlines)
        data_file.close()
        searching_system(entry_data)

def write_needed_item(item_needed):
    output_list[output_run_times]
    output_run_times = output_run_times + 1
    print('\nAdded the following entry to the output file: ',item_needed)

def input_system():
    print('\nPlease input the items you would like to calulate the required items for.\nTo stop type the word "End" into the input field and the program will start to calulate.')
    user_input = 'Null'
    run = 0
    while user_input != 'End':
        print(' ')
        user_input = input('Please input the item here : ')
        if user_input != 'End':
            user_input_list[0] = user_input

def output_system():
    unsorted_file = open('raw_output_file.txt','r')
    unsorted_output = unsorted_file.readlines()
    unsorted_file.close()
    unsorted_output_len = len(unsorted_output)
    not_done == 'Yes'
    output_sort_runs = 0
    while not_done == 'Yes':
        sorted_output_list_len = len(sorted_output_list)
        sorted_output_list_final_num = sorted_output_list_len - 1
        matching_runs = 0
        while no_match_found == 'Yes':
            if unsorted_output[output_sort_runs] == sorted_output_list[matching_runs]:
                number_of_existing_entrys = sorted_output_list[matching_runs+1]
                number_of_existing_entrys = int(number_of_existing_entrys)
                new_number_of_entrys = number_of_existing_entrys + 1
                sorted_output_list[matching_runs+1] = str(new_number_of_entrys)
                no_match_found = 'No'
            elif matching_runs == sorted_output_list_final_num:
                sorted_output_list[sorted_output_list_len] = unsorted_output[output_sort_runs]
                sorted_output_list[sorted_output_list_len + 1] = '1'
            matching_runs = matching_runs + 1
        if output_sort_runs == unsorted_output_len:
            not_done = 'No'
        output_sort_runs = output_sort_runs + 1
    if database_settings[1] == 'Yes':
        not_done = 'Yes'
        line_on = 1
        stack_size = database_settings_file[3]
        stack_size_int = int(stack_size)
        while not_done == 'Yes':
            current_number = sorted_output_list[line_on]
            new_number = int(current_number)
            stack_count = 0
            while new_number > stack_size_int:
                new_number = new_number - stack_size_int
                stack_count = stack_count + 1
            if new_number == stack_size_int:
                new_number = 0
                stack_count = stack_count + 1
            stack_count_str = str(stack_count)
            new_number_str = str(new_number)
            new_line_contents = current_number+'       ( '+stack_count_str+' stacks and '+new_number+' Items ) '
            sorted_output_list[line_on] = new_line_contents
            line_on = line_on + 2
    sorted_output_file = open('sorted_output_file.txt','wt')
    sorted_output_file.write(sorted_output_list)
    sorted_output_file.close()
    print('\nThis is your final output:\n',sorted_output_list)
    input('Press enter to close this window and open the output in a .txt file')
    exit()

#root = Tk()

startup()

#root.mainloop()
