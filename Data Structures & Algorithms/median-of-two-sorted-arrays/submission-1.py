class Solution:
    def validCut(self, nums1: List[int], nums2: List[int], cut1: int):
        # Return Valid, tooHigh?
        n1, n2 = len(nums1), len(nums2)
        cut2 = (n1+n2+1)//2 - cut1

        if cut1-1 > -1 and cut2 < n2 and nums1[cut1-1] > nums2[cut2]:
            return (False, True)
        if cut2-2 > -1 and cut1 < n1 and nums2[cut2-1] > nums1[cut1]:
            return (False, False)
        return (True, None)

    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        n1, n2 = len(nums1), len(nums2)
        
        l, r = 0, n1
        while l < r:
            mid = (l+r)//2
            valid, tooHigh = self.validCut(nums1, nums2, mid)
            if valid:
                break
            else:
                if tooHigh:
                    r = mid
                else:
                    l = mid+1
        
        cut1 = (l+r)//2
        cut2 = (n1+n2+1)//2 - cut1

        l1 = nums1[cut1-1] if cut1 > 0 else float("-inf")
        r1 = nums1[cut1] if cut1 < n1 else float("+inf")
        l2 = nums2[cut2-1] if cut2 > 0 else float("-inf")
        r2 = nums2[cut2] if cut2 < n2 else float("+inf")

        left_el = max(l1, l2)
        right_el = min(r1, r2)

        d, r = divmod(n1+n2, 2)
        if r == 1:
            return left_el if cut1+cut2 > d else right_el
        else:
            return (left_el+right_el) / 2.0


        
        
        