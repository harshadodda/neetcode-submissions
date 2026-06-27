class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # my first solution:
        # put into frequency map, sort the frequency map, get k elements from that array
        freq_map = Counter(nums)
        return [item[0] for item in freq_map.most_common(k)]