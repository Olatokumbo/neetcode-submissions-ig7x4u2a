class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        my_map = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        for item in s:
            if item not in my_map.keys():
                stack.append(item)
            else:
                if stack and stack[len(stack)-1]==my_map[item]:
                    stack.pop()
                else:
                    return False

        return len(stack)==0