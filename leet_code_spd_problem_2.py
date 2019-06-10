# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# function to turn a linked list to a number
def return_integer_from_ll(ll: ListNode) -> int:
    # repr_num = [] # takes O(n) time and space complexity
    repr_num = ""  # O(n) space complexity and time is O(1) time complexity
    current_node = ll

    while current_node != None:  # make sure that the current node does not equal to none
        # repr_num.insert(0, str(current_node.val)) # changed this because this would be O(n) time and space complexity
        repr_num += str(current_node.val)  # O(1) time complexity
        current_node = current_node.next
    # return int("".join(repr_num)) # along with the join method would make it O(n) time complexity
    # python's inbuilt reverse string method makes it easy
    return int(repr_num[::-1])


# function to turn a number into a linked list
def convert_num_to_ll(num: int) -> ListNode:
    num_str = str(num)[::-1]  # convert the number into a string and reverse it

    head = None  # [first->]
    tail = None  # [second-> "next" second->]

    ####   create the linked list ####
#   prepend method for linked list
    for n in num_str:
        # create a new node with the value
        new_node = ListNode(int(n))
        # check if the head of the linked list is empty
        if head == None:
            # set the start of the linked list
            tail = new_node
        # otherwise
        else:
            new_node.next = head

        # set the new node as well as the new node created above
        # tail = new_node
        head = new_node
        # head.next = tail
    return head


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # instantiate the linked list we need to return.
        # l3 = ListNode(None)

        # a function or method that allows me to traverse through the linked list and return a digit value
        l1_num = return_integer_from_ll(l1)

        l2_num = return_integer_from_ll(l2)

        l3 = convert_num_to_ll((l1_num + l2_num))
        # another function to get a digit and return a linked list representation of the number given
        return l3

        # Restate: So, I have two non-empty linked lists. And the data containing the linked list are non-negative integers.
        # In total they represent a number but it is reversed. So for example 3->2->1 is simply 123. With that I need to add these two numbers.
        # Then I need to return the total of those two numbers as a reversed representation linked list.
        # Also, besides each individual node, the total number of a linked list will not be zero?

        # Clarifying Questions:
        # 1. does the linked list have a tail property
        # 2. Does the linked lists given have to be singly or can they be doubly
        # 3. is the data in the linked data type of int or strings or both
        # 4. what does "two numbers do not contain any leading zero, except the number 0 itself." mean?

        # Assumptions:
        # 1. the linked list has a head and tail properties
        # 2. the linked list given have head and tail properties.
        # 3. I can create my own node and linked list class
        # 4. I can convert ints into strings

        # Think out load

        # brainstorm solutions: I'm thinking about traversing through the given linked list and getting the values
        # from each node and putting it into a list and later reversing those numbers to get a single whole number.
        # Then repeating the same function for the second linked list and then adding them together.
        # With that given whole integer, I convert it into a string in order to traverse through the number.
        # I reverse traverse and start creating nodes of the inverse representation of the added number.
        # Create a reusable method to traverse through a linked list and return the proper number.
        # Another method to reverse the number and create a reversed linked list.

        # explain your rationale: I feel as through It needs to be done in this manner because regardless traversing
        # through a linked list is O(n). Having a custom method makes it cleaner code and reusable.

        # discuss trade offs: I was considering putting the numbers in an array as a traverse through the linked list then calling the reverse option
        # on the arrays. However, that is another time complexity I need to consider. It is better if I call .insert(0, node.data) method
        # to add the given value to the front then later converting that entire list into a whole integer. Less operations than appending them
        # to the list to later reverse them.

        # suggest improvements:

        # Leetcode:
