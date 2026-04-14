class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = {}
        for word in strs:
            key = [0]*26
            for letter in word:
                index = ord(letter) - ord("a")
                key[index]+=1
            key = tuple(key)
            if key not in my_map:
                my_map[key] = []
            my_map[key].append(word)
        return(list(my_map.values()))