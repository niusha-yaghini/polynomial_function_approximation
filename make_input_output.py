def making_x_compare(domain, stop_size):
    x = []
    i = domain[0]
    while (i<=domain[1]):
        x.append(i)
        i+=stop_size
    return x

def making_y_compare1(x):
    y = [(i**2) for i in x]
    return y

def making_y_compare2(x):
    y = [ (4*(i**4) + 3*(i**3) + 2*(i**2) + i) for i in x]
    return y
    

if __name__ == "__main__":
    
    f = open('in_out2.txt', 'w')

    f.write("our function is: 4*(x^4) + 3*(x^3) + 2*(x^2) + x \n")

    amount = 100
    stop_size = 0.1
    domain = (0.1, 10)
    x = making_x_compare(domain, stop_size)
    y = making_y_compare2(x)

    for i in range(amount):
        f.write(f"{x[i]}, {y[i]}\n")
        
    f.close() 