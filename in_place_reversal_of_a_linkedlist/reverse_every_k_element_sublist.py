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


def reverse_every_k_elements(head, k):
    # TODO: Write your code here
    dummy = Node(0)
    dummy.next = head
    left_prev = dummy
    while head != None:
        prev = None
        start = head

        temp2 = head
        check = True
        for i in range(k):
            if temp2:
                temp2 = temp2.next
            else:
                check = False

        if check:
            for i in range(k):
                if head:
                    temp = head.next
                    head.next = prev
                    prev = head
                    head = temp
            left_prev.next = prev
            left_prev = start
        else:
            left_prev.next = head
            break


    return dummy.next


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = Node(7)
  head.next.next.next.next.next.next.next = Node(8)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_every_k_elements(head, 3)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()







