# Find the greatest common denominator of two numbers
# using Euclid's Algorithm

# def gcd(a, b):
#   while not b is 0:
#     temp = a
#     a = b
#     b = temp % b
#   return a

# # try problem with a few test cases
# assert gcd(20, 8) == 4
# print(gcd(20, 8))
# assert gcd(60, 96) == 12
# print(gcd(60, 96))

# ======================================

# class Node(object):
#   def __init__(self, val):
#     self.val = val
#     self.next = None

#   # get data
#   # set data
#   # get the next node
#   # set the next node

# class LinkedList(object):
#   def __init__(self, head=None):
#     self.head = head
#     self.size = 0

#   def insert(self, data):
#     # TODO: insert a new node
#     new_node = Node(data)
#     new_node.next = self.head
#     self.head = new_node
#     self.size += 1

#   def find(self, val):
#     # TODO: find the first item with a given value
#     item = self.head

#     while item != None:
#       if item.val == val:
#         return item
#       else:
#         item = item.next
#     return None

#   def delete_at(self, index):
#     # TODO: delete an item at given index
#     if index > self.size - 1:
#       return
#     if index == 0:
#       self.head = self.head.next
#     else:
#       temp_index = 0
#       node = self.head
#       while temp_index < index - 1:
#         node = node.next
#         temp_index += 1
#       node.next = node.next.next
#       self.size -= 1


#   def dump_list(self):
#     temp_node = self.head
#     while temp_node != None:
#       print("Node: ", temp_node.val)
#       temp_node = temp_node.next

# # testing insert
# itemList = LinkedList()
# itemList.insert(38)
# itemList.insert(49)
# itemList.insert(13)
# itemList.insert(15)
# itemList.dump_list()

# print("Linkedlist size: ", itemList.size)
# print("Find item: ", itemList.find(13))
# print("Finding item: ", itemList.find(78))

# print("Deleting....")
# itemList.delete_at(3)
# print("Linkedlist size: ", itemList.size)
# print("Finding item: ", itemList.find(38))
# itemList.dump_list()

# # Stacks
# # create an empty stack
# stack = []
# # push items onto the stack
# stack.append(1)
# stack.append(2)
# stack.append(3)
# stack.append(4)
# # print stack contents
# print(stack)
# # pop an item off the stack
# x = stack.pop()
# print(stack)

# it is better to use a linkedlist for queues or deque
# from collections import deque
# # xreare an empty deque object that will function as a queue
# queue = deque()
# # add some items to the queue
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.append(4)
# # print the queue contents
# print(queue)
# # pop an item off the front of the queue
# x = queue.popleft()
# print(queue)

#  recursion
# recursion is when a functions calls itsel
# recursion functions need to have a breaking condition
# ,this prevents infinite loops and eventually crashes

# def countdown(x):
#   if x == 0:
#     print("done!")
#     return
#   else:
#     print(x, "...")
#     countdown(x - 1)
#     print("Interesting: ", x)

# countdown(3)

# def power(num, pwr):
#   # write the breaking condition first
#   if pwr == 0:
#     return 1
#   else:
#     return num * power(num, pwr - 1)

# def factorial(num):
#   if num == 0:
#     return 1
#   else:
#     return num * factorial(num - 2)

# print("{} to the power of {} is {}".format(5, 3, power(5, 3)))
# print("{}! is {}".format(8, factorial(8)))

# Sorting

# def bubble_sort(dataset):
#     # we decrease by one because we do not need to examine every element. so for range(x,x, -1) the -1 at the end indicates to decrease
#     # we stop at the 0 index item that is why we have a zero in the middle
#     for i in range(len(dataset) - 1, 0, -1):
#         for j in range(i):
#             if dataset[j] > dataset[j+1]:
#                 temp = dataset[j]
#                 dataset[j] = dataset[j+1]
#                 dataset[j+1] = temp


#  Merge sort is a
# divide-and-conquer algorithm
# breaks a dataset into individual pieces and merges them
# uses recursion to operate on datasets
# performs well on large datasets
#  O(n log n time complexity)


# def merge_sort(dataset):
#     if len(dataset) > 1:
#         mid = len(dataset) // 2
#         left_arr = dataset[:mid]
#         right_arr = dataset[mid:]

#         # TODO: recursively break down the arrays
#         merge_sort(left_arr)  # break the left array smaller
#         merge_sort(right_arr)  # break the right array smaller

#         # TODO: now perform the merging
#         i = 0  # index into the left array
#         j = 0  # index into the right array
#         k = 0  # index into the merged array

#         # TODO: while both arrays have content
#         while i < len(left_arr) and j < len(right_arr):
#             if left_arr[i] < right_arr[j]:
#                 dataset[k] = left_arr[i]
#                 i += 1
#             else:
#                 dataset[k] = right_arr[j]
#                 j += 1
#             k += 1

#         # TODO: if the left array still has value, add them
#         while i < len(left_arr):
#             dataset[k] = left_arr[i]
#             i += 1
#             k += 1 
#         # TODO: if the right array still has value, add them
#         while j < len(right_arr):
#           dataset[k] = right_arr[j]
#           j += 1
#           k += 1


# Quick sort similar to merge sort but does it in place. 
# if it is already sorted it will take O(n^2)
# pivot point selection

dataset = [20, 6, 8, 53, 23, 87, 42, 19]

def quick_sort(dataset, first, last):
  if first < last:
    # calculate the split point
    pivot_index = partition(dataset, first, last)
    # sort the two partitions
    quick_sort(dataset, first, pivot_index - 1)
    quick_sort(dataset, pivot_index + 1, last)

def partition(data_values, first, last):
  # choose the first item as the pivot value
  pivot_value = data_values[first]
  lower = first + 1
  upper = last

  done = False
  while not done:
    while lower <= upper and data_values[lower] <= pivot_value:
      lower += 1
    while data_values[upper] >= pivot_value and upper >= lower:
      upper -= 1
    if upper < lower:
      done = True
    else:
      temp_value = data_values[lower]
      data_values[lower] = data_values[upper]
      data_values[upper] = temp_value
  # when the split point is found, exchange the pivot value
  temp = data_values[first]
  data_values[first] = data_values[upper]
  data_values[upper] = temp
  # return the split point index
  return upper

print(dataset)
quick_sort(dataset, 0, len(dataset) - 1)
print(dataset)

# all(itemList[i] <= itemList[i+1] for i in range(len(itemList) - 1))
