class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # creates empty list [] for each new key
        my_map = defaultdict(list)

        for s in strs:
            # initialize an array of 26 0s for character count
            count = [0] * 26
            for char in s:
                # ord() converts each character to its ASCII number
                # ord(char) - ord('a') maps each letter to an index 0–25
                count[ord(char) - ord('a')] += 1
            # must change to tuple to use as dict key because list cant be used as dict key
            my_map[tuple(count)].append(s)
        
        # values() returns all grouped lists and list casting changes it
        # from a tuple back to a list
        return list(my_map.values())