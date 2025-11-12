
# Brute force solution
# nums = [2,0,2,1,1,0]
# nums.sort()
# print(nums)

# Better solution
nums = [2,0,2,1,1,0]
count_zero = 0
count_one = 0
count_two = 0

for val in nums:
    if val == 0:
        count_zero += 1
    
    elif val == 1:
        count_one += 1
    else:
        count_two += 1

for i in range(count_zero):
    nums[i] = 0

for i in range(count_zero,count_zero+count_one):
    nums[i] = 1

for i in range(count_one+count_zero, len(nums)):
    nums[i] = 2

print(count_zero,count_one,count_two)

print(nums)