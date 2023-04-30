import random as rnd

def roulette_wheel_selection(p_trees):
    # how much the mae is smaller the probbility of choosing it increases
    
    couple_parent = []
    sum_mae = sum([(1/t.mae) for t in p_trees])
    
    for i in range(2):
        
        #this is going to choose a number between 0 and 1    
        p = rnd.random()
        s = 0
        
        flag = True
        for t in p_trees:
            if(flag):
                if(p < (((1/t.mae)/sum_mae) + s)):
                    couple_parent.append(t)
                    flag = False
                else:
                    s += 1/t.mae    
    return couple_parent[0], couple_parent[1]       
