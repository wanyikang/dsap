# -*- coding: utf-8 -*-
# I use binary tree to demonstrate the algorithm, but it fits the general tree
# too. Just for easiness to using binary tree.
# The running time of this algorithm is O(max(dp, dq)).
import sys
sys.path.append('../')
from trees.mutable_linked_binary_tree import MutableLinkedBinaryTree
from trees.mutable_linked_binary_tree import construct_tree

class BinaryTree(MutableLinkedBinaryTree):

    def lowest_common_ancestor(self, p, q):
        """ Get the lowest ancestor of p and q."""
        p_acs = []
        q_acs = []
        # get all ancestor of p
        pa = p
        while pa != self.root():
            p_acs.append(pa)
            pa = self.parent(pa)
        p_acs.append(pa)
        # get all ancestor of q
        qa = q
        while qa != self.root():
            q_acs.append(qa)
            qa = self.parent(qa)
        q_acs.append(qa)

        # get the lowest ancestor from the two lists
        k = -1
        while True:
            try:
                pa = p_acs[k]
                qa = q_acs[k]
            except IndexError:
                break
            if pa != qa:
                break
            else:
                k -= 1
        k += 1  # index of the lowest common ancestor
        return p_acs[k]


if __name__ == '__main__':
    t = construct_tree('((((3+1)x3)/((9-5)+2))-((3x(7-4))+6))', BinaryTree)
    p = t.left(t.left(t.left(t.left(t.root()))))
    q = t.left(t.left(t.right(t.root())))
    lca = t.lowest_common_ancestor(p, q)
    print(lca.element())

