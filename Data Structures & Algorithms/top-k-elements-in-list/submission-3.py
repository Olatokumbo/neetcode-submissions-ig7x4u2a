class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums)+1)]
        my_map = {}
        res = []
        for item in nums:
            my_map[item] = my_map.get(item, 0)+1

        for key, value in my_map.items():
            buckets[value].append(key)

        for index in range(len(buckets)-1, -1, -1):
            for n in buckets[index]:
                res.append(n)
                if len(res)==k:
                    return res