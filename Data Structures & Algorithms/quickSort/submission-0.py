from typing import *


#Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
        
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def quick(pairs, s: int, e: int) -> None:
            print(s, e)
            if e - s + 1 <= 1: return
            
            pivot: Pair = pairs[e]
            left: int = s # 파티션이 들어갈 인덱스
            
            for i in range(s, e):
                if pairs[i].key < pivot.key:
                    pairs[i], pairs[left] = pairs[left], pairs[i]
                    left += 1
            
            pairs[e], pairs[left] = pairs[left], pairs[e]
            
            quick(pairs, s, left - 1)
            quick(pairs, left + 1, e)
        
        quick(pairs, 0, len(pairs) - 1)
        
        return pairs