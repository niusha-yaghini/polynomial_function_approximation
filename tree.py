import random
from sklearn.metrics import mean_squared_error
import math
import numpy as np

# choosing the operator
def my_operator():
    op = ['+', '-', '*', '**']
    return(random.choice(op))

def power_list():
    power_domain = (0.25, 4)
    power_rate = 0.25
    
    p = np.arange(power_domain[0], power_domain[1], power_rate)
    return p

def coefficient_list():
    coefficient_domain = (0.1, 50.4)
    coefficient_rate = 0.1

    c = np.arange(coefficient_domain[0], coefficient_domain[1], coefficient_rate)
    return c
    
class Node:
    # my node class 
    
    def __init__(self, _depth, _operator, _children = [], _is_leaf = False):
        self.operator = _operator
        self.depth = _depth
        self.children = _children
        self.is_leaf = _is_leaf

class Tree:
    # my tree class

    def __init__(self, _max_depth = None):
        self.max_depth = _max_depth
        self.root = None
        self.in_order = None
        self.mae = None
        self.power_l = power_list()
        self.coefficient_l = coefficient_list()
        
    def _fit(self):
        self.root = self._grow_tree(self.max_depth)
        
    def _grow_tree(self, max_depth, CS=2):
        
        # choosing a random depth each time (between 0 to max given depth)
        depth = random.randint(0, max_depth)
          
        # choosing the operator for current node
        x = my_operator()
        
        children = []
        
        # building the tree base on current depth and children needed
        if(depth==0):
            x = random.choice(self.coefficient_l)
        else:
            if(x=='**'):
                n1 = Node(0, 'x', [])
                n1.is_leaf = True
                n2 = Node(0, random.choice(self.power_l), [])
                n2.is_leaf = True
                
                children.append(n1)
                children.append(n2)
                
                depth = 1
            else:
                for i in range(CS):
                    children.append(self._grow_tree(depth-1))

        # making the node 
        n = Node(depth, x, children)
        if(depth==0):
            n.is_leaf = True
        return n          

    def print_tree(self):
        # making the inorder show of our tree
        self.in_order = self.to_math_string(self.root)
   
    def to_math_string(self, node):
        if(node.is_leaf):
            return f"{node.operator}"
        else:
            if(len(node.children)) == 1:
                return f"{node.operator}{self.to_math_string(node.children[0])}"
            else:
                return f"{self.to_math_string(node.children[0])}{node.operator}{self.to_math_string(node.children[1])}"

def tree_making(max_depth):  
    # making each of our trees

    t = Tree(max_depth)
    t._fit()
    t.print_tree()
    return t     
        
def all_trees(amount, max_depth):
    # making a list of all random trees (generation 0)

    trees = []
    for i in range(amount):
        tree = tree_making(max_depth)
        trees.append(tree)
    return trees
        
def calculator(root, x, flag):
    # doing the calculating for each function that we have made with given input
    
    if(flag):
        return
    
    if(root.is_leaf):
        if(root.operator == 'x'): 
            return x
        else: 
            return root.operator
    else:
        
        left_val = calculator(root.children[0], x, flag)
        right_val = calculator(root.children[1], x, flag)


        if (root.operator == '+'):
            return left_val + right_val
        elif (root.operator == '-'):
            return left_val - right_val
        elif (root.operator == '*'):
            return left_val * right_val
        elif (root.operator == '**'):
            if(left_val==0 and right_val<0):
                flag = True
                return 1
            else:
                return left_val**right_val
                # if(right_val==0):
                #     return 1
                # x = 1
                # i = 0
                # while(not flag and i<right_val):
                #     x = x*left_val
                #     i+=1
                #     if(x>100000 or x<-100000):
                #         flag = True
                #         return 1
                # return x
        
def mean_abs_error(actual_y, predicted_y):
    amount = len(predicted_y)
    sum = 0
    for i in range(amount):
        sum += abs(predicted_y[i]-actual_y[i])
        # sum+=a
        # print("actual y =", format(actual_y[i], ".2f"), "predicted y =", format(predicted_y[i], ".2f"), "mae is =", format(a, ".2f"))

    return sum/amount
        
def _mae(tree, list_x, list_y):
    # calculating each tree mae with given inputs and outputs
    
    trees_y = []
    for single_x in list_x:
        flag = False
        t_y = calculator(tree.root, single_x, flag)
        if(flag==True or t_y>100000 or t_y<-100000):
            t_y = 100000

        trees_y.append(t_y)

    # print(tree.in_order)
    mae = mean_abs_error(list_y, trees_y)
    # print()
    # if(mae<0.00001):
    #     mae = 0
    return mae

def calculating_mae(tree_list, X, Y):
    # calculating the average-mae and best-mae for all of our trees and given inputs and outputs
    
    i = 1
    mae_sum = 0
    best_mae = float('inf')
    best_tree = None
    for t in tree_list:
        t.mae = _mae(t, X, Y)
        mae_sum += t.mae
        if (t.mae<best_mae):
            best_mae = t.mae
            best_tree = t
        print(f"tree number {i} = {t.in_order} and its mae is = {t.mae}")
        i += 1

    return mae_sum/i, best_mae, best_tree