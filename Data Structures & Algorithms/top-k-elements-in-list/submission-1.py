class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        freq_map = {}

        for num in nums:
            freq_map[num] = freq_map.get(num, 0)+1

        bucket = [[] for _ in range(len(nums)+1)]
        
        for n, c in freq_map.items():
            bucket[c].append(n)

        for i in range(len(bucket)-1, -1, -1):
            for n in bucket[i]:
                result.append(n)
                if len(result)==k:
                    return result

        return result