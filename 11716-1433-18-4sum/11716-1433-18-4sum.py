class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for x in range(n-3):
            if x > 0 and nums[x] == nums[x - 1]:
                    continue
            i=x+1
            while i < n-2:
                left, right = i + 1, n - 1
                while left < right:

                    curr_sum = nums[i] + nums[left] + nums[right] + nums[x]
                    if curr_sum == target:
                        res.append([nums[i], nums[left], nums[right],nums[x]])
                        
                        # Move left pointer and skip duplicates
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        
                        # Move right pointer and skip duplicates
                        right -= 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1


                    elif curr_sum < target:
                        left += 1
                    else:
                        right -= 1
                i+=1
                while i < n-2 and nums[i] == nums[i-1]:
                    i=i+1
                        
        return res
