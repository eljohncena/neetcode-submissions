class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for number in range(len(nums)):
            if nums[number] != val:
                nums[k] = nums[number]
                k += 1
        return k
        

                