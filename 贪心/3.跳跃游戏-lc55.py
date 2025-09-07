# 给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。
class Solution(object):
    def canJump(self, nums):
        # 先试试动态规划
        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # for i in range(len(nums)):
        #     if dp[i-1] < i:
        #         return False
        #     dp[i] = max(dp[i-1],nums[i] + i)
        # return True

        # 用贪心试试
        max_jump = 0
        for i in range(len(nums)):
            max_jump = max(max_jump, i + nums[i])
            if nums[i] == 0 and max_jump <= i:
                break

        return True if max_jump >= len(nums) - 1 else False