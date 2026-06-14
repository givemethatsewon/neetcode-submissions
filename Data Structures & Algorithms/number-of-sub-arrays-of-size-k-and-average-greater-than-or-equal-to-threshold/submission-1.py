class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cnt = 0
        for L in range(0, len(arr) - k + 1):
            R = L + k - 1
            mean = sum(arr[L:R+1]) / k
            if mean >= threshold: 
                cnt += 1
        
        return cnt
