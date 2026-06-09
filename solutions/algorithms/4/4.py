# To find the median :
# - Fuse the arrays,
# - Merge sort 
# - Calculate and return the median

class Solution:
    def mergeSort(self, nums: List[int]) -> List[int]:
        n = len(nums)

        if (not nums or n <= 1) : return nums

        # Split the array and sort        
        d = n // 2
        part1 = self.mergeSort(nums[:d])
        part2 = self.mergeSort(nums[d:])

        # Fusion
        i = 0
        j = 0
        n1 = len(part1)
        n2 = len(part2)

        sorted_nums = [0 for i in range(n)]
        while(i < n1 and j < n2) :
            vi, vj = part1[i], part2[j]
            if(vi < vj) :
                sorted_nums[i+j] = vi
                i += 1
            else :
                sorted_nums[i+j] = vj
                j += 1

        while(i < n1) :
            sorted_nums[i+j] = part1[i]
            i += 1
        while(j < n2) :
            sorted_nums[i+j] = part2[j]
            j += 1

        return sorted_nums

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if (not nums1 and not nums2) : return 0.0

        nums = nums1 + nums2

        nums = self.mergeSort(nums)

        n = len(nums)
        d = n // 2
        if (n % 2 == 1) :
            return nums[d]
        else :
            return (nums[d - 1] + nums[d]) / 2 