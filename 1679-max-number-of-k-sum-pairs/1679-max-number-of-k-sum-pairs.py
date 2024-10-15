class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=0
        r=len(nums)-1
        count=0
        while r>l:
            if nums[l]+nums[r]==k:
                nums[l]="s"
                nums[r]="s"
                count+=1
                r=r-1
                l=l+1
            else:
                if nums[l]+nums[r]<k:
                    l+=1
                else:
                    r-=1
        return count

        