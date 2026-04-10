class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range (n):
            for j in range (n-1-i):
                if nums[j] > nums[j+1]:
                   nums[j], nums[j+1] = nums[j+1], nums[j]
                   swapped = True
            if not swapped:
                break
        return nums

# Input: nums = [5,2,3,1]
#Output: [1,2,3,5]
#Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).