class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #1: set L and target
        L = 0
        length = default = len(nums) + 1
        total = 0
        #2: increase R 0 -> end
        for R in range(len(nums)):
            total += nums[R]
        #3: compare total >= target
            while total >= target:
            # O -> lenth = min(length, subarray length), increase L controlling total
                length = min(length, R-L+1)
                total -= nums[L]
                L += 1
            # X -> back to #2
        
        return 0 if length == default else length
        