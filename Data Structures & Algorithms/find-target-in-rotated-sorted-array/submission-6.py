class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while nums[l] > nums[r]:
            mid = (l + r) // 2
            if nums[mid] >= nums[l]: 
                l = mid + 1
            else:
                r = mid

        pivot = l - 1

        if pivot == -1:
            l, r = 0, len(nums) - 1
        elif nums[0] <= target <= nums[pivot]:
            l, r = 0, pivot
        else:
            l, r = pivot + 1, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1

