class LinkedList:
  def __init__(self,collection=None):
    self.head = None
    self.length = 0
    for element in reversed(collection):
      self.insert(element)

  def __iter__(self):
    def value_generator():
      current = self.head
      while current:
        yield current.value
        current = current.next
    return value_generator()

  def __str__(self):
      return_string = self.concat_list()
      if self.head == None:
          return "NULL"
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
    
    for i,item in enumerate(self):
      if i == idx:
        return item
    
    raise IndexError
  
  def concat_list(self):
    list_item = self.head
    linked_list_string = ""
    while list_item is not None:
        linked_list_string += f"[ {list_item.value} ] -> "
        list_item = list_item.next
    return linked_list_string

  def insert(self, value):
      newNode = Node(value, self.head)
      self.head = newNode
      self.length += 1

  def append(self,value):
    current = self.head
    while current:
      if current.next == None:
        current.next = Node(value,None)
        self.length += 1
        break
      current = current.next

class Node:
    def __init__(self, data, next=None):
        self.value = data
        self.next = next