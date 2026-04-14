class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False;   
        
        store = {}
        for item in s:
            store[item] = store.get(item, 0)+1

        for item in t:
            if item not in store:
                return False
            store[item]-=1

            if store[item] < 0:
                return False
        
        for _, value in store.items():
            if value  != 0:
                return False

        return True
