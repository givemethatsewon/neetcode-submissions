class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums[i] + nums[j] == target
        # target - nums[i]: i -> during visit, check nums[i] is already in dict
        value_idx_dict = dict()
        for i in range(len(nums)):
            if target - nums[i] not in value_idx_dict:
                value_idx_dict[nums[i]] = i
            
            else:
                return [value_idx_dict[target - nums[i]], i]
            
            

