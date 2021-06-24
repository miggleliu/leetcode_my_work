class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        median = 0
        min_index = 0
        max_index = m
        left = 0
        right = 0
        
        if m == 0:
            median = nums2[(n-1)//2] if n%2 ==1 else 1/2*(nums2[n//2-1]+nums2[n//2])
            return median
        elif n == 0:
            median = nums1[(m-1)//2] if m%2 ==1 else 1/2*(nums1[m//2-1]+nums1[m//2])
            return median
            
        while min_index <= max_index:
            i = int((min_index+max_index)/2)
            j = int((m+n+1)/2)-i
            if j < 0:
                max_index -= 1
                continue
            if j > n:
                min_index += 1
                continue
            if j < n and i > 0 and nums1[i-1] > nums2[j]:
                max_index = i-1
            elif j > 0 and i < m and nums1[i] < nums2[j-1]:
                min_index = i+1
            else:
                if i == 0:
                    left = nums2[j-1]
                elif j == 0:
                    left = nums1[i-1]
                else:
                    left = max(nums2[j-1],nums1[i-1])

                if i == m:
                    right = nums2[j]
                elif j == n:
                    right = nums1[i]
                else:
                    right = min(nums2[j],nums1[i])

                if (m+n) % 2 == 0:
                    median = (left + right)/2
                else:
                    median = left
                return median

