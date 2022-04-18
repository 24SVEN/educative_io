class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_sum_of_path_numbers(root):
    # TODO: Write your code here

    def dfs(root,current_path,all_path):
        if root is None:
            return None

        current_path.append(str(root.val))

        if root.left is None and root.right is None:
            all_path.append(list(current_path))
        else:
            dfs(root.left,current_path,all_path)
            dfs(root.right,current_path,all_path)

        current_path.pop()

    all_path = []
    dfs(root,[],all_path)
    total = 0
    for li in all_path:
        li = int("".join(li))
        total += li


    return total



def main():
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)
  print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
