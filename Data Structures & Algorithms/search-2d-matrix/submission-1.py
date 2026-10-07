class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l = 0
        r = len(matrix) - 1

        while l <= r:
            mid = (r - l) // 2 + l
            if matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][-1] < target:
                l = mid + 1
            else:
                break

        if not l<= r:
            return False
        
        row = matrix[mid]

        l = 0
        r = len(row) - 1
        while l <= r:
            mid = (r - l) // 2 + l
            if row[mid] == target:
                return True
            elif row[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False



        