def search_rotated_array(arr, key):
    # TODO: Write your code here

    lw,rw = 0,len(arr)-1

    while lw<= rw:

        mid = lw + (rw-lw)//2

        if arr[mid] == key:
            return mid

        elif arr[lw] < arr[mid] and key >= arr[lw] and key < arr[mid]:
            rw = mid - 1

        elif arr[lw] > arr[mid] and key >= arr[lw] and key >arr[mid]:
            rw = mid-1
        elif arr[lw] > arr[mid] and key <=arr[lw] and key <arr[mid]:
            rw = mid-1
        else:
            lw = mid+1

    return -1

def main():
  print(search_rotated_array([10, 15, 1, 3, 8], 15))
  print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))


main()