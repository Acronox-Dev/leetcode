class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        memo = {}

        def jump_at_index(i: int) -> int:
            if i >= n - 1:
                return 0

            if i in memo:
                return memo[i]

            min_jumps = float('inf')
            for j in range(1, min(nums[i], n - 1 - i) + 1):
                min_jumps = min(min_jumps, 1 + jump_at_index(i + j))

            memo[i] = min_jumps
            return memo[i]

        return jump_at_index(0)