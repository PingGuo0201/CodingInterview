'''
Author: Ping Guo
Email: pingg104@gmail.com
problem Statement: Check Balanced (4.4) pg. 110
    Implement a function to check if a binary tree is balanced. For the
    purposes of the question, a balanced tree is defined to be a tree that
    the heights of the two subtrees of any node never differ by more than one.
Complexity: BigO(N)
Usage: check_balance <node>
'''


def answer(n):

    def recursive_count(node, height):
        '''
        inorder traveral to count the height of the bottom nodes, and compare
        the height difference between left node and right node.
        '''
        height_left = recursive_count(node.left, height+1)
        height_right = recursive_count(node.right, height+1)
        if height_left < 1 or height_right < 1:
            return None

        elif abs(height_left - height_right) <= 1:
            return ((height_left + height_right)+abs(height_left - height_right))/2
        else return None
    h = 1
    return recursive_count(n, h)

# executable
if __name__ == '__main__':
    # executable import only
    from docopt import docopt
    args = docopt(__doc__)
    n = args('<node>')

    print answer(args)
