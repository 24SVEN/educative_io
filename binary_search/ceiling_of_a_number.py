import math

def search_ceiling_of_a_number(arr, key):
    # TODO: Write your code here

    lw,rw = 0, len(arr) - 1
    result = math.inf

    while lw<=rw:
        mid = (rw + lw) // 2

        if arr[mid] == key:
            return mid

        elif arr[mid] > key:
            result = min(result,mid)
            rw = mid - 1
        else:
            lw=mid+1

    if result == math.inf:
        return -1

    return result


def main():
    print(search_ceiling_of_a_number([4, 6, 10], 6))
    print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_ceiling_of_a_number([4, 6, 10], 17))
    print(search_ceiling_of_a_number([4, 6, 10], -1))


main()
