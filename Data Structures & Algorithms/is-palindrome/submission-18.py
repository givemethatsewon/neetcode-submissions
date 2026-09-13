class Solution:
    def isPalindrome(self, s: str) -> bool:
        # pointer at each front and back
        left, right = 0, len(s) - 1
        
        def is_valid(c):
            if 'a' <= c <= 'z' or '0' <= c <= '9' or 'A' <= c <= 'Z':
                return True
            return False
        
        while left < right:
            while left < right and not is_valid(s[left]):
                left += 1
            while left < right and not is_valid(s[right]):
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1

        return True        
