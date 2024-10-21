from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        
        def backtrack(start, current_sum, current_combination):
            # Base case: if current sum equals target, we add the combination
            if current_sum == target:
                results.append(list(current_combination))  # Deep copy of current_combination
                return
            # If current sum exceeds target, stop further exploration
            if current_sum > target:
                return
            
            # Explore further
            for i in range(start, len(candidates)):
                current_combination.append(candidates[i])
                backtrack(i, current_sum + candidates[i], current_combination)
                current_combination.pop()
        
        # Initial call to the backtrack function
        backtrack(0, 0, [])
        return results
