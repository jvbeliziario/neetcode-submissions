class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    # Using 2 dictionaries to store the count for each character, if the dictionaries are
    # different, then the two strings are not anagrams.

        count_s = {}
        count_t = {}

        for letter in s:
            if letter in count_s:
                count_s[letter] += 1
            else:
                count_s[letter] = 1

        for letter in t:
            if letter in count_t:
                count_t[letter] += 1
            else:
                count_t[letter] = 1

        return count_s == count_t