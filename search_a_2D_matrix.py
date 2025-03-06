from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        length_r, length_l = 0, len(matrix)-1
        length = 0
        width = 0
        while length_l >= length_r :
            mid = (length_r + length_l) // 2
            if matrix[mid][0] <= target and (mid == len(matrix)-1 or matrix[mid+1][0] > target):
                length = mid
                break
            if matrix[mid][0] > target:
                length_l = mid - 1
            else:
                length_r = mid + 1
        
        width_r, width_l = 0, len(matrix[0])-1

        while width_l >= width_r :
            mid = (width_r + width_l) // 2
            if matrix[length][mid] == target:
                width = mid
                break
            if matrix[length][mid] > target:
                width_l = mid - 1
            else:
                width_r = mid + 1
        return matrix[length][width] == target

if __name__ == "__main__":
    solution = Solution()
    result = solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)
    print(result)