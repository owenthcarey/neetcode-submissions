class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {letter : 0 for letter in s}
        t_dict = {letter : 0 for letter in t}
        for letter in s:
            s_dict[letter] += s_dict[letter] + 1
        for letter in t:
            t_dict[letter] += t_dict[letter] + 1
        return s_dict == t_dict
