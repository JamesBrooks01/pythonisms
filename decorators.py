from functools import wraps
from time import time, sleep

def function_timer(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    time1 = time()
    return_value = func(*args, **kwargs)
    time2 = time()
    print(f'Function {func.__name__} executed in {(time2 -  time1):.4f}s')
    return return_value
  return wrapper

def function_slower(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    sleep(1)
    return func(*args, **kwargs)
  return wrapper

def list_converter(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    result = func(*args, **kwargs)
    return [result]
  return wrapper

def string_converter(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    result = func(*args, **kwargs)
    return str(result)
  return wrapper

def first_input_validator(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    print(f'Type of Arg is {type(args[0])}')
    return func(*args, **kwargs)
  return wrapper

@function_timer
@function_slower
def tester_function(txt):
  return txt

@first_input_validator
@function_timer
def long_loop(n):
  for i in range(n):
    for j in range(100000):
      i*j

@string_converter
# @list_converter
def number_adder(x,y):
  return (x + y)

if __name__ == "__main__":
  # print(tester_function("This is a test string"))
  # print(long_loop(5))
  # print(number_adder(10,15))
  pass
