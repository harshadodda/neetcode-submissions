class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # using Counter built in dict subclass that counts
        # frequency of elements in an iterable
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t) 
        
        ana_list = []
        for letter in s:
            ana_list.append(letter)
        for letter in t:
            if letter in ana_list:
                ana_list.remove(letter)
            else:
                return False    
        return len(ana_list) == 0