class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        fin=[]
        nums.sort()
        print(nums)
        for curr in range(len(nums)-2):
            if curr>0 and nums[curr]==nums[curr-1]:
                continue
            i=curr+1
            a=len(nums)-1
            while a>i:
                tsum=nums[a]+ nums[i]+ nums[curr]
                
                if tsum>0:
                    a-=1
                elif tsum<0:
                    i+=1
                else:
                    out=[nums[a],nums[i],nums[curr]]
                    out.sort()
                    fin.append(out)
                    i+=1
                    while nums[i]==nums[i-1] and a>i:
                        i+=1
                    a-=1
                    while nums[a]==nums[a+1] and a>i:
                        a-=1
                    
                    
        i=0
        


        return fin
    # -4,-1,-1,0,1,2
