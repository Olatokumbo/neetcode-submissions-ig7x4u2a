class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_map = {}

        for letter in s:
            my_map[letter] = my_map.get(letter, 0)+1
        
        for letter in t:
            if letter not in my_map:
                return False
            my_map[letter] = my_map[letter]-1
        
        for item in my_map:
            if my_map[item] !=0:
                return False
        return True