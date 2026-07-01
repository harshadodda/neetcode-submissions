class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join(filter(str.isalnum, s)).lower()
        print(clean_s)
        i, j = 0, len(clean_s) - 1
        ret = True
        while i < j:
            if clean_s[i] != clean_s[j]:
                return False
            i += 1
            j -= 1
        return ret
