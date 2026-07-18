class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = count = 0

        for number in nums:
            if number == 0:
                maxCount = max(maxCount,count)
                count = 0
            else:
                count += 1

        return max(maxCount,count)