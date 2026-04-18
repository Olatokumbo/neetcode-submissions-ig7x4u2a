class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []

        for index in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[index]:
                res[stack[-1]] = index - stack[-1]
                stack.pop()
            stack.append(index)

        return res