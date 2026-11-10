class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2

        if len(nums1) > len(nums2):
            a, b = nums2, nums1
        
        total = len(a) + len(b)
        half = total // 2

        left = 0
        right = len(a) - 1

        while True:
            i = (right - left) // 2 + left
            # half = (i+1)+(j+1)
            j = half - i - 2

            leftA = a[i] if i >= 0 else float("-inf")
            rightA = a[i + 1] if i + 1 < len(a) else float("inf")
            leftB = b[j] if j >= 0 else float("-inf")
            rightB = b[j + 1] if j + 1 < len(b) else float("inf")

            if leftA <= rightB and leftB <= rightA:
                if total % 2:
                    return min(rightA, rightB)
                return (min(rightA, rightB) + max(leftA, leftB)) / 2
            elif leftA > rightB:
                right = i - 1
            else:
                left = i + 1



