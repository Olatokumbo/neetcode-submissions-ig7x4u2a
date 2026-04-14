class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = {}
        bucket = [[] for _ in range(len(nums)+1)]
        res = []

        for item in nums:
            my_map[item] = my_map.get(item, 0)+1

        for key, value in my_map.items():
            bucket[value].append(key)
        
        for index in range(len(bucket)-1, 0, -1):
            for item in bucket[index]:
                if len(res)<k:
                    res.append(item)

        return res
        