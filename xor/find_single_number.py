def find_single_number(arr):
    # TODO: Write your code here
    
    base_num = 0

    for num in arr:
        base_num = num ^ base_num
    return base_num

def main():
    arr = [1, 4, 2, 1, 3, 2, 3]
    print(find_single_number(arr))
    arr2 = [7,9,7]
    print(find_single_number(arr2))

main()