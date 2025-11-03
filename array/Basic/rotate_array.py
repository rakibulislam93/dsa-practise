
# nums = [1,2,3,4,5,6,7] 
nums = [-1,-100,3,99]
k = 2

# temp = nums[len(nums)-k:]
# for i in range(len(nums)-k):
#     temp.append(nums[i])

# print(temp)

k = k % len(nums)
nums.reverse()
nums[:k] = reversed(nums[:k])
nums[k:] = reversed(nums[k:])