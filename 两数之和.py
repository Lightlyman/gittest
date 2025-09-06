# 梦开始的地方
# Hello Algorithm!
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            n = target - nums[i]
            if n in hashmap.keys():
                return [hashmap.get(n), i]
            hashmap[nums[i]] = i
        return []