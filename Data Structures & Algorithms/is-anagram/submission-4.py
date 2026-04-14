class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_map = {}

        for letter in s:
            my_map[letter] = my_map.get(letter, 0)+1
        
        for letter in t:
            if letter not in my_map:
                return False
            else:
                my_map[letter]-=1
        
        for key in my_map:
            if my_map[key] != 0:
                return False
        return True
