from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        r, l = 0, len(nums) - 1
        while r < l:
            mid = (r + l) // 2
            if nums[mid] > nums[l]:
                r = mid + 1
            else:
                l = mid
        return nums[r]
    
if __name__ == "__main__":
    solution = Solution()
    result = solution.findMin([3,4,5,1,2])
    print(result)
