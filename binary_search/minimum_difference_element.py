
def search_min_diff_element(arr, key):
    # TODO: Write your code here

    if arr[-1] < key:
        return arr[-1]
    if arr[0] > key:
        return arr[0]

    lw,rw=0,len(arr)

    while lw<rw:
        mid=lw + (rw-lw)//2

        #difference is growing again
        if arr[mid] == key:
            return arr[mid]
        elif arr[mid] > key:
            rw = mid-1
        else:
            lw = mid + 1

    if abs(key - arr[lw]) > abs(key-arr[rw]):
        return arr[rw]
    else:
        return arr[lw]




def main():
  print(search_min_diff_element([4, 6, 10], 7))
  print(search_min_diff_element([4, 6, 10], 4))
  print(search_min_diff_element([1, 3, 8, 10, 15], 12))
  print(search_min_diff_element([4, 6, 10], 17))


main()
