class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 1: init
        if len(s) == 0: return 0
        if len(s) == 1: return 1
        L = 0
        window = set()
        window.add(s[L])
        length = len(window)

        # 2: check duplicate
        for R in range(1, len(s)):
            while s[R] in window:
                # duplicate
                window.remove(s[L])
                L += 1

            window.add(s[R])
            length = max(length, R-L+1)

        
        return length
