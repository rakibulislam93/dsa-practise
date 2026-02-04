
# class Solution {
# public:
#     bool isMonotonic(vector<int>& nums) {
#         bool decrease = true;
#         bool increase = true;
#         int n = nums.size();

#         for(int i = 0; i < n - 1; i++){
#             if(nums[i] < nums[i+1]){
#                 decrease = false;
#             }
#             if(nums[i] > nums[i+1]){
#                 increase = false;
#             }
#         }

#         return decrease || increase;
#     }
# };

from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        decrease = True
        increase = True
        n = len(nums)
        
        for i in range(n - 1):
            if nums[i] < nums[i + 1]:
                decrease = False
            if nums[i] > nums[i + 1]:
                increase = False
        
        return decrease or increase