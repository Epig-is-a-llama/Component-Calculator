file_to_sort = open('Unorganised_database.txt','r')
unsorted_database = file_to_sort.readlines()
# reads the contents of the databse it needs to sort
file_to_sort.close()
total_lines = len(unsorted_database)
# calulates the number of the final index number of the unsorted databse
final_entry = total_lines+1
done = 'No'
line_on = -1
# sets varibles to start the loop
while done == 'No':
    line_on = line_on + 1
    current_line = unsorted_database[line_on]
    if current_line[0] == 'E' and current_line[1] == 'n' and current_line[2] == 't' and current_line[3] == 'r' and current_line[4] == 'y' and current_line[5] == '-':
        # cheacks the first 6 caracters of the entry are correct
        start_of_entry = line_on
        end_of_entry_not_found = 'Yes'
        while end_of_entry_not_found == 'Yes':
            line_on = line_on + 1
            if unsorted_database[line_on] == 'End of entry':
                end_of_entry = line_on
                # marks the end of the entry
                end_of_entry_not_found = 'No'
        run = 0
        for x in range(start_of_entry,end_of_entry):
            entry_own_file[run] = unsorted_database[run+start_of_entry+1]
            run = run + 1
        new_filename = unsorted_database[start_of_entry]+'.txt'
        new_file = open(new_filename,'wt')
        new_file.write(entry_own_file)
        new_file.close()
        # writes to its own file therefore sorting that bit of data
    if line_on == total_lines:
        done = 'Yes'
print('\nThe databse has now been sorted!')
input('Press enter to exit')
