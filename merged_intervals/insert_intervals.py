def insert(intervals, new_interval):
    merged = []
    # TODO: Write your code here
    #intervals.append(new_interval)

    #intervals.sort(key=lambda x:x[0])

    #already sorted
    for i in range(len(intervals)):
        if new_interval[0] > intervals[i][0]:
            insert_index = i
            break
    
    
    intervals = intervals.copy()[:i+1] + [new_interval] + intervals.copy()[i+1:]


    idx = 0

    while idx < len(intervals)-1 and len(intervals)!=1:
        if intervals[idx+1][0] <= intervals[idx][1]:
            intervals[idx+1] = [intervals[idx][0],max(intervals[idx+1][1],intervals[idx][1])]
            intervals.pop(idx)
        else:
            idx+=1


    return intervals


def main():
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
#   print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
#   print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


main()
