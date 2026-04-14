class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = []
        columns = []
        squares = []

        for r in range(len(board)):
            for c in range(len(board)):
                value = board[r][c]

                if value == ".":
                    continue

                if (r, value) in rows:
                    return False
                else:
                    rows.append((r, value))

                if (c, value) in columns:
                    return False
                else:
                    columns.append((c, value))
                
                if (r // 3, c // 3, value) in squares:
                    return False
                else:
                    squares.append((r // 3, c // 3, value))

        return True