from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)

        def merge_sort(left: int, right: int):
            if left >= right:
                return

            mid = (left + right) // 2
            merge_sort(left, mid)
            merge_sort(mid + 1, right)

            i, j, k = left, mid + 1, left
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    result [k] = nums[i]
                    i += 1
                else:
                    result [k] = nums[j]
                    j += 1
                k += 1

            while i <= mid:
                result [k] = nums[i]
                i += 1
                k += 1

            while j <= right:
                result [k] = nums[j]
                j += 1
                k += 1

            nums[left : right + 1] = result [left : right + 1]

        merge_sort(0, len(nums) - 1)
        return nums