class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_path(root, sequence):
  

  def dfs(root,path,sequence):
    if root is None:
      return path

    path.append(root.val)
    if root.left:
      dfs(root.left,path)
    if root.right:
      dfs(root.right,path)

    if path == sequence:
      return True

    else:
      return False
  
  return dfs(root,[],sequence)

  # TODO: Write your code here
  return False  



def main():

  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
  print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
