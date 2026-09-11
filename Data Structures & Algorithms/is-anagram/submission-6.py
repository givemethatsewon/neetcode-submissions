from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # same char, same number
        # {char : cnt}
        s_char_cnt = defaultdict(int)
        t_char_cnt = defaultdict(int)

        if len(s) != len(t):
            return False

        for char in s:
            s_char_cnt[char] += 1
        for char in t:
            t_char_cnt[char] += 1
        
        return s_char_cnt == t_char_cnt
        