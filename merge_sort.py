#this is the easiest sorting algorithm and probably my favorite

def merge(list1, list2):    #this is just a helper method
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):    #as long as there are elements in list1 and list2 this loop will keep looping
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1

    while i < len(list1):   #if there are some elements left in loop1 then this is gonna execute
        combined.append(list1[i])
        i += 1

    while j < len(list2):   #if there are some elements left in loop2 then this is gonna execute
        combined.append(list2[j])
        j += 1

    return combined

def merge_sort(my_list):    #this is main sorting method
    #base case:
    if len(my_list) == 1:
        return my_list

    #recursive case:
    mid_index = int(len(my_list) / 2)   #eg: if list contains 4 elements (index = 0, 1, 2, 3). its mid is going to be index 2 (0,1,2 wala 2, 3)
    #splitting happens here also merge_sort is used here as recursively:
    left = merge_sort(my_list[:mid_index])  #whatever is on the left becomes starting point. if you dont have anything on the left then the starting point is first element, and we dont include the mid_index
    right = merge_sort(my_list[mid_index:])

    return merge(left, right)

print(merge_sort([3, 1, 4, 2]))
