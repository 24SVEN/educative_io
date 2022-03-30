class Point:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def print_point(self):
    print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')

import heapq
def find_closest_points(points, k):
    result = []
    # TODO: Write your code here
    min_heap = []
    for point in points:
      c = (point.x ** 2 + point.y ** 2) ** .5
      min_heap.append([c,point])

    heapq.heapify(min_heap)

    while k > 0:
      dist,point = heapq.heappop(min_heap)
      result.append(point)
      k-=1
    return result


def main():

  result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
  print("Here are the k points closest the origin: ", end='')
  for point in result:
    point.print_point()


main()

