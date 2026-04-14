class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = {}
        res = []

        for word in strs:
            key = [0]*26
            for letter in word:
                index = ord(letter) - ord("a")
                key[index]+=1
            my_map[tuple(key)] = my_map.get(tuple(key), [])
            my_map[tuple(key)].append(word)
        for key, value in my_map.items():
           res.append(value)
        return res