class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        symbols=["+", "-", "*", "/"]
        stack = []

        for item in tokens:
            if item in symbols:
                num2 = int(stack.pop())
                num1 = int(stack.pop())

                if item == '+':
                    total = num1+num2
                    stack.append(total)
                elif item == '-':
                    total = num1-num2
                    stack.append(total)
                elif item =="*":
                    total=num1*num2
                    stack.append(total)
                elif item=="/":
                    total=int(num1/num2)
                    stack.append(total)
            else:
                stack.append(int(item))
                
        return stack[-1]