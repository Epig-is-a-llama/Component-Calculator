#from tkinter import *

def startup():
    database_file = open('main_database.txt','rt')
    full_database = database_file.readlines()
    database_file.close()
    read_input_file(full_database)

def read_input_file(full_database):
    input_file = open('input_file.txt','rt')
    wanted_items = input_file.readlines()
    input_file.close()
    searching_system(full_database,wanted_items)

def searching_system(full_database,wanted_items):
    types_of_needed_items_dobble = len(wanted_items)
    types_of_needed_items = types_of_needed_items_dobble/2
    item_on = -2
    while types_of_needed_items >= item_on:
        item_on = item_on+2
        current_item = whanted_items[item_on]
        current_item = 'Entry-'+current_item
        first_letter = current_item[0]
        if first_letter == 'A' or first_letter == 'a':
            letter_ID = 1
        elif first_letter == 'B' or first_letter == 'b':
            letter_ID = 2
        elif first_letter == 'C' or first_letter == 'c':
            letter_ID = 3
        elif first_letter == 'D' or first_letter == 'd':
            letter_ID = 4
        elif first_letter == 'E' or first_letter == 'e':
            letter_ID = 5
        elif first_letter == 'F' or first_letter == 'f':
            letter_ID = 6
        elif first_letter == 'G' or first_letter == 'g':
            letter_ID = 7
        elif first_letter == 'H' or first_letter == 'h':
            letter_ID = 8
        elif first_letter == 'I' or first_letter == 'i':
            letter_ID = 9
        elif first_letter == 'J' or first_letter == 'j':
            letter_ID = 10
        elif first_letter == 'K' or first_letter == 'k':
            letter_ID = 11
        elif first_letter == 'L' or first_letter == 'l':
            letter_ID = 12
        elif first_letter == 'M' or first_letter == 'm':
            letter_ID = 13
        elif first_letter == 'N' or first_letter == 'n':
            letter_ID = 14
        elif first_letter == 'O' or first_letter == 'o':
            letter_ID = 15
        elif first_letter == 'P' or first_letter == 'p':
            letter_ID = 16
        elif first_letter == 'Q' or first_letter == 'q':
            letter_ID = 17
        elif first_letter == 'R' or first_letter == 'r':
            letter_ID = 18
        elif first_letter == 'S' or first_letter == 's':
            letter_ID = 19
        elif first_letter == 'T' or first_letter == 't':
            letter_ID = 20
        elif first_letter == 'U' or first_letter == 'u':
            letter_ID = 21
        elif first_letter == 'V' or first_letter == 'v':
            letter_ID = 22
        elif first_letter == 'W' or first_letter == 'w':
            letter_ID = 23
        elif first_letter == 'X' or first_letter == 'x':
            letter_ID = 24
        elif first_letter == 'Y' or first_letter == 'y':
            letter_ID = 25
        elif first_letter == 'Z' or first_letter == 'z':
            letter_ID = 26
        else:
            print('\n\nError:\nA letter ID could not be defiened this is very likley to be a database file error the problem entry in the database is: ', current_item)
            input('')
        letter_ID_full = letter_ID + 1
        start_line = readline(letter_ID_full)
        start_line = int(start_line)
        start_line = start_line - 1
        line_on = start_line
        if letter_ID != 26:
            letter_ID_end = letter_ID + 2
            end_line = readline(letter_ID_end)
            end_line = int(end_line)
            end_line = end_line + 1
        elif letter_ID == 26:
            end_line = len(full_database)
        else:
            print('Error:\nLetter ID variable could not be read')
        not_found = 'Yes'
        while not_found == 'Yes':
            line_on = line_on + 1

#root = Tk()

startup()

#root.mainloop()
