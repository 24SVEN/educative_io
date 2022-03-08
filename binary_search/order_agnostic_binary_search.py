#704. Binary Search 
# https://leetcode.com/problems/binary-search/submissions/
#change parameters to arr and key in leetcode. Then return mid on line 22 for leetcode submission.
def binary_search(arr, key):
    # TODO: Write your code here

    # if key in arr:
    #     #index methods time complexity of O(N)
    #     return arr.index(key)



    lw,rw,mid = 0,len(arr) - 1,0
    isAscendending = False
    if arr[rw] > arr[lw]:
        isAscendending = True


    while lw<=rw:
        mid = (rw+lw)//2

        if arr[mid] == key:
            return key
        if isAscendending:

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

def main():
    print(binary_search([4, 6, 10], 10))
    print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
    print(binary_search([10, 6, 4], 10))
    print(binary_search([10, 6, 4], 4))


main()
