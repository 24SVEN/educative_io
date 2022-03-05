#Leetcode 113
#https://leetcode.com/problems/path-sum-ii/

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root, sum):
    allPaths = []
    # TODO: Write your code here
    if not root:
        return []
    dfs(root,sum,allPaths,[])
    return allPaths

def dfs(root,sum,allPaths,currentPath):
    if root:

        if not root.left and not root.right and sum == root.val:
            currentPath += [root.val]
            allPaths.append(currentPath)

        dfs(root.left,sum - root.val,allPaths,currentPath + [root.val])
        dfs(root.right,sum-root.val,allPaths,currentPath + [root.val])

        




# def find_paths(root, targetSum: int):

#     res = []
#     dfs(root, targetSum, [], res)
#     return res

# def dfs(root, sum, ls, res):
#     if root:
#         if not root.left and not root.right and sum == root.val:
#             ls.append(root.val)
#             res.append(ls)
#         dfs(root.left, sum-root.val, ls+[root.val], res)
#         dfs(root.right, sum-root.val, ls+[root.val], res)

def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) +
        ": " + str(find_paths(root, sum)))


main()
