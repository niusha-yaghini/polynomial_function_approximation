import tree
import matplotlib.pyplot as plt
import children    
import print_function


def draw_average_mae(x_generation_number, y_average_mae_of_each, given_function):
    fig, ax = plt.subplots()
    average_of_each, = plt.plot(x_generation_number, y_average_mae_of_each, label='average of each generation')
    ax.set_title(f"function = {given_function}, population = {amount_of_trees}")
    ax.legend(handles=[average_of_each])
    name = f"average_{photo_number}_" + str(amount_of_trees) + '.png'

    plt.savefig(name)
    plt.show()

def draw_best_mae(x_generation_number, y_best_mae_of_each, y_best_mae_of_all, given_function, y_min_mae):
    
    fig, ax = plt.subplots()
    best_of_each,  = plt.plot(x_generation_number, y_best_mae_of_each, label='best of this generation')
    best_of_all, = plt.plot(x_generation_number, y_best_mae_of_all, label='best of all generations since now')

    ax.set_title(f"function: {given_function}, population_num: {amount_of_trees}, generations_num: {amount_of_generations}, min_mae: {y_min_mae}")
    ax.legend(handles=[best_of_each, best_of_all])
    name = f"result_{photo_number}_" + str(amount_of_trees) + '.png'

    print("best mae: ", y_min_mae)

    plt.savefig(name)
    plt.show()

def Genetic(input_file_name):
    
    f = open(f'{input_file_name}', 'r')
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
    parents_average_mae, parents_best_mae, best_parent_tree = tree.calculating_mae(list_of_parents, X, Y)
    
    # making lists for showing 
    x_generation_number = []
    y_average_mae_of_each = []
    y_best_mae_of_each = []
    y_best_mae_of_all = []
    y_best_tree = []
    y_min_mae = None
    
    # appending 0 generation information
    x_generation_number.append(0)
    y_average_mae_of_each.append(parents_average_mae)
    y_best_mae_of_each.append(parents_best_mae)
    y_best_mae_of_all.append(parents_best_mae)
    y_best_tree.append(best_parent_tree)

    for i in range(amount_of_generations):
    
        print(f"population number {i+1}")
        list_of_children = children.making_children(list_of_parents, k, pc, pm)
        average_mae, best_mae, best_tree = tree.calculating_mae(list_of_children, X, Y)
        list_of_parents = list_of_children
        
        x_generation_number.append(i)
        y_best_tree.append(best_tree)
        y_best_mae_of_each.append(best_mae)
        y_min_mae = min(y_best_mae_of_each)
        print("best mae so far: ", y_min_mae)
        y_best_mae_of_all.append(y_min_mae)
        y_average_mae_of_each.append(average_mae)

    final_best_tree = None
    for i in y_best_tree:
        if i.mae==y_min_mae:
            final_best_tree = i

    final_best_tree_in_order = tree.to_math_string(final_best_tree.root)            

    draw_best_mae(x_generation_number, y_best_mae_of_each, y_best_mae_of_all, given_function, y_min_mae)
    
    print_function.print_func(X, Y, final_best_tree, given_function, final_best_tree_in_order, photo_number)

    draw_average_mae(x_generation_number, y_average_mae_of_each, given_function)


if __name__ == "__main__":
    
    photo_number = 12
    
    # parameters
    amount = 100

    # population size (0)
    amount_of_trees = 100
    max_depth = 12

    k = 3 # k tournoment parameter
    pc = 0.8 # the probblity of cross-over
    pm = 0.8 # the probblity of mutation

    amount_of_generations = 50
    
    input_file_name = 'in_out2.txt'
    
    Genetic(input_file_name)

    print()
    
    # power_domain = (0.25, 4)
    # power_rate = 0.25    

    # for now the new generation is the children

    print()