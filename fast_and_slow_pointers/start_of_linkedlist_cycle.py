from __future__ import print_function
from math import dist


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
        print()


def find_cycle_start(head):
    # TODO: Write your code here

    #while this solution works the space complexity is O(N) due to the hashmap
    # hashmap = {}
    # while head:
    #     if head in hashmap:
    #         return head
    #     else:
    #         hashmap[head] = 1

    #     head = head.next

    # return head


    def get_distance(slow):
        current = slow
        distance = 0
        while current:
            current = current.next
            distance += 1
            if current == slow:
                return distance

    slow,fast = head,head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            distance = get_distance(fast)
            break

    
    slow,fast = head,head

    for i in range(distance):
        fast = fast.next

    while slow != fast:
        fast = fast.next
        slow = slow.next
    
    return slow

        




def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()
