class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        for x in nums:
        	j = 0
        	for y in nums:
        		if x + y == target and i < j:
        			return [i+1, j+1]
        		j = j + 1
        	i = i + 1
        return None

numbers=[0,4,3,0]
target=0
sol = Solution().twoSum(numbers, target)
print(sol)