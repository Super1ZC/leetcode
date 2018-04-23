class Solution:
    """The first solution that I made it without seeing any other solutions."""
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = sorted(nums1+nums2)
        #There are two special case need to be considered here.
        if len(nums3) == 0:
            return []
        if len(nums3) == 1:
            return nums3[0]
        else:
            #This divmod function works well for this test.
            a,b = divmod(len(nums3),2)
            if b != 0:
                result = nums3[a]
            else:
                result = (nums3[a]+nums3[a-1])/2
            return result


if __name__=='__main__':
    n1 = [1,3,5]
    n2 = [4,6,11]
    s = Solution()
    print(s.findMedianSortedArrays(n1,n2))
    
