
# nums = [1, 2, 3, 4, 5]
nums = [1, 2, 1, 4, 5]

def check_sort_array(arr):
    
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True


print(check_sort_array(nums))