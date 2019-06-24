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

class Node(object):
  def __init__(self, val):
    self.val = val
    self.next = None

  # get data
  # set data
  # get the next node
  # set the next node

class LinkedList(object):
  def __init__(self, head=None):
    self.head = head
    self.size = 0

  def insert(self, data):
    # TODO: insert a new node
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
    self.size += 1
  
  def find(self, val):
    # TODO: find the first item with a given value
    item = self.head

    while item != None:
      if item.val == val:
        return item
      else:
        item = item.next
    return None
  
  def delete_at(self, index):
    # TODO: delete an item at given index
    if index > self.size - 1:
      return
    if index == 0:
      self.head = self.head.next
    else:
      temp_index = 0
      node = self.head
      while temp_index < index - 1:
        node = node.next
        temp_index += 1
      node.next = node.next.next
      self.size -= 1


  def dump_list(self):
    temp_node = self.head
    while temp_node != None:
      print("Node: ", temp_node.val)
      temp_node = temp_node.next

# testing insert
itemList = LinkedList()
itemList.insert(38)
itemList.insert(49)
itemList.insert(13)
itemList.insert(15)
itemList.dump_list()

print("Linkedlist size: ", itemList.size)
print("Find item: ", itemList.find(13))
print("Finding item: ", itemList.find(78))

print("Deleting....")
itemList.delete_at(3)
print("Linkedlist size: ", itemList.size)
print("Finding item: ", itemList.find(38))
itemList.dump_list()