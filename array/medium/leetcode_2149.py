
nums = [3,1,-2,-5,2,-4]

# Brute force solution .................
# pos_arr = []
# neg_arr = []
# result = []
# for val in nums:
#     if val>0:
#         pos_arr.append(val)
#     else:
#         neg_arr.append(val)

# for i in range(len(pos_arr)):
#     result.append(pos_arr[i])
#     result.append(neg_arr[i])

# print(pos_arr)
# print(neg_arr)
# print(result)

# Optimize solution ..............

result = [0]* len(nums)
pos_indx = 0
neg_indx = 1

for val in nums:
    if val>0:
        result[pos_indx] = val
        pos_indx += 2
    else:
        result[neg_indx] = val
        neg_indx += 2
    

print(result)
