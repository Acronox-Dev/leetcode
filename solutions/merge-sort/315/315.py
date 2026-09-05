class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = [ 0 for _ in range(n) ]

        def mergeSort(array: List[int]) :
            if len(array) <= 1 : return array

            # Split and recursion
            m = len(array) // 2
            left = mergeSort(array[:m])
            right = mergeSort(array[m:])

            # Fuse
            i, j = 0, 0
            while (i < len(left) and j < len(right)) :
                if left[i][0] <= right[j][0] :
                    count[left[i][1]] += j
                    i += 1
                else :
                    j += 1
            while i < len(left) :
                count[left[i][1]] += j

                i += 1

        result = m
        return count

?