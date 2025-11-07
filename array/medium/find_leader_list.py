
nums = [1, 2, 5, 3, 1, 2]
leader_list = []
max_from_right = float('-inf')

for i in range(len(nums)-1,-1,-1):
    if nums[i] > max_from_right:
        max_from_right = nums[i]
        leader_list.append(nums[i])

print(leader_list[::-1])