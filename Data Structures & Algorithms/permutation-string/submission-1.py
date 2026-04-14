class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
            
        s1Window = [0]*26
        countWindow = [0]*26
        
        for i in s1:
            s1Window[ord(i) -  ord("a")]+=1
        
        k = len(s1)

        for i in range(k):
            countWindow[ord(s2[i]) -  ord("a")]+=1
        
        if s1Window==countWindow:
            return True
        
        for i in range(k, len(s2)):
            countWindow[ord(s2[i]) - ord("a")]+=1
            countWindow[ord(s2[i-k]) - ord("a")]-=1

            if countWindow==s1Window:
                return True

        return False
        

