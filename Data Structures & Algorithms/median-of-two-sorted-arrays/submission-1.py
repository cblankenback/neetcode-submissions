class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        if len(nums2) < len(nums1):
            a, b = nums2, nums1
        left = 0
        right = len(a) - 1
        half = (len(a) + len(b)) // 2

        while True:
            i = (right - left) // 2 + left
            j = half - i - 2

            leftA = a[i] if i >= 0 else float("-inf")
            rightA = a[i + 1] if i + 1 < len(a) else float("inf")
            leftB = b[j] if j >= 0 else float("-inf")
            rightB = b[j + 1] if j + 1 < len(b) else float("inf")

            if leftA <= rightB and leftB <= rightA:
                if (len(nums1)+len(nums2)) % 2:
                    return min(rightB, rightA)
                return (min(rightB, rightA) + max(leftA, leftB)) / 2
            elif leftA > rightB:
                right = i - 1
            else:
                left = i + 1
