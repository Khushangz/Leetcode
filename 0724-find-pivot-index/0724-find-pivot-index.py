import numpy as np
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tot=np.sum(nums)
        t=0
        if len(nums)==1:
            return 0
        flag=0
        for i in range(len(nums)):
            if t*2 ==tot-nums[i]:
                flag==1
                return i
                break
            t=t+nums[i]
        if flag==0:
            return -1
