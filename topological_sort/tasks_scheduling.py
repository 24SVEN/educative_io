from collections import deque

class Solution:
    def is_scheduling_possible(self,tasks, prerequisites):
    # TODO: Write your code here
        visited = []

        freshman_class = {i : [] for i in range(tasks)}
        in_degrees = {i : 0 for i in range(tasks)}

        for pre_req in prerequisites:
            beginner_class, advanced_class = pre_req[0],pre_req[1]
            freshman_class[beginner_class].append(advanced_class)
            in_degrees[advanced_class] += 1

        queue = deque()
        
        for key,val in in_degrees.items():
            if val == 0:
                queue.append(key)
        
        while queue:
            current_class = queue.popleft()
            for prereq in freshman_class[current_class]:
                in_degrees[prereq] -= 1
                if in_degrees[prereq] == 0:
                    #check if cycle here
                    if prereq in visited:
                        return False
                    visited.append(prereq)
                    queue.append(prereq)

        return True

def main():
    test = Solution()
    
    print("Is scheduling possible: " +
    str(test.is_scheduling_possible(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " +
    str(test.is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " +
    str(test.is_scheduling_possible(6, [[0, 4], [1, 4], [3, 2], [1, 3]])))

main()
