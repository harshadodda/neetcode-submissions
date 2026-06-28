class Solution:

    def encode(self, strs: List[str]) -> str:
        # mark strings with delimiter in between 
        # construct string
        res = ""   
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        # go through the string and find the numbers and construct the array
        strs = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) # i is pointing to the digit, j is pointing to #, using string splicing is exclusive of j so just digit is extracted
            strs.append(s[j + 1 : j + length + 1]) 
            i = j + length + 1 # i is now the next digit after the word we just put in strs and j will be the next # after loop runs again

        return strs