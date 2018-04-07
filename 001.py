class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i,num in enumerate(nums):
            x=target-num
            if x in nums and i!=nums.index(x):
                return sorted([i,nums.index(x)])
print(Solution().twoSum([2,7,11,15],9))

'''相关参考：http://www.runoob.com/python/python-func-sorted.html
			 https://blog.csdn.net/churximi/article/details/51648388'''