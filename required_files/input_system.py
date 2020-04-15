print('\nPlease input the items you would like to calulate the required items for.\nTo stop type the word "End" into the input field and the program will start to calulate.')
user_input = 'Null'
run = 0
while user_input != 'End':
    print(' ')
    user_input = input('Please input the item here : ')
    if user_input != 'End':
        user_input_list[0] = user_input

input_file = open('input_file.txt','w')
input_file.write(user_input_list)
input_file.close()
