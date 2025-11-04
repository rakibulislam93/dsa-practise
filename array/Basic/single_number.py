
# nums = [1, 2, 2, 4, 3, 1, 4]
# nums = [4,1,2,1,2]
nums = [1]


N = 3 * 10**4
freq = [0]* (N+1)

for val in nums:
    freq[val] += 1 
        
for val in nums:
    if freq[val]==1:
       print(val)
       break
        
