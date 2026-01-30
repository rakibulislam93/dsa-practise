
arr = [3, 5, 2, 8, 1, 4]

# Brute-force approach to find the largest number
# time complexity: O(n^2)
def find_largest_brute(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr 


# Optimized approach to find the largest number
# time complexity: O(n)
def find_largest_optimized(arr):
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num

print(find_largest_brute(arr)[-1])
print(find_largest_optimized(arr))