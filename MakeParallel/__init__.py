from multiprocessing import Process, cpu_count, Pool
import os
import pandas as pd
import numpy as np

def MakeParallel(function, argu):
    p = Process(target=function, args=argu)
    p.start()

def parallelize(data, func):
    cores = cpu_count() #Number of CPU cores on your system
    partitions = cores #Define as many partitions as you want
    data_split = np.array_split(data, partitions)
    pool = Pool(cores)
    data = pd.concat(pool.map(func, data_split))
    pool.close()
    pool.join()
    return data
