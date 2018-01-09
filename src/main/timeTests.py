'''
Created on Feb 4, 2014

@author: Starfox
'''

import time
import random
from QuickSort.Algorithm import quickSort

randToSort = random.sample(xrange(0, 10000), 1000)

start = time.time()
print(quickSort(randToSort))
elapsed = (time.time() - start)


