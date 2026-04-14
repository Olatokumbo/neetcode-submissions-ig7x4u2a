class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums)+1)]
        res : List[int] = []
        my_map = {}

        for value in nums:
            my_map[value] = my_map.get(value,0)+1
        
        for key, value in my_map.items():
            bucket[value].append(key)

        for index in range(len(bucket)-1, 0, -1):
            for item in bucket[index]:
                res.append(item)
                if len(res)==k:
                    return res
