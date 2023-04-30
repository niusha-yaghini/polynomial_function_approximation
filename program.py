import tree
import matplotlib.pyplot as plt
import children    
import print_function
import random as rnd


def draw_average_mae(x_generation_number, y_average_mae_of_each, given_function):
    fig, ax = plt.subplots()
    average_of_each, = plt.plot(x_generation_number, y_average_mae_of_each, label='average of each generation')
    ax.set_title(f"function = {given_function}, population = {population_size}")
    ax.legend(handles=[average_of_each])
    name = f"average_{photo_number}_" + str(population_size) + '.png'

    plt.savefig(name)
    plt.show()

def draw_best_mae(x_generation_number, y_best_mae_of_each, y_best_mae_of_all, given_function, y_min_mae):
    
    fig, ax = plt.subplots()
    best_of_each,  = plt.plot(x_generation_number, y_best_mae_of_each, label='best of this generation')
    best_of_all, = plt.plot(x_generation_number, y_best_mae_of_all, label='best of all generations since now')

    ax.set_title(f"function: {given_function}, population_num: {population_size}, generations_num: {amount_of_generations}, min_mae: {y_min_mae}")
    ax.legend(handles=[best_of_each, best_of_all])
    name = f"result_{photo_number}_" + str(population_size) + '.png'

    print("best mae: ", y_min_mae)

    plt.savefig(name)
    plt.show()

def Termination_condition(y_min_mae):
    if(y_min_mae<0.0001): return True
    else: return False

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
    list_of_parents = tree.all_trees(population_size, max_depth)
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
    y_min_mae = min(y_best_mae_of_each)
    print("best mae so far: ", y_min_mae)
    y_best_mae_of_all.append(parents_best_mae)
    y_best_tree.append(best_parent_tree)

    for i in range(amount_of_generations):
        
        if(Termination_condition(y_min_mae)):
            return
    
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

def Genetic_for_compare(input_file_name):
    
    f = open(f'{input_file_name}', 'r')
    given_function = f.readline().split(':')[1]
    X = []
    Y = []
    for i in range(amount):
        a = f.readline().split(',')
        X.append(float(a[0]))
        Y.append(float(a[1]))
        
    # population number zero
    print("population number 0")
    list_of_parents = tree.all_trees(population_size, max_depth)
    parents_average_mae, parents_best_mae, best_parent_tree = tree.calculating_mae(list_of_parents, X, Y)
    
    y_best_mae_of_each = []
    
    y_best_mae_of_each.append(parents_best_mae)

    for i in range(amount_of_generations):
        
        # if(Termination_condition(y_min_mae)):
        #     return
    
        print(f"population number {i+1}")
        list_of_children = children.making_children(list_of_parents, k, pc, pm)
        average_mae, best_mae, best_tree = tree.calculating_mae(list_of_children, X, Y)
        list_of_parents = list_of_children
        
        y_best_mae_of_each.append(best_mae)
        
    y_min_mae = min(y_best_mae_of_each)
    return y_min_mae

def compare_tournoment_roulette(iteration, input_file_name):

    f = open('compare_tournoment_roulettewheel.txt', 'a')
    f.write("roulette wheel \n")
    
    roulettewheel = []
    for i in range(iteration):
        print(f"iteration {i}\n")
        y_min = Genetic_for_compare(input_file_name)
        roulettewheel.append(y_min)
        f.write(f"best mae of iteration {i} is: {y_min}\n")
    
    avg = sum(roulettewheel)/len(roulettewheel)
    f.write(f"average is: {avg}")
    f.close()
    
def compare_completed_and_uncompleted_tree(input_file_name, iteration):
    f = open('completed_and_uncompleted_tree.txt', 'a')
    # f.write("completed tree max depth = 3 \n")
    # f.write("uncompleted tree max depth = 12 \n")
    
    completed_tree = []
    for i in range(iteration):
        print(f"iteration {i}\n")
        y_min = Genetic_for_compare(input_file_name)
        completed_tree.append(y_min)
        f.write(f"best mae of iteration {i} is: {y_min}\n")
    
    avg = sum(completed_tree)/len(completed_tree)
    f.write(f"average is: {avg}")
    f.close()

    
def Genetic_compare_max_depth(input_file_name, max_depth_domain, population_size, iteration):
    
    f = open(f'{input_file_name}', 'r')
    given_function = f.readline().split(':')[1]
    X = []
    Y = []
    for i in range(amount):
        a = f.readline().split(',')
        X.append(float(a[0]))
        Y.append(float(a[1]))
    
    f = open('compare_max_depths(complete_tree).txt', 'a')
    
    for i in range(max_depth_domain[0], max_depth_domain[1]):
        maes = []
        f.write(f"\n \nmax depth is: {i}\n")
        print(f"max depth is: {i}\n")

        for j in range(iteration):
            print(f"iteration number {j}")
            max_depth = i
            list_of_parents = tree.all_trees(population_size, max_depth)
            parents_average_mae, parents_best_mae, best_parent_tree = tree.calculating_mae(list_of_parents, X, Y)
            f.write(f"best mae of iteration {j} is: {parents_best_mae}\n")
            maes.append(parents_best_mae)
        avg = sum(maes)/len(maes)
        f.write(f"average is: {avg}")

    f.close()
    
def make_max_depths_diagram():
    X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    Y = [8061.8780849116165,6537.099422319303,5540.937601493546,4746.9959186147435,
        4727.1649867168335,4355.375348877292,3727.133688684925,3713.400576959709,
        3618.9511372586976,3479.8047431170526,3607.4952489767193,2958.849237901331,
        3081.586960965158,3389.7723867068007,3057.646864662037,3661.8409771767106, 
        3469.532412653947,3141.013927733322,3301.489759040152,3284.0203830930204]
    
    fig, ax = plt.subplots()
    max_depths,  = plt.plot(X, Y)

    ax.set_title('max depths and best mae of pop0')
    ax.legend(handles=[max_depths])
    name = "compare_max_depths" + '.png'

    plt.savefig(name)
    plt.show()
    
def make_max_depths_complete_tree_diagram():
    X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Y = [7948.970115975988,4216.3952709425275,
        3150.2410365787528,3185.476849321872,
        3399.380433220902,4108.563640193231,
        4879.852697585542,5085.764860250136,
        5459.362167282123,5625.37985480556]
    
    fig, ax = plt.subplots()
    max_depths,  = plt.plot(X, Y)

    ax.set_title('max depths and best mae of pop0')
    ax.legend(handles=[max_depths])
    name = "compare_max_depths(completed_tree)" + '.png'

    plt.savefig(name)
    plt.show()

    
if __name__ == "__main__":
    
    # rnd.seed(1)
    
    photo_number = 14
    
    # parameters
    amount = 100

    # population size (0)
    population_size = 100
    max_depth = 3

    k = 3 # k tournoment parameter
    pc = 0.8 # the probblity of cross-over
    pm = 0.8 # the probblity of mutation(leaf_mutation)

    amount_of_generations = 50
    
    input_file_name = 'in_out2.txt'
    
    iteration = 20
    compare_completed_and_uncompleted_tree(input_file_name, iteration)
    
    
    # max_depth_domain = (1, 11)
    # iteration = 100
    # Genetic_compare_max_depth(input_file_name, max_depth_domain, population_size, iteration)
    # make_max_depths_diagram()
    
    # Genetic_compare_max_depth(input_file_name, max_depth_domain, population_size, iteration)
    # make_max_depths_complete_tree_diagram()

    # Genetic(input_file_name)
    # iteration = 40
    # compare_tournoment_roulette(iteration, input_file_name)

    print()
    
    # power_domain = (0.25, 4)
    # power_rate = 0.25    

    # for now the new generation is the children

    print()