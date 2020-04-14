file_to_sort = open('Unorganised_database.txt','r')
unsorted_database = file_to_sort.readlines()
file_to_sort.close()
total_lines = len(unsorted_database)
not_sorted = 'Yes'
while not_sorted == 'Yes':
    
