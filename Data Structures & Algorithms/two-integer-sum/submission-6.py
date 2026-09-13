class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

    # Using a dictionary to store each number and its index allows O(n) performance,
    # since dictionary lookups are O(1). For each number, we calculate its complement
    # (num_b) and check if it's already in target_list. If found, we return the stored
    # index alongside the current index. Otherwise, we store the current number and
    # index for future lookups.

        target_list = {}

        for index, num_a in enumerate(nums):
            
            num_b = target - num_a
            
            if num_b in target_list:
                index_b = target_list[num_b]
                return [index_b, index]
             
            else:
                target_list[num_a] = index


        





    
        