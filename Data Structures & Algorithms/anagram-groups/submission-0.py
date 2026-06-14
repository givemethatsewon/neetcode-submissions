class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = dict()

        for word in strs:
            key = tuple(sorted(c for c in word))
            if key not in anagram_dict:
                anagram_dict[key] = []
            
            anagram_dict[key].append(word)
        
        return [list(i) for i in anagram_dict.values()]