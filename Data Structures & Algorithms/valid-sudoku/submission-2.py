class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        columns = set()
        squares = set()

        for row in range(9):
            for column in range(9):
                value  = board[row][column]
                if value != ".":
                    if (value, row) in rows:
                        return False
                    rows.add((value, row))
                    if (value, column) in columns:
                        return False
                    columns.add((value, column))

                    if (value, row//3, column//3) in squares:
                        return False
                    squares.add((value, row//3, column//3))
        return True
