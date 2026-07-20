class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        def aux(start : int, end : int) :
            if start == end : return nums[start]

            # Divide (Left sum and Right sum)
            m = (start + end) // 2
            s_l = aux(start, m)
            s_r = aux(m + 1, end)

            # Middle case
            current_sum = 0

            prefix_sum = float('-inf')
            for i in range(m, start - 1, -1) :
                current_sum += nums[i]
                if current_sum > prefix_sum :
                   prefix_sum = current_sum

            current_sum = 0
            suffix_sum = float('-inf')
            for i in range(m + 1, end + 1) :
                current_sum += nums[i]
                if current_sum > suffix_sum :
                    suffix_sum = current_sum

            s_m = prefix_sum + suffix_sum

            return max(s_l,s_m,s_r)

        return aux(0, len(nums) - 1) # type: ignore