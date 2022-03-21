from __future__ import print_function


class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def print_interval(self):
    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge(intervals):
  if len(intervals) == 1:
      return intervals
  
  #sort by first
  intervals.sort(key=lambda x:x.start)
  
  i = 0
  
  while i < len(intervals) and i!= len(intervals)-1:
      if intervals[i+1].start <= intervals[i].end:
          intervals[i+1] = Interval(intervals[i].start,max(intervals[i].end,intervals[i+1].end))
          intervals.pop(i)
      else:
          i += 1
  return intervals


def main():
  print("Merged intervals: ", end='')
  for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
    i.print_interval()
  print()

  print("Merged intervals: ", end='')
  for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
    i.print_interval()
  print()

  print("Merged intervals: ", end='')
  for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
    i.print_interval()
  print()

main()