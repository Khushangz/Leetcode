class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        x=len(height)-1
        sum=min(height[i],height[x])*(x-i)
        while i<x:
            m=min(height[i],height[x])*(x-i)
            sum=max(m,sum)
            if height[i]>height[x]:
                x-=1
            else:
                i+=1
        return sum






