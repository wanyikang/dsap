# -*- coding: utf-8 -*-
from linked_binary_tree import LinkedBinaryTree

class EulerTour(object):
    """ Abstract base class for performing Euler tour of a tree.

    _hook_previsit and _hook_postvisit may be overridden by subclasses.
    """
    def __init__(self, tree):
        """ Prepare an Euler tour template for given tree."""
        self._tree = tree

    def tree(self):
        """ Return reference to the tree being traversed."""
        return self._tree

    def execute(self):
        """ Perform the tour and return any result from post visit of root."""
        if len(self._tree) > 0:
            return self._tour(self._tree.root(), 0, [])  # start the recursion

    def _tour(self, p, d, path):
        """ Perform tour of subtree rooted at Position p.

        :param p : Position of current node being visited
        :param d : depth of p in the tree
        :param path: list of indices of children in path from root to p
        """
        self._hook_previsit(p, d, path)
        results = []
        path.append(0)  # add new index to end of path before recursion
        for c in self._tree.children(p):
            results.append(self._tour(c, d+1, path))  # recur on subtree
            path[-1] += 1
        path.pop()  # remove extraneous index from end of path
        answer = self._hook_postvisit(p, d, path, results)
        return answer

    def _hook_previsit(self, p, d, path):
        """ Visit Position p, before the tour of it's children.

        :param p : Position of current position being visited
        :param d : depth of p in the tree
        :param path : list of indices of children on path from root to p
        """
        pass

    def _hook_postvisit(self, p, d, path, results):
        """ Visit Position p, after the tour of it's children.

        :param p : Position of current position being visited
        :param d : depth of p in the tree
        :param path : list of indices of children on path from root to p
        :return : a list of values returned by _hook_postvisit(c) for each
        child c of p.
        """
        pass


class PreorderPrintIndentedTour(EulerTour):

    def _hook_previsit(self, p, d, path):
        print(2*d*' ' + str(p.element()))


class PreorderPrintIndentedLabeledTour(EulerTour):

    def _hook_previsit(self, p, d, path):
        label = '.'.join(str(j+1) for j in path)
        print('{0:s}{1:s}{2:s}'.format(2*d*' ', label, str(p.element())))


class ParenthesizeTour(EulerTour):

    def _hook_previsit(self, p, d, path):
        if path and path[-1] > 0:
            print ', ',
        print p.element(),
        if not self.tree().is_leaf(p):
            print '(',

    def _hook_postvisit(self, p, d, path, results):
        if not self.tree().is_leaf(p):
            print ')',


class BinaryEulerTour(EulerTour):
    """ Abstract base class for performing Euler tour of a binary tree.

    This version includes an additional _hook_invisit that is called after the
    tour of the left subtree (if any), yet before the tour of the right subtree
    (if any).

    Note: Right child is always assigned index 1 in path, even if no left
    sibling.
    """
    def _tour(self, p, d, path):
        results = [None, None]  # will update with results of recursions
        self._hook_previsit(p, d, path)
        if self._tree.left(p) is not None:
            path.append(0)
            results[0] = self._tour(self._tree.left(p), d+1, path)
            path.pop()
        self._hook_invisit(p, d, path)
        if self._tree.right(p) is not None:
            path.append(1)
            results[1] = self._tour(self._tree.right(p), d+1, path)
            path.pop()
        answer = self._hook_postvisit(p, d, path, results)
        return answer

    def _hook_invisit(self, p, d, path):
        """ Visit Position p, between tour of its left and right subtrees."""
        pass


class InorderTour(BinaryEulerTour):

    def _hook_invisit(self, p, d, path):
        print(p.element())


def construct_tree():
    t = LinkedBinaryTree()
    root = t._add_root('Trees')
    l = t._add_left(root, 'General trees')
    r = t._add_right(root, 'Binary trees')

    t1 = LinkedBinaryTree()
    root = t1._add_root('section1')
    left = t1._add_left(root, 'paragraph1')
    right = t1._add_right(root, 'paragraph2')

    t2 = LinkedBinaryTree()
    root = t2._add_root('section2')
    left = t2._add_left(root, 'paragraph1')
    right = t2._add_right(root, 'paragraph2')

    t._attach(l, t1, t2)
    return t

def construct_num_tree():
    t = LinkedBinaryTree()
    root = t._add_root(0)
    l = t._add_left(root, 1)
    r = t._add_right(root, 2)

    t1 = LinkedBinaryTree()
    root = t1._add_root(3)
    left = t1._add_left(root, 5)
    right = t1._add_right(root, 6)

    t2 = LinkedBinaryTree()
    root = t2._add_root(4)
    left = t2._add_left(root, 7)
    right = t2._add_right(root, 8)

    t._attach(l, t1, t2)
    return t


if __name__ == '__main__':
    t = construct_tree()
    ppit = PreorderPrintIndentedTour(t)
    ppit.execute()

    print('\n')
    ppilt = PreorderPrintIndentedLabeledTour(t)
    ppilt.execute()

    t = construct_num_tree()
    pt = ParenthesizeTour(t)
    pt.execute()

    print('\n')
    it = InorderTour(t)
    it.execute()

