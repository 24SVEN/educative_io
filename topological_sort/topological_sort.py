from collections import deque


def topological_sort(vertices, edges):
    sortedOrder = []

    parents = {i : [] for i in range(vertices)}
    in_degrees = {i : 0 for i in range(vertices)}

    for edge in edges:
        parent,child = edge[0],edge[1]
        parents[parent].append(child)
        in_degrees[child] += 1

    queue = deque()
    for key,val in in_degrees.items():
        if val == 0:
            queue.append(key)
    
    while queue:
        current_key = queue.popleft()
        sortedOrder.append(current_key)
        for child in parents[current_key]:
            in_degrees[child] -= 1
            if in_degrees[child] == 0:
                queue.append(child)


    return sortedOrder
 

def main():
  print("Topological sort: " +
        str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
  print("Topological sort: " +
        str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
  print("Topological sort: " +
        str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()
