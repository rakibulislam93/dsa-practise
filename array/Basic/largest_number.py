
nums = [3, 3, 6, 1]

"""
This is brute approach..
TimeComplexity--NlogN....SpaceComplexity : O(N)
"""

# nums.sort()
# print(nums[-1])

# Optimize approach ..Time and space : O(N)

def find_maxNumber(arr):
    mx = arr[0]
    for i in range(len(arr)):
        if arr[i] > mx:
            mx = arr[i]
    
    return mx

print(find_maxNumber(nums))
