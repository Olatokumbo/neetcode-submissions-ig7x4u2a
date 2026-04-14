class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = {}

        def converter(s: str):
            return ord("a") - ord(s)
        
        for word in strs:
            key = [0]*26
            for letter in word:
                key[converter(letter)]+=1
            if tuple(key) in my_map:
                my_map[tuple(key)].append(word)
            else:
                 my_map[tuple(key)] = [word]
        return [v for _, v in my_map.items()]
