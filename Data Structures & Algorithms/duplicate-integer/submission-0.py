class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
    # Using a set for O(1) lookups instead of a list, reducing the overall
    # solution from O(n²) to O(n).
    
        target_set = set()
        for num in nums:
            if num not in target_set:
                target_set.add(num)
            else:
                return True
        return False

