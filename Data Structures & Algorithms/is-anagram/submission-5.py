class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # same char, same number of time -> {char: #}
        if len(s) != len(t): 
            return False
        def get_number_of_times(string):
            char_times = {}
            for c in string:
                if c not in char_times:
                    char_times[c] = 0
                else:
                    char_times[c] += 1
            return char_times

        char_times_of_s = get_number_of_times(s)
        char_times_of_t = get_number_of_times(t)
        
        for key in char_times_of_s:
            if key in char_times_of_t:
                if  char_times_of_s[key] != char_times_of_t[key]:
                    return False
            else:
                return False

        return True