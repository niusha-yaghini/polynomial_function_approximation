import numpy as np
import pandas as pd

columns = ['tree','mae']

tree = []
mae = []

# (tree_mae) is a tuple 
def printing(tree_mae):
    for i in tree_mae:
        tree.append(i[0])
        mae.append(i[1])
    df = pd.DataFrame(list(zip(tree, mae)), columns=columns)
    