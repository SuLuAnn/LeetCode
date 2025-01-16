class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero_count = 0
        for num in nums:
            if num != 0:
                total *= num
            else:
                zero_count += 1
        if zero_count > 1:
            return [0] * len(nums)
        elif zero_count == 1:
            return [ total if num == 0 else 0 for num in nums]
        else:
            return [total // num for num in nums]   