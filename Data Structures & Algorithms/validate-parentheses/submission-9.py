class Solution:
    def isValid(self, s: str) -> bool:

        if len(s)<2:
            return False

        stack = []

        my_map = {
            "}":"{",
            "]":"[",
            ")":"("
        }

        for item in s:
            if item in my_map and stack:
                pop = stack.pop()
                if my_map[item]!=pop:
                    return False
            else:
                stack.append(item)
        
        return len(stack)==0
