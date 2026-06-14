import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt_dict = {}
        for num in nums:
            if num not in cnt_dict:
                cnt_dict[num] = 0
            
            cnt_dict[num] += 1
        
        return heapq.nlargest(k, cnt_dict.keys(), key=lambda x: cnt_dict[x])

        # nums_sorted_by_cnt = sorted(cnt_dict.keys(), key=lambda x: cnt_dict[x] )
        
        # return nums_sorted_by_cnt[-k:]

        