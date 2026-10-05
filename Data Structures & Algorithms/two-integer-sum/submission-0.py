class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        position = {}
        for i,num in enumerate(nums):
            if target - num in position:
                return [position[target - num ], i]
            position[num] = i    
        