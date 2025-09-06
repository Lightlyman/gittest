# 假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。
#
# 对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j，都有一个尺寸 s[j] 。如果 s[j] >= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是满足尽可能多的孩子，并输出这个最大数值。
# https://leetcode.cn/problems/assign-cookies/

'''

            直接贪心就行，把饼干和孩子都排序一下，尝试以最小代价来满足孩子，满足不了当前孩子就加码（j+=1）,直到孩子满足完毕或者饼干遍历完
            （此时饼干可能并没有发完，但是一个孩子只能拿一个饼干，剩下的饼干满足不了剩下的孩子）


'''
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        ans = 0
        g.sort()
        s.sort()
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                ans += 1
                i += 1
            j += 1

        return ans