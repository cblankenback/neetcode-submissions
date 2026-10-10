class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bot = len(matrix) - 1

        while top <= bot:
            mid = (bot - top) // 2 + top
            #target 1
            # mid = 10
            # shift bot
            #       10 > 1
            if matrix[mid][0] > target:
                bot = mid - 1
            # target 14
            # mid 10
            #. 10 < 14
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                break
        
        if not top <= bot:
            return False

        row = matrix[mid]
        left = 0
        right = len(row) - 1 

        while left <= right:
            mid = (right - left) // 2 + left

            if row[mid] == target:
                return True
            # mid = 11
            # target == 13
            # shift l
            # 11 < 13
            elif row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False