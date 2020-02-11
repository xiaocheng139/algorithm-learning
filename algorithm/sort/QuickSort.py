# Recursion
def quick_sort_helper(target_list):
    if len(target_list) <= 1:
        return target_list

    #Divide Conquer
    randomly_picked_element = target_list.pop()
    greater_list = [ele for ele in target_list if ele > randomly_picked_element]
    less_list = [ele for ele in target_list if ele <= randomly_picked_element]
    
    return quick_sort_helper(less_list) + [randomly_picked_element] + quick_sort_helper(greater_list)

def quick_sort_helper_2(target_list, start, end):
    if start < end:
        position = partition(target_list, start, end)
        quick_sort_helper_2(target_list, start, position-1)
        quick_sort_helper_2(target_list, position+1, end)
    print(target_list)

#While Loop
def quick_sort_helper3(target_list):
    temp_list = target_list

    while True:
        while len(temp_list) > 1:
            randomly_picked_element = temp_list.pop()
            temp_list = [ele for ele in temp_list if ele <= randomly_picked_element]

def partition(arr, start, end):
    sliced_arr = arr[start:end]
    randomly_picked_element = sliced_arr.pop()
    less_list = [ele for ele in sliced_arr if ele <= randomly_picked_element]
    greater_list = [ele for ele in sliced_arr if ele > randomly_picked_element]
    arr = less_list + [randomly_picked_element] + greater_list
    return len(less_list) + start

quick_sort_helper_2([7,1,2,6,9,3,4,5], 2, 7)
