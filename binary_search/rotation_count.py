def count_rotations(arr):
    # TODO: Write your code here
    lw,rw = 0,len(arr)-1


    while lw<= rw:
        mid = lw + (rw-lw)//2

        if mid < rw and arr[mid] > arr[mid+1]:
            return mid
        if mid > lw and arr[mid-1] > arr[mid]:
            return mid
        
        elif arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
            return mid
        elif arr[mid] <= arr[lw]:
            rw = mid - 1
        else:
            lw = mid + 1


    return 0


def main():
  print(count_rotations([10, 15, 1, 3, 8]))
  print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
  print(count_rotations([1, 3, 8, 10]))


main()
