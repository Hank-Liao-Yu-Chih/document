# ch3_14_1.py
import numpy as np

x1 = [0, 1, 2, 3, 4]
x2 = [5, 6, 7, 8, 9]
x3 = [10, 11, 12, 13, 14]
x4 = np.array([x1, x2, x3])
x5 = np.array([x4, x4])
print(f"x5[0,2,1] = {x5[0,2,1]}")
print(f"x5[0,1,3] = {x5[0,1,3]}")
print(f"x5[1,0,1] = {x5[1,0,1]}")
print(f"x5[1,1,4] = {x5[1,1,4]}")












 
