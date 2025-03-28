from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right, left = len(nums) - 1, 0
        while right >= left:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            elif nums[right] < nums[mid]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
            

