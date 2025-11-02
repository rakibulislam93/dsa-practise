
nums = [10,20,20,20,30,30]

i = 0

for j in range(1,len(nums)):
    if nums[i] != nums[j]:
        nums[i+1] = nums[j]
        i += 1

print(i+1,nums[:i+1])