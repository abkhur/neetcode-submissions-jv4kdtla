class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ansMap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in ansMap:
                return [ansMap[diff], i]
            ansMap[num] = i