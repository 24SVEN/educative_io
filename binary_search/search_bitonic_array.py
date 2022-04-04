
from turtle import left, right


def binary_search(lw,rw,arr,key,isIncreasing):



    while lw<=rw:
        mid = lw + (rw-lw)//2

        if arr[mid] == key:
            return mid
        if isIncreasing:
            if arr[mid] > key:
                rw = mid -1
            else:
                lw = mid + 1
        else:
            if arr[mid] > key:
                lw = mid + 1
            else:
                rw = mid -1

    return -1
def search_bitonic_array(arr, key):
    # TODO: Write your code here

    lw,rw = 0,len(arr)-1
    midpoint = 0

    if arr[0] > arr[1]:
        return binary_search(0,len(arr)-1,arr,key,False)
    elif arr[-1] > arr[-2]:
        return binary_search(0,len(arr)-1,arr,key,True)

    #binary search 2 times
    while lw<=rw:
        mid = lw + (rw-lw)//2

        if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
            midpoint =  mid
            break
        elif arr[mid] < arr[mid+1]:
            lw = mid + 1
        else:
            rw = mid- 1

    #now have midpoint
    leftside = binary_search(0,midpoint,arr,key,True)
    rightside = binary_search(midpoint,len(arr)-1,arr,key,False)

    if leftside == -1 and rightside == -1:
        return -1
    elif leftside != -1:
        return leftside
    else:
        return rightside


def main():
    print(search_bitonic_array([1, 3, 8, 4, 3], 4))
    print(search_bitonic_array([3, 8, 3, 1], 8))
    print(search_bitonic_array([1, 3, 8, 12], 12))
    print(search_bitonic_array([10, 9, 8], 10))


main()
