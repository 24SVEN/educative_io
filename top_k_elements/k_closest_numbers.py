import heapq
def find_closest_elements(arr, K, X):
    result = []
    # TODO: Write your code here

    #absolute difference | number
    #abs difference is X - current_num
    hashmap = {}
    for i in range(len(arr)):
        diff = abs(arr[i] - X)
        hashmap[diff] = hashmap.get(diff) + 1

    min_heap = []
    for i in range(K):
        heapq.heappush(min_heap,)

    return result


def main():
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


main()
