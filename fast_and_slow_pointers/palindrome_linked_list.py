from multiprocessing.dummy import current_process



class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def is_palindromic_linked_list(head):
    # TODO: Write your code here
    start = head
    slow,fast = head,head
    copy = head

    def reverse_linked_list(head):
      prev = None
      while head:
        temp = head
        head = head.next
        temp.next = prev
        prev = temp
      
      return prev

    while fast and fast.next:
      fast = fast.next.next
      slow = slow.next

    mid = slow


    prev = reverse_linked_list(mid)
    copy = prev
    
    #prev is now starting point
    while prev:
      if prev.value != start.value:
        return False
      prev = prev.next
      start = start.next
    
    reverse_linked_list(copy)

    while copy:
      print(copy.value)
      copy = copy.next

    return True



def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(2)

  print("Is palindrome: " + str(is_palindromic_linked_list(head)))

  # head.next.next.next.next.next = Node(2)
  # print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()







