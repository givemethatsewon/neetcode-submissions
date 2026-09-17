class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            # 경계를 먼저 찾고
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] <= nums[right]:
                right = mid

        pivot = left
        if pivot == 0:
            left, right = 0, len(nums) - 1

        # 어느 리스트인지 판별
        elif nums[0] <= target <= nums[right - 1]:
            left, right = 0, right - 1
        elif nums[right] <= target <= nums[len(nums) - 1]:  
            left, right = right, len(nums) - 1
        else:
            return - 1
        # 그 리스트 안에서 binary search
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1 
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid
        
        return -1