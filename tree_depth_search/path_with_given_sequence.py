class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_path(root, sequence):
  

  def dfs(root,sequence,current_path):
    if root is None:
      return False
    
    current_path.append(root.val)

    if root.left is None and root.right is None and current_path == sequence:
      return True
    
    else:
      res = dfs(root.left,sequence,current_path) or dfs(root.right,sequence,current_path)
    
    current_path.pop()
    return res


  return dfs(root,sequence,[])

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
