class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_map = {}
        for item in s:
            my_map[item] = my_map.get(item, 0)+1
        
        for item in t:
            if item not in my_map:
                return False
            else:
                my_map[item]-=1
                if my_map[item]<0:
                    return False
        
        for index, value in my_map.items():
            if value !=0:
                return False
        return True
