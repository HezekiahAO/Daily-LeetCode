class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        total_ones = sum(nums)
        
        # Edge cases: no ones or all ones
        if total_ones == 0 or total_ones == n:
            return 0
        
        # Duplicate array to handle circularity    # when 1 and 1 are adjacent at the end and start of the array this shows the circular property of an array.
        arr = nums + nums
        
        # Initial window of length total_ones
        current_ones = sum(arr[:total_ones])
        max_ones = current_ones
        
        # Slide the window over the first n starting positions
        for start in range(1, n):
            # Remove the element leaving the window
            current_ones -= arr[start - 1]
            # Add the new element entering the window
            current_ones += arr[start + total_ones - 1]
            max_ones = max(max_ones, current_ones)
        
        # Minimum swaps = zeros inside the best window
        return total_ones - max_ones