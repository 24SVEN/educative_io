def find_range(arr, key):
    result = [- 1, -1]
    # TODO: Write your code here 
    if len(arr) == 1:
        if arr[0] == key:
            return [0,0]
        else:
            result
        return result
    lw,rw = 0,len(arr) - 1
    mid = 0

    l,r = 0,0
    while lw<= rw:
        mid = (rw+lw)//2

        if arr[mid] == key:
            l = mid 
            r = mid 
            while arr[l] == key and l >= 0:
                l-=1
            while r <= (len(arr)-1) and arr[r] == key:
                r+=1
            return [l+1,r-1]

        elif arr[mid] > key:
            rw = mid - 1
        else:
            lw = mid + 1

    return result
def main():
    # print(find_range([4, 6, 6, 6, 9], 6))
    # print(find_range([1, 3, 8, 10, 15], 10))
    # print(find_range([1, 3, 8, 10, 15], 12))
    # print(find_range([1, 3, 8, 10, 15], 12))
    print(find_range([2,2], 2))
main()
