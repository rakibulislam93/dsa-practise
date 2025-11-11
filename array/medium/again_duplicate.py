
nums = [1,3,4,2,2]

slow = nums[0]
fast = nums[0]

slow = nums[slow]
fast = nums[nums[fast]]

while slow != fast:
    slow = nums[slow]
    fast = nums[nums[fast]]

slow = nums[0]

while slow != fast:
    slow = nums[slow]
    fast = nums[fast]


print(slow,fast)