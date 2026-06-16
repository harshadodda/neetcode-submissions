class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ana_list = []
        for letter in s:
            ana_list.append(letter)
        for letter in t:
            if letter in ana_list:
                ana_list.remove(letter)
            else:
                return False    
        return len(ana_list) == 0