
# nums = [8, 8, 7, 6, 5] #output--- 7
# nums.sort()
# second_largest = -1
# for i in range(len(nums)-2,-1,-1):
#     if nums[i] != nums[len(nums)-1]:
#         second_largest = nums[i]
#         break


# print(second_largest)

nums = [8, 8, 7, 6, 5]
F_largest = nums[0]
S_largest = -1

for i in range(len(nums)):
    if nums[i] > F_largest:
        S_largest = F_largest
        F_largest = nums[i]
    elif nums[i] > S_largest and nums[i]<F_largest:
        S_largest = nums[i]

print(F_largest,S_largest)