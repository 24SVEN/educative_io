#Leetcode 113
#https://leetcode.com/problems/path-sum-ii/


class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_paths(root, required_sum):
    allPaths = []
    # TODO: Write your code here
    dfs(root,required_sum,[],allPaths)
    return allPaths


def dfs(root,required_sum,current_path,allPaths):
    if root is None:
        return None

    current_path.append(root.val)

    if root.val == required_sum and root.left is None and root.right is None:
        #allPaths.append(current_path)
        #[[12, 7, 4]]

        #LIST() IS NECESSARY IN ORDER TO CREATE A NEW LIST!! OTHERWISE IT WILL REMOVE FROM THIS
        allPaths.append(list(current_path))
        #[[12, 7, 4]]
    else:
        dfs(root.left,required_sum-root.val,current_path,allPaths)
        dfs(root.right,required_sum-root.val,current_path,allPaths)

    del current_path[-1]


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

