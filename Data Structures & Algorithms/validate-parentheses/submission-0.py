class Solution:
    def isValid(self, s: str) -> bool:
        validMap = {
            "}":"{",
            ")":"(",
            "]":"["
        }
        stack = []
        for item in s:
            if item in validMap and stack:
                queueItem = stack.pop()
                if queueItem != validMap[item]:
                    return False
            else:
                stack.append(item)
        return len(stack)==0
