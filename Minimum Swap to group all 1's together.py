class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums, 1)
        if n == 0:
            return 0
        if n == 