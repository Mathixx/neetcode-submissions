class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            target = -nums[i]
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append([nums[i],nums[l], nums[r]])
                    l+=1
                    r-=1
                    while  l < r and nums[l-1] == nums[l]:
                        l += 1
                    while r > l and nums[r+1] == nums[r]:
                        r -= 1
        
        return res
                
            

        