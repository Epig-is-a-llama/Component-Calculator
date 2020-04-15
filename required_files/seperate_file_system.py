#from tkinter import *

print('\nLoading...\n')

def startup():
    print('\nLoading done!\n')
    input_system()
    print('\nYour calulations will begin shortly.\n')
    read_input_file()

def read_input_file():
    input_file = open('input_file.txt','rt')
    wanted_items = input_file.readlines()
    input_file.close()
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
    output_file = open('needed_items.txt','a')
    output_file.write(item_needed)
    output_file.close()
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

#root = Tk()

startup()

#root.mainloop()
