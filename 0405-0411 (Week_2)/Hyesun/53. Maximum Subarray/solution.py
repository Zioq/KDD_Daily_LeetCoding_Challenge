#https://leetcode.com/problems/maximum-subarray/
#53. Maximum Subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # maxSum = -math.inf
        # for i in range(len(nums)):
        #     curSum = 0
        #     for j in range(i, len(nums)):
        #         curSum += nums[j]
        #         maxSum = max(curSum, maxSum)
        # return maxSum
            
        maxSum = curSum = nums[0]
        for i in range(1, len(nums)):
            curSum = max(curSum + nums[i], nums[i])
            maxSum = max(curSum, maxSum)
        return maxSum 