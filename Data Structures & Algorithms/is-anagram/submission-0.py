class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp_s = {}
        temp_t = {}
        for i in s :
            temp_s[i] = temp_s.get(i,0) + 1
        for j in t :
            temp_t[j] = temp_t.get(j,0) + 1
        if temp_s == temp_t:
            return True
        return False
        