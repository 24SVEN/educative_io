#129. Sum Root to Leaf Numbers

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_path_numbers(root):
    # TODO: Write your code here

    if root is None:
        return 0
    res = []
    def dfs(root,res,cur_list):
        if root:
            if root.left is None and root.right is None:
                cur_list += [root.val]
                str_val = ''
                for x in cur_list:
                    str_val += str(x)

                res.append(int(str_val))
            dfs(root.left,res,cur_list + [root.val])
            dfs(root.right,res,cur_list + [root.val])

    dfs(root,res,[])

    return sum(res)



def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
