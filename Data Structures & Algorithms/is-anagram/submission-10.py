class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sol 1:
        # using Counter built in dict subclass that counts
        # frequency of elements in an iterable

        return Counter(s) == Counter(t) 

        # sol 2:
        # sort the strings, if they are the same after sort, must be anagrams

        # return sorted(s) == sorted(t)


        # sol 3:
        # add to dict, compare dicts

        # slist, tlist = {}, {}

        # if len(s) != len(t):
        #     return False

        # for i in range(len(s)):
        #     slist[s[i]] = slist.get(s[i], 0) + 1
        #     tlist[t[i]] = tlist.get(t[i], 0) + 1

        # for char in slist:
        #     if slist[char] != tlist.get(char, 0):
        #         return False
        # return True