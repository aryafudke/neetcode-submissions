class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts_s = {}
        counts_t = {}
        for i in s:
            counts_s[i] = counts_s.get(i,0) + 1
        for j in t:
            counts_t[j] = counts_t.get(j,0) + 1

        if counts_s == counts_t:
            return True 
        else :
            return False