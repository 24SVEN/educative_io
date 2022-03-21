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


def reverse_sub_list(head, p, q):
    # TODO: Write your code here

    node_p = None
    node_q = None
    prev_p,prev_q = None, None
    prev = None
    while head:
        if head.value == p:
            node_p = head
            prev_p = prev
        if head.value == q:
            node_q = head
            prev_q = prev
        prev = head
        head = head.next

    #
    prev = None
    temp = None
    while head:
        if head == prev_p:
            temp = head.next.next
            node_p.next = temp
            head.next = node_p
        if head == prev_q:
            temp = head.next.next
            node_q.next = temp
            head.next = node_q

        prev = head
        head = head.next
    
    return head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_sub_list(head, 2, 4)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()
