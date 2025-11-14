
nums = [3,1,-2,-5,2,-4]
pos_arr = []
neg_arr = []
result = []
for val in nums:
    if val>0:
        pos_arr.append(val)
    else:
        neg_arr.append(val)

for i in range(len(pos_arr)):
    result.append(pos_arr[i])
    result.append(neg_arr[i])



print(pos_arr)
print(neg_arr)
print(result)