class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1=set(nums1)
        nums2=set(nums2)
        k=nums1.intersection(nums2)
        nums1-=k
        nums2-=k
        k=[]
        k.append(list(nums1))
        k.append(list(nums2))


        return k
            

                