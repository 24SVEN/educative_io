def find_single_number(arr):
    # TODO: Write your code here
    # bit_val = 0
    # for i in range(len(arr)):
    #     bit_val = bit_val ^ arr[i]
    # return bit_val

    dic_bit = {}

    for i in range(len(arr)):
        if arr[i] in dic_bit:
            dic_bit[arr[i]] -= 1
            del dic_bit[arr[i]]
        else:
            dic_bit[arr[i]] = 1

    return [key for key in dic_bit.keys()][0]

def main():
    arr = [1, 4, 2, 1, 3, 2, 3]
    print(find_single_number(arr))
    arr2 = [7,9,7]
    print(find_single_number(arr2))

main()