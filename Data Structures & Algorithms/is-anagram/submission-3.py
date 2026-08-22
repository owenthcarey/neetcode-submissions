class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter_s = {}
        counter_t = {}

        # Get count (in dict) of each letter in s & t
        for i in range(len(s)):
            counter_s[s[i]] = 1 + counter_s.get(s[i], 0)
            counter_t[t[i]] = 1 + counter_t.get(t[i], 0)
        
        # Check if count for each letter matches
        for key in counter_s:
            if counter_s[key] != counter_t.get(key, 0):
                return False
        
        return True