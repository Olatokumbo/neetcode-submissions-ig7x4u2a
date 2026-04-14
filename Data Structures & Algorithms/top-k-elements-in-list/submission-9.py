class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums))]
        my_map = {}
        res = []

        for item in nums:
            my_map[item] = my_map.get(item, 0)+1
       
        for key, value in my_map.items():
            buckets[value-1].append(key)
        
        counter = 0
        for i in range(len(buckets)-1, -1, -1):
            if buckets[i] and counter < k:
                for j in buckets[i]:
                    if counter < k:
                        res.append(j)
                        counter+=1

        return res