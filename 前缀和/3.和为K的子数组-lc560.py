# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
#
# 子数组是数组中元素的连续非空序列。


'''
思路：考虑前缀和 + 哈希表，哈希表中 key = 前缀和, value = 这个前缀和出现的次数, 哈希表要初始化为{0:1}————为什么需要这个？当整个前缀和等于k时（如[1,2,3]中k=6），需要cur_sum - k = 0的计数
'''

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 用哈希表优化前缀和
        hash_table = {0: 1}
        cur_sum = 0
        ans = 0

        for num in nums:
            cur_sum += num
            if cur_sum - k in hash_table:
                ans += hash_table[cur_sum - k]

            hash_table[cur_sum] = hash_table.get(cur_sum, 0) + 1

        return ans