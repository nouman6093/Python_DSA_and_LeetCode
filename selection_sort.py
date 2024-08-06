def selection_sort(my_list):
    for i in range(len(my_list) - 1):
        v = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[v]:
                v = j   #v becomes minimum
        temp = my_list[i]
        my_list[i] = my_list[v]
        my_list[v] = temp
    return my_list

print(selection_sort([4, 2, 6, 5, 1, 3]))
