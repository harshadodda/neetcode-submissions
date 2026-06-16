class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sol 1:
        # using Counter built in dict subclass that counts
        # frequency of elements in an iterable
        #return Counter(s) == Counter(t) 

        # sol 2:
        # sort the strings, if they are the same after sort, must be anagrams
        return sorted(s) == sorted(t)

        ana_list = []
        for letter in s:
            ana_list.append(letter)
        for letter in t:
            if letter in ana_list:
                ana_list.remove(letter)
            else:
                return False    
        return len(ana_list) == 0