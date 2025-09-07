# 给定一个区间的集合 intervals ，其中 intervals[i] = [starti, endi] 。返回 需要移除区间的最小数量，使剩余区间互不重叠 。
#
# 注意 只在一点上接触的区间是 不重叠的。例如 [1, 2] 和 [2, 3] 是不重叠的。

'''

以区间结束节点排序，排序后判断后面区间的起始点是否大于等于当前维护区间，如果是就更新

'''

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        sort_val = sorted(intervals, key=lambda x: x[1])
        end = -float('inf')
        choose = 0
        for interval in sort_val:
            if interval[0] >= end:
                choose += 1
                end = interval[1]

        return len(intervals) - choose