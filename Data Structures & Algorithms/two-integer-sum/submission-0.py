class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums):
            if (i != j and target == num1 + num2):
                return [i, j]
