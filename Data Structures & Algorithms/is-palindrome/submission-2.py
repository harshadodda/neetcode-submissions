class Solution:
    def isPalindrome(self, s: str) -> bool:
        # sol 1: 
        # my first solution

        # clean_s = "".join(filter(str.isalnum, s)).lower()
        # print(clean_s)
        # i, j = 0, len(clean_s) - 1
        # ret = True
        # while i < j:
        #     if clean_s[i] != clean_s[j]:
        #         return False
        #     i += 1
        #     j -= 1
        # return ret

        # sol 2: 
        # using builtin functions 

        # newStr = ""
        
        # for c in s:
        #     if c.isalnum():
        #         newStr += c.lower()
        
        # return newStr == newStr[::-1]

        # sol 3: 
        # no builtin functions, using 2 pointers
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
