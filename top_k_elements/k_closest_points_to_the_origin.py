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
    sqrt = [((point.x ** 2) + (point.y ** 2)) **.5 for point in points]


    hashmap = dict(zip(points,sqrt))

    return [point for point,val in sorted(hashmap.items(),key = lambda x : x[1])][-k:]


def main():

  result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
  print("Here are the k points closest the origin: ", end='')
  for point in result:
    point.print_point()


main()

