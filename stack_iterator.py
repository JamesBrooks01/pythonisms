class Stack:
  def __init__(self):
    self.top = None
    self.length = 0

  def __iter__(self):
    def value_generator():
      current = self.top
      while current:
        yield current.value
        current = current.next
    return value_generator()

  def __str__(self):
    return_string = self.concat_string()
    if self.top == None:
      return "NONE"
    return f"{return_string}None"

  def __len__(self):
    return self.length

  def __eq__(self, another):
    return list(self) == list(another)

  def __getitem__(self, idx):
    if len(self) == 0:
      raise IndexError
    if idx < 0:
      raise IndexError

    for i, item in enumerate(self):
      if i == idx:
        return item
    
    raise IndexError

  def __bool__(self):
    return not (self.top == None)

  def concat_string(self):
    stack_item = self.top
    stack_string = ""
    while stack_item:
      stack_string += f"[ {stack_item.value} ] <- "
      stack_item = stack_item.next
    return stack_string

  def push(self, value):
    self.top = Node(value, self.top)
    self.length += 1

  def pop(self):
    if not self.top:
      raise InvalidOperationError("Method Not Allowed on an Empty Stack")
    previous_top = self.top
    self.top = self.top.next
    previous_top.next = None
    self.length -= 1
    return previous_top.value

  def peek(self):
    if not self.top:
      raise InvalidOperationError("Method Not Allowed on an Empty Stack")
    return self.top.value

  def is_empty(self):
    if self.top == None:
      return True
    else:
      return False

class Node:
  def __init__(self, data, next=None):
    self.value = data
    self.next = next

class InvalidOperationError(Exception):
    pass
