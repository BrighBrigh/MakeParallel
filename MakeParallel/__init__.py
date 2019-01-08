from multiprocessing import Process
import os
import pandas as pd

def MakeParallel(function, argu):
    p = Process(target=function, args=argu)
    p.start()
