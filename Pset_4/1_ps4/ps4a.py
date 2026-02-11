# Problem Set 4A
# Name:
# Collaborators:

from tree import Node # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the test named test_data_representation should pass.
tree1 = Node(8,Node(2,Node(1),Node(6)),Node(10))
tree2 = Node(7,Node(2,Node(1),Node(5,Node(3),Node(6))),Node(9,Node(8),Node(10))) 
tree3 = Node(5,Node(3,Node(2),Node(4)),Node(14,Node(12),Node(21,Node(20),Node(26))))

def find_tree_height(tree):
    '''
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer depth of the tree
    '''
    if tree==None:
        return -1 # Edge case 1: empty tree
    elif tree.get_left_child()==None and tree.get_right_child()==None:
        return 0
    else:
        return 1+max(find_tree_height(tree.get_left_child()),find_tree_height(tree.get_right_child()))

def is_heap(tree, compare_func):
    '''
    Determines if the tree is a max or min heap depending on compare_func
    Inputs:
        tree: An element of type Node constructing a tree
        compare_func: a function that compares the child node value to the parent node value
            i.e. op(child_value,parent_value) for a max heap would return True if child_value < parent_value and False otherwise
                 op(child_value,parent_value) for a min meap would return True if child_value > parent_value and False otherwise
    Output:
        True if the entire tree satisfies the compare_func function; False otherwise
    '''
    if tree==None:
        return True
    if tree.get_left_child()!=None:
        if not is_heap(tree.get_left_child(),compare_func):
            return False
        if not compare_func(tree.get_left_child().get_value(),tree.get_value()):
            return False
    if tree.get_right_child()!=None:
        if not is_heap(tree.get_right_child(),compare_func):
            return False
        if not compare_func(tree.get_right_child().get_value(),tree.get_value()):
            return False
    return True
    # -----------------
    # Incorrect version
    # -----------------
    # if tree==None:
    #     return True
    # elif tree.get_left_child()==None and tree.get_right_child()==None:
    #     return True
    # else:
    #     if is_heap(tree.get_left_child(),compare_func) and compare_func(tree.get_left_child().get_value(),tree.get_value()) and is_heap(tree.get_right_child(),compare_func) and compare_func(tree.get_right_child().get_value(),tree.get_value):
    #         return True
    #     return False
    # Edge case 2: Incomplete binary tree(None.get_value() would raise an error)



if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below if you do not add your own code
    pass