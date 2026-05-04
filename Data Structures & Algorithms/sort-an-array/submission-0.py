class Solution:
    def mergeSorted(self, nums1, nums2):
        merged = []
        if not nums1: return nums2
        if not nums2: return nums1

        i1, i2 = 0, 0
        n1, n2 = len(nums1), len(nums2)
        while i1 < n1 and i2 < n2:
            if nums1[i1] <= nums2[i2]:
                merged.append(nums1[i1])
                i1+=1
            else:
                merged.append(nums2[i2])
                i2+=1

        if i1 == n1 and i2 == n2:
            return merged
        elif i1 == n1:
            merged.extend(nums2[i2:])
            return merged
        else:
            merged.extend(nums1[i1:])
            return merged

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        
        n = len(nums)
        m = n // 2
        nums1 = self.sortArray(nums[:m])
        nums2 = self.sortArray(nums[m:])
        return self.mergeSorted(nums1, nums2)
        