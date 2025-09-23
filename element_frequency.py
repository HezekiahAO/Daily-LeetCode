from typing import List

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = len(set(nums))
        return counts

sol = Solution()
print(sol.maxFrequencyElements([1,1,1,2,3,4,3]))
print(sol.maxFrequencyElements([1,1,2,4,3,5]))