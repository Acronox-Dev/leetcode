class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Initialization
        n = len(candidates)

        # Recursivity
        def combinationSumRecursive(i : int, target : int) :
            if target < 0 : return []
            if i >= n : return [[]] if target == 0 else []

            c = candidates[i]
            res1 = combinationSumRecursive(i + 1, target)
            res2 = combinationSumRecursive(i, target - c)

            result = []
            if res1 != [] :
                for r in res1 :
                    result.append(r)
            if res2 != [] :
                for r in res2 :
                    result.append([c] + r)

            return result

        return combinationSumRecursive(0,target)