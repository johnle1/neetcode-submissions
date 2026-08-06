class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        jump_count = 0
        l = r =0
        while r < len(nums) -1:
            farthest = 0 
            for i in range(l,r+1):
                farthest = max(farthest, i + nums[i])
            l = r+1
            r = farthest
            jump_count += 1
        return jump_count

            