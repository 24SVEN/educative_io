from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse(head):
    # TODO: Write your code here

    prev_node = None

    while head:
        #temporarily store head.next
        next_node = head.next

        #set next to previous head
        head.next = prev_node

        #set prev_head to the next_node now to complete the switch
        prev_node = head
        #set back to head
        head = next_node


    return prev_node


def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(8)
  head.next.next.next.next = Node(10)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse(head)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()
