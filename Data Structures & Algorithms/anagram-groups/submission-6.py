class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bucket = {}

        def getNum(letter: str):
            return ord("a") - ord(letter)
        
        for word in strs: 
            key = [0]*26
            for letter in word:
                key[getNum(letter)]+=1
            key = tuple(key)
            if key in bucket:
                bucket[key].append(word)
            else:
                bucket[key] = [word]

        return list(bucket.values())