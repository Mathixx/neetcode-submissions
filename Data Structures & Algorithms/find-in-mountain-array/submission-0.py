class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # First bs for finding peak
        n = mountainArr.length()
        l, r = 0, n-1
        pivot = -1
        while l <= r:
            mid = (l+r) // 2
            mid_val = mountainArr.get(mid)
            premid_val = mountainArr.get(mid-1)
            postmid_val = mountainArr.get(mid+1)
            if premid_val < mid_val < postmid_val:
                l = mid+1
            elif premid_val > mid_val > postmid_val:
                r = mid-1
            else:
                pivot = mid
                break

        assert pivot != -1

        # Then 2 bs for checking if target in one of 2 slopes
        # First check left one cause we want min
        l, r = 0, pivot
        while l<=r:
            mid = (l+r) // 2
            mid_val = mountainArr.get(mid)
            if mid_val < target:
                l = mid+1
            elif mid_val > target:
                r = mid-1
            else:
                return mid
        
        l, r = pivot+1, n-1
        while l<=r:
            mid = (l+r) // 2
            mid_val = mountainArr.get(mid)
            if mid_val < target:
                r = mid-1
            elif mid_val > target:
                l = mid+1
            else:
                return mid
        
        return -1

        