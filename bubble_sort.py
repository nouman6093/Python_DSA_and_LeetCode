#Upper Loop: This loop controls the number of passes through the list. It starts from the end of the list and moves towards the beginning with each iteration. The variable i represents the last index up to which the inner loop needs to iterate in each pass. With each pass, i decreases by 1, which effectively reduces the part of the list that needs to be sorted.
#Inner Loop:  This loop does the actual comparison and swapping of elements. It starts from the beginning of the list and goes up to the ith element (exclusive). In each iteration, it compares the current element (my_list[j]) with the next one (my_list[j + 1]). If the current element is larger, it swaps the two elements. This process is repeated for all pairs of adjacent elements up to the ith index.

def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1):    #iteration starts from 5 in our case, decreases by -1 with each iteration and then stops at 1.
        for j in range(i):
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
    return my_list

print(bubble_sort([4, 2, 6, 5, 1, 3]))
