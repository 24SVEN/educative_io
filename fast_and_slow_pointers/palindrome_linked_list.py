from multiprocessing.dummy import current_process



class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def is_palindromic_linked_list(head):
    # TODO: Write your code here
    start = head
    slow,fast = head,head

    while fast and fast.next:
      fast = fast.next.next
      slow = slow.next


    mid = slow

    prev = None
    while mid:
      temp = mid
      mid = mid.next
      temp.next = prev
      prev = temp
    
    #prev is now starting point
    while prev:
      if prev.value != start.value:
        return False
      prev = prev.next
      start = start.next
    
    return True



def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(2)

  #print("Is palindrome: " + str(is_palindromic_linked_list(head)))

  head.next.next.next.next.next = Node(2)
  print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()







