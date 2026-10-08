class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bot = len(matrix) - 1
        while top <= bot:
            mid = (bot - top) // 2 + top
            
            if matrix[mid][0] > target:
                bot = mid - 1
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                break
        if not top <= bot:
            return False

        row = matrix[mid]
        l = 0
        r = len(row) - 1
        while l <= r:
            mid = (r - l) // 2 + l
            if row[mid] == target:
                return True
            elif row[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
            


            ## mid == 2
            # is 10 > 20