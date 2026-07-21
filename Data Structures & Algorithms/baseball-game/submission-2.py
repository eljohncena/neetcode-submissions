class Solution:
    def calPoints(self, operations: List[str]) -> int:
        basketStack = []

        for operation in operations:
            if operation == "+":
                basketStack.append(basketStack[-1] + basketStack[-2])
            elif operation == "D":
                basketStack.append(2 * basketStack[-1])
            elif operation == "C":
                basketStack.pop()
            else:
                basketStack.append(int(operation))
        return sum(basketStack)
