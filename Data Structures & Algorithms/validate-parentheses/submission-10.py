class Solution:
    def isValid(self, s: str) -> bool:
        valid = []

        my_map = {
            "}":"{",
            ")":'(',
            "]":"["
        }

        for item in s:
            if item in my_map:
                if valid and valid[-1]==my_map[item]:
                    valid.pop()
                else:
                    return False
            else:
                valid.append(item)

        return len(valid)==0
        
        



