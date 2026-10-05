class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = {}
        for i,num in enumerate(nums) :
            if num not in temp:
                temp[num] = i
            else :
                return True
        return False

        