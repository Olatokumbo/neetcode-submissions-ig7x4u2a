class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(s):
            return False

        count = {}

        for letter in s:
            count[letter] = count.get(letter, 0)+1
        
        for letter in t:
            if letter not in count:
                return False
            else:
                count[letter]-=1
        
        for _, value in count.items():
            if value != 0:
                return False
            
        return True