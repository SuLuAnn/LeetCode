from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column_store = [[False for i in range(10)] for i in range(10)]
        row_store = [[False for i in range(10)] for i in range(10)]
        box_store = [[False for i in range(10)] for i in range(10)]
        for column in range(len(board)):
            for row in range(len(board[0])):
                boxes = board[column][row]
                if boxes == ".":
                    continue
                print(f"have data : column: {column}, row {row}, boxes {boxes}")
                index = int(boxes)
                if column_store[column][index]:
                    print("c end")
                    return False
                column_store[column][index] = True
                if row_store[row][index]:
                    print("r end")
                    return False
                row_store[row][index] = True
                print(f"box: {(column // 3) * 3 + row // 3}")
                if box_store[(column // 3) * 3 + row // 3][index]:
                    print("b end")
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
