# Leet Code SPD1.01 Problem 1
# Question: Two Sum


class Solution:
    def twoSum(self, nums, target):
     #       going to create a dictionary for instant lookup, where key is the number and the value is the index
        # num_store = self.create_num_store(nums) # O(n) space complexity and time
        num_store = {}

        # i want to have a bank of the numbers given to me
        # as i go through the array of numbers I substract the given number with the target and get a value
        # with that value number i will look in my bank of key(num) value(index) pairs
        for index, num in enumerate(nums):
            lookup = target - num
            if lookup in num_store:
                return [num_store[lookup], index]
            num_store[num] = index
        return []


# Restate: Okay, so I am given an array that contains a list of numbers.
# I am also getting a target value. I need to find two numbers within the
# given array that add up to the given target. When I find those numbers
# I need to store their index in a list and return that.

# Clarifying Questions:
# 1. can the list contain negative numbers
# 2. what if there is no solution what should we return
# 3. on the example the list is sorted, will it always be sorted?
# 4. should we focus on correctiveness of the algorithm or performance or both
# 5. can we use built-in language specifics
# 6. what if the array is empty, should I return an empty list or raise an error
# 7. the target input could it be a negative number

# Assumptions:
# 1. the given list will be a dynamic array and not another form of linear order; linked list
# 2. we should return an empty list if there is no solution
# 3. i will always be given a data type of a list as an input
# 4. the elements within the list are all of type int
# 5. the target number will be of type integer and no other primitive data type

# ORIGINAL THOUGHT:
# I was thinking of having two variable pointers one that starts at index 0
# the other starting at index of the first point plus one
# the second point will go through the entire list and add each number that it gets with the index value of pointer 1
# if it does not find it it will shift the pointer 1 up one and the pointer 2 will restart to pointer's 1 index plus 1 and repeat
# until it finds the total sum to return the index. If not it will return an empty list.
# However this solution is O(n^2) in time complexity and O(1) space complexity. Meaning it will take a long time if we get large inputs
