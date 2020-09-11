import numpy as np
from numpy.random import randn

x = randn()
if x > 1:
    print (x , "Greater than 1")
elif x >= -1:
    print (x, "Between -1 and 1")
else:
    print (x, "Less than 1")
    
