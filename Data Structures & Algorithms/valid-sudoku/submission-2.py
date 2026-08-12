class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset = defaultdict(set)
        colset = defaultdict(set)
        squareset = defaultdict(set)
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue
                if board[row][col] in colset[col]:
                    return False
                else:
                    colset[col].add(board[row][col])

                if board[row][col] in rowset[row]:
                    return False
                else:
                    rowset[row].add(board[row][col])

                squareX = math.ceil((col + 1) / 3)
                squarey = math.ceil((row + 1) / 3)

                if board[row][col] in squareset[(squareX,squarey)]:
                    return False
                else:
                    squareset[(squareX,squarey)].add(board[row][col])
        return True