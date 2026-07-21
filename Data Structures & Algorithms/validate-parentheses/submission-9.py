class Solution:
    def isValid(self, s: str) -> bool:
        validMap = {")": "(", "]": "[", "}": "{"}
        stack = []
        for bracket in s:
            if bracket in validMap:
                if stack and stack[-1] == validMap[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        return True if not stack else False
