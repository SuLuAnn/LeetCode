from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column_store = [[False] * 10 for _ in range(10)]
        row_store = [[False] * 10 for _ in range(10)]
        box_store = [[False] * 10 for _ in range(10)]
        for column in range(9):
            for row in range(9):
                boxes = board[column][row]
                if boxes == ".":
                    continue
                index = int(boxes)
                if column_store[column][index]:
                    return False
                column_store[column][index] = True
                if row_store[row][index]:
                    return False
                row_store[row][index] = True
                if box_store[(column // 3) * 3 + row // 3][index]:
                    return False
                box_store[(column // 3) * 3 + row // 3][index] = True
        return True
    
if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    print(Solution().isValidSudoku(board))
