class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False

        map1 = {}
        map2 = {}
        for item in s:
            map1[item] = map1.get(item, 0)+1

        for item in t:
            map2[item] = map2.get(item, 0)+1
        
        for item in map1:
            if map1.get(item) != map2.get(item):
                return False

        return True