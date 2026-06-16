class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = {} 
        if len(s) != len(t):
            return False
        for char in s: 
            if char not in hm:
                hm[char] = 1
            else: 
                hm[char] = hm[char] + 1
        for char in t:
            if char not in hm:
                return False
            elif hm[char] > 1: 
                hm[char] = hm[char] - 1
            else:
                del hm[char]
        if hm:
            return False
        else:
            return True
        