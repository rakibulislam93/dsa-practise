
nums = [1,3,4,2,2]

freq = {}

for val in nums:
    if val in freq:
        freq[val] += 1
    
    freq[val] = 1


