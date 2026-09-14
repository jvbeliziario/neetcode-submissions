class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Iterate through nums, using each number as a dictionary key. If the number
        # hasn't been seen yet, add it with a count of 1. Otherwise, increment its
        # existing count. Then sort the keys by count in descending order, and slice
        # the first k elements to return the k most frequent numbers.

        final_list = {}
        
        for number in nums:
            if number not in final_list:
                counter = 1
                final_list[number] = counter
            else:
                final_list[number] += 1
        
        sorted_list = sorted(final_list, key=lambda number: final_list[number], reverse=True)
        return sorted_list[:k]
        
