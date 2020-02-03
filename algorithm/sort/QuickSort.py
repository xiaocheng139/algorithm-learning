def quick_sort(target_list):
    sorted_list = quick_sort_helper(target_list)
    print(sorted_list)

# Recursion
def quick_sort_helper(target_list):
    if len(target_list) <= 1:
        return target_list

    #Divide Conquer
    randomly_picked_element = target_list.pop()
    greater_list = [ele for ele in target_list if ele > randomly_picked_element]
    less_list = [ele for ele in target_list if ele <= randomly_picked_element]
    
    return quick_sort_helper(less_list) + [randomly_picked_element] + quick_sort_helper(greater_list)

#While Loop
def quick_sort_helper2(target_list):
    temp_list = target_list

    while True:
        while len(temp_list) > 1:
            randomly_picked_element = temp_list.pop()
            temp_list = [ele for ele in temp_list if ele <= randomly_picked_element]
