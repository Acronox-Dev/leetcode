from typing import List

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        array = [0] * len(nums1)
        for i in range(len(nums1)):
            array[i] = nums1[i] - nums2[i]

        result = [0] * len(nums1)

        def merge_sort(left: int, right: int) -> int:
            if left >= right:
                return 0
        
            mid = (left + right) // 2
            count = merge_sort(left, mid) + merge_sort(mid + 1, right)
        
            # Count the pairs
            j = mid + 1
            for i in range(left, mid + 1):
                while j <= right and array[i] > array[j] + diff:
                    j += 1
                count += (right - j + 1)
        
            # Merge
            i, k = left, left
            j = mid + 1
        
            while i <= mid and j <= right:
                if array[i] <= array[j]:
                    result[k] = array[i]
                    i += 1
                    k += 1
                else:
                    result[k] = array[j]
                    j += 1
                    k += 1
        
            while i <= mid:
                result[k] = array[i]
                i += 1
                k += 1
        
            while j <= right:
                result[k] = array[j]
                j += 1
                k += 1
        
            array[left : right + 1] = result[left : right + 1]
        
            return count
        
        return merge_sort(0, len(nums1) - 1)