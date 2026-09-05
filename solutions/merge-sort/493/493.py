from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0

        result = [0] * len(nums)

        def merge_sort(left: int, right: int) -> int:
            if left >= right:
                return 0

            mid = (left + right) // 2
            count = merge_sort(left, mid) + merge_sort(mid + 1, right)

            # Count the reverse pairs
            j = mid + 1
            for i in range(left, mid + 1):
                while j <= right and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)

            # Merge
            i, k = left, left
            j = mid + 1

            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    result[k] = nums[i]
                    i += 1
                else:
                    result[k] = nums[j]
                    j += 1
                k += 1

            while i <= mid:
                result[k] = nums[i]
                i += 1
                k += 1

            while j <= right:
                result[k] = nums[j]
                j += 1
                k += 1

            nums[left : right + 1] = result[left : right + 1]

            return count

        return merge_sort(0, len(nums) - 1)