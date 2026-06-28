class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # my first solution:
        # put into frequency map, sort the map if needed, get top k elements from that frequency map
        # freq_map = Counter(nums)
        # return [item[0] for item in freq_map.most_common(k)]

        # sol 2:
        count = {} # frequency hash map
        freq = [[] for i in range(len(nums) + 1)]

        # creates frequency hash map
        for n in nums: 
            count[n] = 1 + count.get(n, 0) # add 1 to previous count for each num and defaults to 0
        
        # n is the number, c is the the frequency
        for n, c in count.items(): # for every key value pair in the frequency map
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        