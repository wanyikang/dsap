# -*- coding: utf-8 -*-
# len:
#   There is an instance variable in the LinkedBinaryTree to track the number
#   of all nodes in the tree, so len method is just return the instance
#   variable value. The running time is O(1).
#
# is_empty:
#   Like len method, it alse use the instance variable to check if tree is
#   empty. The running time is O(1).
#
# root:
#   There is an instance variable `_root` in the tree to track the root, so
#   root method is just return the position object of the _root variable. The
#   running time is O(1).
#
# parent:
#   There is a instance variable `_parent` in the _Node object within tree to
#   track the parent of this node, and alse a `_left` to track the left child
#   of this node, and a `_right` to track the right child. So when we want to
#   get the parent, left child, right child of a node, we just follow the
#   repective instance variable to get them. The running time is O(1).
#
# left:
#   Like parent, the running time is O(1).
#
# right:
#   Like parent, the running time is O(1).
#
# sibling:
#   Like parent, when we want to find the sibling of a node, we can get parent,
#   and then get all two children, and then  we can find the sibling. The
#   running time is O(1).
#
# children:
#   Like parent, we can get left child and right child of a node. The running
#   time is O(1).
#
# num_children:
#   Like children, the running time is O(1)
#
# is_root:
#   Like root, the running time is O(1).
#
# is_leaf:
#   Like parent. We can get all two children of a node, so we can check it's
#   leaf or not.
#
# depth:
#   The depth of node N is one more than the depth of it's parent, and depth of
#   root is 0. So we can recursive it's parent node to get the depth of node N.
#   The running time depends on show deep the node is in the tree, is O(dp +
#   1), dp means depth of node N.
#
# height:
#   The height of node N is one more than the maximum of it's children's
#   height, the height of leaf is 0. Height of tree is height of root node. We
#   can recursive it's children's height to get the height of root node. The
#   running time is O(n).
#
# add_root:
#   Just create a _Node node and make it be root, raise an error if already
#   have an root, and increase the size too. The running time is O(1).
#
# add_left:
#   Create a _Node node and make it be left node of p, raise error if p already
#   have a left child, then increase the size. The running time is O(1).
#
# add_right:
#   Create a _Node node and make it be right node of p, raise error if p already
#   have a right child, then increase the size. The running time is O(1).
#
# replace:
#   Get the node of p and replace the element, then return the old one. The
#   running time is O(1).
#
# delete:
#   Delete the node represented by p and move the child node up, consider
#   deleting root and p having two children. The running time is O(1).
#
# attach:
#   Make t1 be left subtree of p, make t2 be right subtree of p, and do not
#   forget to check p is leaf or not and t1, t2 is the same type of t or not.
#   The running time is O(1).
#
