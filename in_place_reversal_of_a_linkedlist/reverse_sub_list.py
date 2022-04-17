from __future__ import print_function


class Node:
  def __init__(self, value=0, next=None):
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
    
    #assuming that p is always the left index (if not would just need to implement logic beforehand to get smaller of p and q)

    dummy = Node()
    dummy.next = head
    slow = dummy
    faster= dummy

    #slow is right before starting. At index 1, right before 2
    for i in range(p-1):
      slow = slow.next
    

    #Faster is exactly at node 4
    for i in range(q):
      faster = faster.next

    last = faster.next

    #start is at Node 2
    start_copy = slow.next
    start = slow.next
    prev = None

    #reverse node
    for i in range(q-p+1):
      temp = start.next
      start.next = prev
      prev = start
      start = temp
      

    #connect slow to start
    slow.next = prev
      
    #connect start to faster.next
    start_copy.next = last

    return dummy.next




def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  result = reverse_sub_list(head, 2, 4)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()
