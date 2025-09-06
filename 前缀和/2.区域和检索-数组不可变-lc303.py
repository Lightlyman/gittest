# 给定一个整数数组  nums，处理以下类型的多个查询:
#
# 计算索引 left 和 right （包含 left 和 right）之间的 nums 元素的 和 ，其中 left <= right
# 实现 NumArray 类：
#
# NumArray(int[] nums) 使用数组 nums 初始化对象
# int sumRange(int i, int j) 返回数组 nums 中索引 left 和 right 之间的元素的 总和 ，包含 left 和 right 两点（也就是 nums[left] + nums[left + 1] + ... + nums[right] )

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.prefix = [0] * len(nums)
        self.prefix[0] = nums[0]
        for i in range(1, len(self.prefix)):
            self.prefix[i] = self.prefix[i - 1] + nums[i]

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.prefix[right] - self.prefix[left] + self.nums[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)