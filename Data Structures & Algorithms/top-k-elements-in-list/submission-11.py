class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = {}
        bucket = [[] for _ in range(len(nums)+1)]
        res = []

        for value in nums:
            my_map[value] = my_map.get(value, 0)+1
        
        for key, value in my_map.items():
            bucket[value].append(key)

        counter = 0
        for index in range(len(bucket)-1, -1, -1):
            if bucket[index] != []:
                for value in bucket[index]:
                    if counter <k:
                        res.append(value)
                        counter+=1
                    else:
                        break
        return res