# MakeParallel
Simple Python library to have a function utilize multiple CPU cores

# Dependancies
* pandas >= 0.23.4
* numpy >= 1.15.4
* Python 3.7.1

# Installation
1. Download or clone repository: `git clone https://github.com/BrighBrigh/MakeParallel.git && cd MakeParallel/`
2. Install using pip: `pip install .`

# Usage

1. Import: `from MakeParallel import MakeParallel` or `from MakeParallel import parallelize`
2. In loops, call `MakeParallel(funct, args)` where `funct` is a function to be called to be made parallel and `args` is a tuple of arguments to be passed into the function. 
3. For pandas DataFrames, call `parallelize(df, function)` where `df` is a pandas DataFrame and `function` is an operation on a DataFrame taking only `df` as the argument.

# Example
```python
from MakeParallel import MakeParallel, parallelize
import pandas as pd

def testFunction(name, value):
  print(name + str(value))

def testFunction2(df):
  return df['null'].apply(lambda x : x+1)
  
list = ['bob', 'sue', 'joe']
val = 9
for name in list:
  arg = name, val
  MakeParallel(testFunction, arg)

data = pd.read_csv('null.csv')
data = parallelize(data, testFunction2)
```
