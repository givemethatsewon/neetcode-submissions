class Solution:
    def isPalindrome(self, s: str) -> bool:
        # pointer at each front and back
        left, right = 0, len(s) - 1
        
        def is_valid(c):
            if 'a' <= c <= 'z' or '0' <= c <= '9':
                return True
            return False
        
        s = s.lower()
        while left < right:
            while not is_valid(s[left]) and left < right:
                left += 1
            while not is_valid(s[right]) and left < right:
                right -= 1
            
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1

        return True        
