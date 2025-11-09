
nums = [2, 3, 5, -2, 7, -4] # output -- 15
# nums = [1, -2, 3] # output -- 3


max_sum = float('-inf')
n = len(nums)

for i in range(n):
    for j in range(n):
        current_sum = 0
        for k in range(i,j+1):
            current_sum += nums[k]
        
        max_sum = max(max_sum,current_sum)


print(max_sum)