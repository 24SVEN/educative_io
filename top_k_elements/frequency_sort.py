import heapq
import collections
def sort_character_by_frequency(str):
    # TODO: Write your code here

    hashmap = {}

    for i in range(len(str)):
        hashmap[str[i]] = hashmap.get(str[i],0) + 1

    #sorted_tuples = [key for key,val in hashmap.items()]

    heap_list = []

    for num,freq in hashmap.items():
        heapq.heappush(heap_list,[freq,num])

    result = collections.deque()
    while heap_list:
        pair = heapq.heappop(heap_list)
        result.appendleft(pair[1] * pair[0])


    return "".join(result)


def main():

  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("Programming"))
  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("abcbab"))


main()
