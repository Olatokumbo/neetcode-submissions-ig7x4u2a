class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        my_map = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        for item in s:
            if item in my_map:
                if stack and stack[len(stack)-1]==my_map[item]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(item)
    
        return len(stack)==0 