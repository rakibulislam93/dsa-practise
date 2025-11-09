
nums = [2, 3, 5, -2, 7, -4] # output -- 15
# nums = [1, -2, 3] # output -- 3


# max_sum = float('-inf')
# n = len(nums)

# for i in range(n):
#     for j in range(n):
#         current_sum = 0
#         for k in range(i,j+1):
#             current_sum += nums[k]
        
#         max_sum = max(max_sum,current_sum)


# for i in range(n):
#     current_sum = 0
#     for j in range(i,n):
#         current_sum += nums[j]
#         max_sum = max(max_sum,current_sum)

max_sum = nums[0]
curr_sum = nums[0]

for i in range(1,len(nums)):
    curr_sum = max(nums[i],curr_sum + nums[i])
    max_sum = max(curr_sum,max_sum)


print(max_sum)