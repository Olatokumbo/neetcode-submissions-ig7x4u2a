class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        columns = set()
        squares = set()

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == ".":
                    continue

                if (r, value) in rows or (c, value) in columns or ((r//3, c//3), value) in squares:
                    return False
                else:
                    rows.add((r, value))
                    columns.add((c, value))
                    squares.add(((r//3, c//3), value ))
        return True   