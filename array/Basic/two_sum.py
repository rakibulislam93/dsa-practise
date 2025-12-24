
nums = [3,2,4] 

# nums = [3,3]
target = 6

mp = {}
for i,val in enumerate(nums):
    need = target - val
    if need in mp:
        print(mp[need],i)
        break

    mp[val]=i

# print("rakibul islam")