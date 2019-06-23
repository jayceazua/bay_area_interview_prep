class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # a variable to keep track of the iteration of the sequence
        return_counter = 0
        # another counter variable to later compare with the return_counte; this is the variable that will be reset back to 0
        compare_counter = 0
        # have a set to check if the character was looked at before
        substring = set()  # O(n) space complexity
        substring.
        # keep track of the current index
        # current_index = 0
        # keep track of the previous index
        # previous_index = -1

        # loop through the given string but also keep track of the index
        for char in s:  # O(n) time complexity
            #         check if the character of the string is in the set
            if char in substring:  # O(1) time complexity for lookup
                #         check if the compare counter is greater than the return counter
                if compare_counter > return_counter:
                    #           make sure that the return counter is equal to the compare since it is a larger number than the return counter
                    return_counter = compare_counter
#         clear the set to no values to start the sequence from zero
                substring.clear()
#         start from zerp
                compare_counter = 0
#       otherwise
            else:
                    #         increate the compare counter by one
                compare_counter += 1

            substring.add(char)
            # return_counter += 1
            # compare_counter += 1

        print("Returning: {}".format(compare_counter))
        return return_counter  # O(1) space complexity


# Restate:
# Alright, so I am given a string, and I need to find the longest "substring"
# that does not have repeating characters from within the given string.

# Clarifying Questions:
# 1. what if I am given an empty string, what should I return then?
# 2. If there is no substring, what should I return?
# 3. Should I always expect for the given input to always be of type string?
# 4. Can I use built-in language specifics methods, functions, or libraries?

# Assumptions:
# 1. I would need to iterate through the entire given string, to find other substring that "might be longer".
# 2. what if there are two substrings that equal in length, I assume to simply just return that length.
# 3. there is no point in shorting the give string.

# Think out load

# brainstorm solutions:
# I am going to have a counter variable on which I am going to return at the end of the function. I am also going to have a variable that
# remembers the previous or should I do the one ahead? Going to have a checker if the current_index
# is the same as either the previous or next coming index value. I might consider doing the previous index to avoid index out range error.

# explain your rationale:
# by doing such I make time complexity O(n) and space complexity O(1).
# I keep a variable counter that compares later if another substring sequence begins.


# discuss trade offs: Found out that it is best to use a set data structure to keep track of the sequence of repeats.

# suggest improvements: using a hastset was a major improvement from me. 

# Leetcode:
