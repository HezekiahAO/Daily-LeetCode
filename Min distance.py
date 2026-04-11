class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        index_map = {}
        min_dist = float('inf')

        for i, num in enumerate(nums):          #enumerate used to get both index and value

            if num in index_map:            #in Used to check existance of num in index_map
                index_map[num].append(i)

                if len(index_map[num]) >= 3:
                    current_dist = 2 * (index_map[num][-1] - index_map[num][0])
                    min_dist = min(min_dist, current_dist)
            else:
                index_map[num] = [i]
        if min_dist == float('inf'):
            return -1

        return min_dist