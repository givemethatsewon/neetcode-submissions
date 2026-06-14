# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        result_list = []    
        for i in range(1, len(pairs)):
            j = i - 1
            result_list.append(pairs[::])
            while j >= 0 and pairs[j+1].key < pairs[j].key: 
                pairs[j+1], pairs[j] = pairs[j], pairs[j+1]                
                j -= 1
        result_list.append(pairs[::])
        return pairs if not pairs else result_list