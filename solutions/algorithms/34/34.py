class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # Find left (Search between i and j)
        def findLeft(i : int, j : int) :
            if not nums or (i == j and nums[i] != target) : return -1
            if i == j and nums[i] == target : return i

            middle = (i + j) // 2
            value = nums[middle]

            if value == target :
                temp = findLeft(i,middle)
                if temp != -1 :
                    return temp
                return middle
            
            elif value < target :
                return findLeft(middle + 1, j)
            
            else :
                return findLeft(i, middle)
                
        # Find right
        def findRight(i : int, j : int) :
            if not nums or (i == j and nums[i] != target) : return -1
            if i == j and nums[i] == target : return i

            middle = (i + j) // 2
            value = nums[middle]

            if value == target :
                temp = findRight(middle + 1, j)
                if temp != -1 :
                    return temp
                return middle
            
            elif value < target :
                return findRight(middle + 1, j)
            
            else :
                return findRight(i, middle)
            
        # Solution
        n = len(nums)
        v1 = findLeft(0,n-1)
        v2 = findRight(0,n-1)

        return [v1,v2]