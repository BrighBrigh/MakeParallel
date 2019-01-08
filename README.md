# MakeParallel
Simple Python library to have a function utilize multiple CPU cores

# Installation
1. Download or clone repository
2. `cd MakeParallel/`
3. `pip install .`

# Usage

1. Import: `from MakeParallel import MakeParallel`
2. Call `MakeParallel(funct, args)` where `funct` is a function to be called to be made parallel and `args` is a tuple of arguments to be passed into the function.

# Example
```python
from MakeParallel import MakeParallel

def testFunction(name, value):
  print(name + str(value))
  
list = ['bob', 'sue', 'joe']
val = 9
for name in list:
  arg = name, val
  MakeParallel(testFunction, arg)
```
