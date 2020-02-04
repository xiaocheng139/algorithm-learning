#Recursive
def binary_search_recursive(arr, value, left, right):
    if left >= right:
        return False
    else:
        mid = left + (right - left) // 2

        #Compare the mid element with the target value
        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            return binary_search_recursive(arr, value, left, mid-1)
        else:
            return binary_search_recursive(arr, value, mid+1, right)

#Iterable
def binary_search_iterable(arr, value):
    left = 0
    right = len(arr) - 1

    while left + 1 < right:
        mid = left + (right - left) // 2

        if arr[mid] > value:
            right = mid
        elif arr[mid] < value:
            left = mid
        else:
            return mid

    if arr[left] == value:
        return left
    elif arr[right] == value:
        return right
    else:
        return False

def test_binary_search():
    test_arr = [1,5,8,23,145,457,987,1234,2367]
    test_value = 987
    result1 = binary_search_recursive(test_arr, test_value, 0, len(test_arr) - 1)
    result2 = binary_search_iterable(test_arr, test_value)
    print(result1) 
    print(result2)

test_binary_search()