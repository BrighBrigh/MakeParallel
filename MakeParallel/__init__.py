from multiprocessing import Process, cpu_count, Pool
import numpy as np
import pandas as pd

### Use in a loop to parallelize the loop
def MakeParallel(function, argu):
    p = Process(target=function, args=argu)
    p.start()


### Use this function to parallelize pandas DataFrame operations
def parallelize(data, func):
    cores = cpu_count() #Number of CPU cores on your system
    partitions = cores #Define as many partitions as you want
    data_split = np.array_split(data, partitions)
    pool = Pool(cores)
    data = pd.concat(pool.map(func, data_split))
    pool.close()
    pool.join()
    return data
