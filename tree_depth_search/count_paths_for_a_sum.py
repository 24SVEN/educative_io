from msilib import sequence


class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def count_paths(root, S):
    # TODO: Write your code here

    def dfs(root,S,current_path,all_path):
        if root is None:
            return False

        current_path.append(root.val)

        if sum(current_path) > S:
            current_path = [root.val]

        if sum(current_path) == S and root.left is None and root.right is None:
            all_path.append(list(current_path))
        else:
            dfs(root.left,S,current_path,all_path)
            dfs(root.right,S,current_path,all_path)

        current_path.pop()

    
    all_path = []
    dfs(root,S,[],all_path)

    return len(all_path)


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has paths: " + str(count_paths(root, 11)))


main()
