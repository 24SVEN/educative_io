class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def has_cycle(head):
  # TODO: Write your code here
    # h_map = {}
    
    # nodes = []

    # while head:
    #     if head in h_map and head.next == h_map[head]:
    #         return True
        
    #     h_map[head] = head.next

    #     head = head.next

    # return False

    slow_pointer,fast_pointer = head,head

    while fast_pointer and fast_pointer.next:
        fast_pointer = fast_pointer.next.next
        slow_pointer = slow_pointer.next
        if fast_pointer == slow_pointer:
            return True

    return False




def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  print("LinkedList has cycle: " + str(has_cycle(head)))

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList has cycle: " + str(has_cycle(head)))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList has cycle: " + str(has_cycle(head)))


main()
