
nums = [3,0,1,4,2]
n = len(nums)
total_sum = n*(n+1)/2
subtotal = 0

for val in nums:
    subtotal += val


print(int(total_sum-subtotal))