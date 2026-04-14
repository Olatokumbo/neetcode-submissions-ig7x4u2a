class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitizedlist = []
        for letter in s:
            if letter.isalnum():
                sanitizedlist.append(letter)
        
        p1, p2 = 0, len(sanitizedlist)-1

        while p2>p1:
            if sanitizedlist[p2].lower() != sanitizedlist[p1].lower():
                return False
            p2-=1
            p1+=1
        
        return True
