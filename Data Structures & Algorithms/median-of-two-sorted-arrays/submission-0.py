class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        a, b = nums1, nums2

        if len(a) > len(b):
            a, b = b, a
            
        size = len(a) + len(b)
        half = size // 2
        
        left = 0
        right = len(a) - 1
        
        while True:
            mid = (left + right) // 2
            i = mid
            j = half - mid - 2

            lefta_end = a[i] if i >= 0 else float("-inf")
            righta_start = a[i + 1] if (i + 1) < len(a) else float("inf")
            leftb_end = b[j] if j >= 0 else float("-inf")
            rightb_start = b[j + 1] if (j + 1) < len(b) else float("inf")

            # Check if partition is correct
            if lefta_end <= rightb_start and leftb_end <= righta_start:
                # Odd length: the extra element is the smallest on the right side
                if size % 2:
                    return float(min(righta_start, rightb_start))
                # Even length: average of the two middle elements
                return (max(lefta_end, leftb_end) + min(righta_start, rightb_start)) / 2.0
            
            elif lefta_end > rightb_start:
                right = mid - 1
            else:
                left = mid + 1