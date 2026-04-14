class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res: List[List[str]] = []
        my_map={}

        def getValue(s: str):
            return ord(s) - ord("a")

        for word in strs:
            key = [0]*26 
            for letter in word:
                index = getValue(letter)
                key[index]+=1
            key = tuple(key)
            if key in my_map:
                my_map[key].append(word)
            else:
                my_map[key] = [word]

        for index, value in my_map.items():
            res.append(value)

        return res 
