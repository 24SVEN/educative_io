import heapq

#Can solve this problem in O(N) with bucket sort. Review!

def find_k_frequent_numbers(nums, k):
    topNumbers = []
    # TODO: Write your code here
    hashmap = {}

    for i in range(len(nums)):
        hashmap[nums[i]] = 1 + hashmap.get(nums[i],0)

    result_nums = [[val,key] for key,val in hashmap.items()]
    
    for i in range(k):
        heapq.heappush(topNumbers,result_nums[i])

    for i in range(k,len(result_nums)):
        if result_nums[i][0] > topNumbers[0][0]:
            heapq.heappop(topNumbers)
            heapq.heappush(topNumbers,result_nums[i])

    
    return [pair[1] for pair in topNumbers]


def main():

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()

