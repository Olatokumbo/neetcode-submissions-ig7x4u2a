class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = []
        columns = []
        squares = []

        for row in range(len(board)):
            for column in range(len(board)):
                value = board[row][column]
                if value != ".":
                    if (row, value) in rows:
                        return False
                    else:
                        rows.append((row, value))
                    
                    if (column, value) in columns:
                        return False
                    else:
                        columns.append((column, value))
                    
                    if (row //3, column//3, value) in squares:
                        return False
                    else:
                        squares.append((row//3, column//3, value))
        return True


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  