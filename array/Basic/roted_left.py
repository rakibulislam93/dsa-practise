
# nums = [1, 2, 3, 4, 5]
nums = [-1, 0, 3, 6]

for i in range(len(nums)-1):
    temp = nums[i]
    nums[i]=nums[i+1]
    nums[i+1] = temp
print(nums)