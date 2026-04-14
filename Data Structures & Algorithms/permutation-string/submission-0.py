class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        s1Count = [0]*26
        windowCount = [0]*26

        for letter in s1:
            s1Count[ord(letter)-ord("a")]+=1
        
        k = len(s1)

        for i in range(k):
            windowCount[ord(s2[i])-ord("a")]+=1
        
        if windowCount==s1Count:
            return True
        
        for i in range(k, len(s2)):
            windowCount[ord(s2[i])-ord("a")]+=1
            windowCount[ord(s2[i-k])-ord("a")]-=1

            if windowCount == s1Count:
                return True

        return False