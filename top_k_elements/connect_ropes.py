from audioop import add
import heapq
def minimum_cost_to_connect_ropes(ropeLengths):
    result = []
    # TODO: Write your code here

    total_cost = 0
    current_length = 0
    #isnt time complexity of heap same as sorting since we need to go through all elements?
    heapq.heapify(ropeLengths)


    while len(ropeLengths) > 1:
        added_rope = heapq.heappop(ropeLengths) + heapq.heappop(ropeLengths)
        total_cost += added_rope
        heapq.heappush(ropeLengths,added_rope)

    return total_cost


def main():

  print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
  print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
  print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))


main()