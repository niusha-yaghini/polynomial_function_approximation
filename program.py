import numpy as np
import random as rnd
import math
import tree
import print_tree_mae
import copy
import matplotlib.pyplot as plt
import children    
    

if __name__ == "__main__":
    
    # parameters
    amount = 100

    # population size (0)
    amount_of_trees = 200
    max_depth = 6

    k = 3 # k tournoment parameter
    pc = 0.5 # the probblity of cross-over
    pm = 0.5 # the probblity of mutation

    amount_of_generations = 100
    
    # power_domain = (0.25, 4)
    # power_rate = 0.25
    
    # using domain
    f = open('in_out2.txt', 'r')
    given_function = f.readline().split(':')[1]
    X = []
    Y = []
    for i in range(amount):
        a = f.readline().split(',')
        X.append(float(a[0]))
        Y.append(float(a[1]))
        
        
    # population number zero
    print("population number 0\n")
    list_of_parents = tree.all_trees(amount_of_trees, max_depth)
    parents_average_mae, parents_best_mae, best_tree = tree.calculating_mae(list_of_parents, X, Y)
    
    # making lists for showing 
    x_generation_number = []
    y_average_of_each = []
    y_best_mae_of_each = []
    y_best_mae_of_all = []
    y_best_tree = []
    
    # y_last_best = 0
    
    for i in range(amount_of_generations):
    
        print(f"population number {i+1}")
        list_of_children = children.making_children(list_of_parents, k, pc, pm)
        average_mae, best_mae, best_tree = tree.calculating_mae(list_of_children, X, Y)
        list_of_parents = list_of_children
        
        x_generation_number.append(i)
        y_best_tree.append(best_tree)
        y_best_mae_of_each.append(best_mae)
        y_best_mae_of_all.append(min(y_best_mae_of_each))
        y_average_of_each.append(average_mae)


    final_best_tree = None
    mae = float('inf')
    for i in y_best_tree:
        if i.mae<mae:
            final_best_tree = i
            mae = i.mae

    fig, ax = plt.subplots()
    # plt.figure(figsize=(10,6))
    best_of_each,  = plt.plot(x_generation_number, y_best_mae_of_each, label='best of this generation')
    best_of_all, = plt.plot(x_generation_number, y_best_mae_of_all, label='best of all generations since now')

    # ax.text("last predicted y: ", min(y_best_of_all))
    ax.set_title(f"function: {given_function}, population: {amount_of_trees}, amount_of_generations: {amount_of_generations} , my genetic believes: {final_best_tree.in_order}")
    ax.legend(handles=[best_of_each, best_of_all])
    name = "result_5_" + str(amount_of_trees) + '.png'

    print("the function that my genetic believes: ", final_best_tree.in_order)
    print("best mae: ", min(y_best_mae_of_all))

    plt.savefig(name)
    plt.show()
    
    print()
    
    fig, ax = plt.subplots()
    average_of_each, = plt.plot(x_generation_number, y_average_of_each, label='average of each generation')
    ax.set_title(f"function = {given_function}, population = {amount_of_trees}")
    ax.legend(handles=[average_of_each])
    name = "average_4_" + str(amount_of_trees) + '.png'

    plt.savefig(name)
    plt.show()

    # for now the new generation is the children

    print()