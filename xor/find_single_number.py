def find_single_number(arr):
    # TODO: Write your code here
    bit_val = 0
    for i in range(len(arr)):
        bit_val = bit_val ^ arr[i]
    return bit_val

def main():
    arr = [1, 4, 2, 1, 3, 2, 3]
    print(find_single_number(arr))
    arr2 = [7,9,7]
    print(find_single_number(arr2))

main()