class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
    # Group anagrams using a dictionary. For each word, sort its letters and join
    # them into a string key. Words with the same key are anagrams of each other.
    # If the key already exists in the dictionary, append the word to its list.
    # Otherwise, create a new list for that key. Finally, return all the grouped
    # lists (the dictionary's values) as a list of lists.

        final_list = {}

        for word in strs:
            sorted_letters = sorted(word)
            key = "".join(sorted_letters)

            if key not in final_list:
                final_list[key] = [word]
            else:
                final_list[key].append(word)
            
        final_list = list(final_list.values())
        return final_list
        
            

        

