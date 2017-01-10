'''
Author: Ping Guo
Email: pingg104@gmail.com
Problem Statement: (4.5) Validate BST
Implement a function to check if a binary tree is a binary search tree.
Complexity:BigO(N)
Usage: validate_BST <node>
'''


def answer(n):
    last_printed = None

    def check_BST(root):
        '''
        In-order traversal to print the first number and compare with the
        second number, if the first >= the second, return False. This solution
        assumed that there are not duplicate number in the tree.

        '''
        if root:
            if not check_BST(root.left):
                return False
            if last_printed is not None and last_printed >= root:
                return False
            last_printed = root

            if not check_BST(root.right):
                return False

            return True

    return check_BST(n)

# executable
if __name__ == '__main__':
    # executable import only
    from docopt import docopt
    args = docopt(__doc__)
    n = args('<node>')
    print answer(n)
