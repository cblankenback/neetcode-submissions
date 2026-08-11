class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset = defaultdict(set)
        colset = defaultdict(set)
        squareset = defaultdict(set)
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue

                if board[row][col] in rowset[row]:
                    return False
                else:
                    rowset[row].add(board[row][col])
                
                if board[row][col] in colset[col]:
                    return False
                else:
                    colset[col].add(board[row][col])
                a = math.ceil((row+1)/3)
                b =  math.ceil((col+1)/3)
                if  board[row][col] in squareset[(a, b)]:
                    return False
                else:
                    squareset[(a, b)].add(board[row][col])
                
        return True

                