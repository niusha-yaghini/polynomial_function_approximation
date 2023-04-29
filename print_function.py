import matplotlib.pyplot as plt
import tree


def result(t, list_x):    
    trees_y = []
    for single_x in list_x:
        flag = False
        t_y = tree.calculator(t.root, single_x, flag)
        if(flag==True or t_y>100000 or t_y<-100000):
            t_y = 100000

        trees_y.append(t_y)
    return trees_y

def print_func(list_x, actual_y, predicted_tree, actual_f, predicted_f, photo_number):

    predicted_y = result(predicted_tree, list_x)

    fig, ax = plt.subplots()
    actual_function,  = plt.plot(list_x, actual_y, label='actual function')
    predicted_function, = plt.plot(list_x, predicted_y, label='predicted function')

    ax.set_title(f"actual function: {actual_f}, predicted function: {predicted_f}")
    ax.legend(handles=[actual_function, predicted_function])
    name = f"exact_function_{photo_number}_" + '.png'

    plt.savefig(name)
    plt.show()
    
    print()