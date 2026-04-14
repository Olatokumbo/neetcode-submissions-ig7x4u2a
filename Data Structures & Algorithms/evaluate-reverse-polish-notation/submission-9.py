class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["*", "+", "-", "/"]

        for item in tokens:
            if item not in operators:
                stack.append(int(item))
            else:
                value = 0
                v1 = stack.pop()
                v2 = stack.pop()

                if item =="*":
                    value = v1*v2
                elif item =="+":
                    value = v1+v2
                elif item =="-":
                    value = v2-v1
                elif item == "/":
                    value = int(v2/v1)
                stack.append(value)

        return int(stack[0])