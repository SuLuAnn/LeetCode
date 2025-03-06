from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        r, l = 0, len(nums) - 1
        while r < l:
            mid = (r + l) // 2
            if nums[mid] > nums[l]:
                r = mid + 1
            elif nums[mid] < nums[l] and (mid == 0 or nums[mid - 1] > nums[mid]):
                return nums[mid]
            else:
                l = mid - 1
        return nums[r]
    
if __name__ == "__main__":
    solution = Solution()
    result = solution.findMin([3,4,5,1,2])
    print(result)
