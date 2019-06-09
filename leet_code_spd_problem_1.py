# Leet Code SPD1.01 Problem 1
# Question: Two Sum



class Solution:
  def twoSum(self, nums, target):
   #       going to create a dictionary for instant lookup, where key is the number and the value is the index
    num_store = self.create_num_store(nums) # O(n) space complexity
  # 
    for num in nums: # O(n) time complexity
      lookup_num = target - num
      if lookup_num in num_store: #O(1) time complexity 
        return [num, lookup_num]
      else:
        num_store.pop(num)

    
    
  def create_num_store(self, nums) :
    num_dict = {}

    for index, number in enumerate(nums):
      num_dict[number] = index
    return num_dict



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
# 