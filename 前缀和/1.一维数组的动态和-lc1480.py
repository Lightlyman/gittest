# 给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。
#
# 请返回 nums 的动态和。

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 前缀和
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        for i in range(1, len(prefix)):
            prefix[i] = prefix[i - 1] + nums[i]
        return prefix