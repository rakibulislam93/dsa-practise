
nums = [0, 1,0,0, 4, 0, 5, 2]
temp = []
for val in nums:
    if val != 0:
        temp.append(val)


for i in range(len(nums)):
    if i < len(temp):
        nums[i] = temp[i]
    else:
        nums[i] = 0

print(temp)
print(nums)