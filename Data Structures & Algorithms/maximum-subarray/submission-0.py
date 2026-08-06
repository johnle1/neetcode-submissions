class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) ==1  :
            return nums[0]

        curr = 0
        max_sum = nums[0] 
        for n in nums:
            if curr < 0:
                curr = 0 
            curr += n
            max_sum = max(max_sum,curr)
        return max_sum

        