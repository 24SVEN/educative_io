
def search_min_diff_element(arr, key):
    # TODO: Write your code here

    lw,rw=0,len(arr)
    prev_diff = float('inf')

    while lw<=rw:
        mid=(rw+lw)//2
        diff = abs(arr[mid]-key)
        #difference is growing again
        if diff > prev_diff or diff == 0:
            return arr[mid]
        elif diff > arr[mid]:
            lw = mid + 1
            prev_diff=diff
        else:
            rw = mid-1
            prev_diff=diff


    return -1


def main():
  print(search_min_diff_element([4, 6, 10], 7))
  print(search_min_diff_element([4, 6, 10], 4))
  print(search_min_diff_element([1, 3, 8, 10, 15], 12))
  print(search_min_diff_element([4, 6, 10], 17))


main()
