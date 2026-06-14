class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles) # k의 범위
        res = high
        
        while low <= high:
            k_mid = (low + high) // 2   # k_mid 계산
            h_sum = 0   # 시간 합 초기화

            for pile in piles:
                h_sum += (pile // k_mid if pile % k_mid == 0 else pile // k_mid + 1) # 시간 합 계산
            
            if h_sum > h: # h보다 크면 k를 키워서 h_sum을 줄여보자
                low = k_mid + 1
            else: # h보다 작거나 같아지면 minimum k를 구하기 위해서 k를 줄여보자
                res = k_mid
                high = k_mid - 1
            
        
        return res


        