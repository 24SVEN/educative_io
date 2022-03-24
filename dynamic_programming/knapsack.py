
class Solution():
    def solve_knapsack(self,profits, weights, capacity):
        # TODO: Write your code here

        dp = [[0 for i in range(capacity+1)] for _ in range(len(weights))]

        for row in range(len(weights)):
            for col in range(capacity+1):
                if weights[row] > col:
                    if row == 0:
                        dp[row][col] = 0
                    else:
                        dp[row][col] = dp[row-1][col]
                else:
                    #num_fruits = col // weights[row]
                    if row > 0:
                        
                        dp[row][col] = max(dp[row-1][col],dp[row-1][col-weights[row]] + profits[row])
                    else:
                        #this is basically the first row's calculation
                        dp[row][col] = profits[row]

        return dp[-1][-1]


def main():
    test = Solution()
    print(test.solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(test.solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 61))
    print(test.solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 100))


main()

