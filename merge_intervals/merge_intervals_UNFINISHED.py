from __future__ import print_function


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge(intervals):
    merged = []
    # TODO: Write your code here
    if len(intervals) == 1:
        return intervals
    for i in range(1,len(intervals)):
        merged.append(helper(intervals[i-1],intervals[i]))



    return merged

def helper(first_interval,second_interval):
    merged = []
    if second_interval.start > first_interval.start and second_interval.start < first_interval.end or second_interval.end < first_interval.end and second_interval.end >first_interval.start:
        merged.append(Interval(min(first_interval.start,second_interval.start),max(first_interval.end,second_interval.end)))
    else:
        merged.append([first_interval,second_interval])
    return merged

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