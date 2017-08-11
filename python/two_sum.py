# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# place in dictionary to be looked up later

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for idx, num in enumerate(nums):
        	nums_dict[num] = idx
        for idx, num in enumerate(nums):
        	print idx
        	if (target-num in nums_dict.keys() and idx != nums_dict[target-num]):
        		return [idx, nums_dict[target-num]]

# TEST
s = Solution()
nums = [2, 7, 11, 15]
target = 9
nums1 = [2, 5, 5, 11]
target1 = 10
nums2 = [3, 3]
target2 = 6
print s.twoSum(nums, target) # print [0, 1]
print s.twoSum(nums1, target1) # print [1, 2]
print s.twoSum(nums2, target2) # print [0, 1]
