class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        print('nums1',nums1, nums1[0], m)
        if m==0:
            print(type(nums1),nums1[0])
            for i in range(n):
                nums1[i]=nums2[i] 
        elif m!=0 and n!=0:
            i=m-1
            last=m+n-1
            for j in range(n-1,-1,-1):
                while(i>=0):
                    if nums2[j]>nums1[i]:
                        nums1[last]=nums2[j]
                        last=last-1
                        break
                    elif nums2[j]<=nums1[i]:
                        nums1[last]=nums1[i]
                        #nums1[i]=nums2[j]
                        i=i-1
                        last=last-1
                
                # copying leftover elements from nums2 to nums1
                if j>=0 and i<0:
                    nums1[0:j+1]=nums2[0:j+1]



                        
                        