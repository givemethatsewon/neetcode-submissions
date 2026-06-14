class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            # mid 계산
            mid = (left + right) // 2
            # target이 mid 인덱스의 값 보다 큰 경우 오른쪽 탐색
            if target > nums[mid]:
                left = mid + 1
            # target이 mid 인덱스의 값 보다 작은 경우 왼쪽 탐색
            elif target <nums[mid]:
                right = mid - 1
            # 같을 경우 mid 인덱스 return
            else:
                return mid
        # loop 빠져나올 경우 없다는 의미이므로 -1 return
        return -1
        