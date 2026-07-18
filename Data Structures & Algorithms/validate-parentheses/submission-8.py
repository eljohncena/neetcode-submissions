class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapyMap = {
            ")":"(" , "}": "{" , "]": "["
        }

        for character in s:
            if character in mapyMap:
                if stack and stack[-1] == mapyMap[character]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(character)

        return True if not stack else False