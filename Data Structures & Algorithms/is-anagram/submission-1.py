class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = {} 
        both_strings = zip(s,t)
        if len(s) != len(t):
            return False
        for char,char1 in both_strings: 
            if char not in hm:
                hm[char] = 1
            else: 
                hm[char] = hm[char] + 1
            if char1 not in hm:
                hm[char1] = -1
            else:
                hm[char1] = hm[char1] - 1
            if char in hm and hm[char] == 0:
                del hm[char]
            if char1 in hm and hm[char1] == 0:
                del hm[char1]
        # for char in t:
        #     if char not in hm:
        #         return False
        #     elif hm[char] > 1: 
        #         hm[char] = hm[char] - 1
        #     else:
        #         del hm[char]
        if hm:
            return False
        else:
            return True
        