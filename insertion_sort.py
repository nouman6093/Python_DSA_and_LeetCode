def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        current_variable = my_list[i]   #smaller value is stored here
        previous_index = i - 1  #possibility that previous value may be bigger value
        while previous_index >= 0 and current_variable < my_list[previous_index]:   #current_variable keeps getting compared with previous value as long as index of previous index reaches 0
            my_list[previous_index + 1] = my_list[previous_index]   #big value which is located at my_list[previous_index] is stored in the location of small value which is my_list[previous + 1] aka current_value
            my_list[previous_index] = current_variable
            previous_index -= 1

    return my_list

print(insertion_sort([4, 2, 6, 5, 1, 3]))
