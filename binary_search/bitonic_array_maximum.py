def find_max_in_bitonic_array(arr):
    # TODO: Write your code here

    #need to solve for edge cases where max is at 0 and n-1
    if arr[0] > arr[1]:
        return arr[0]
    if arr[len(arr)-1] > arr[len(arr)-2]:
        return arr[len(arr)-1]

    lw,rw = 0,len(arr)-1

    while lw<rw:
        mid = lw + (rw-lw)//2

        if arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:
            return arr[mid]
        elif arr[mid] < arr[mid+1]:
            lw = mid + 1
        else:
            rw = mid - 1


    return -1


def main():
    print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
    print(find_max_in_bitonic_array([3, 8, 3, 1]))
    print(find_max_in_bitonic_array([1, 3, 8, 12]))
    print(find_max_in_bitonic_array([10, 9, 8]))


main()
