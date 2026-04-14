class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_map = {}

        for letter in s:
            my_map[letter] = my_map.get(letter, 0)+1
        
        for letter in t:
            if letter in my_map:
                new_value = my_map[letter]-1
                if new_value <0:
                    return False
                else:
                    my_map[letter] = new_value
            else:
                return False

        for i in my_map.keys():
            if my_map[i] !=0:
                return False

        return True 
