import pytest
from stack_iterator import Stack
from stack_iterator import InvalidOperationError


def test_exists():
    assert Stack


# @pytest.mark.skip("TODO")
def test_push_onto_empty():
    s = Stack()
    s.push("apple")
    actual = s.top.value
    expected = "apple"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_push_onto_full():
    s = Stack()
    s.push("apple")
    s.push("banana")
    s.push("cucumber")
    actual = s.top.value
    expected = "cucumber"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_pop_single():
    s = Stack()
    s.push("apple")
    actual = s.pop()
    expected = "apple"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_pop_some():
    s = Stack()

    s.push("apple")
    s.push("banana")
    s.push("cucumber")

    s.pop()

    actual = s.pop()
    expected = "banana"

    assert actual == expected


# @pytest.mark.skip("TODO")
def test_pop_until_empty():
    s = Stack()
    s.push("apple")
    s.push("banana")
    s.push("cucumber")
    s.pop()
    s.pop()
    s.pop()
    actual = s.is_empty()
    expected = True
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_peek():
    s = Stack()
    s.push("apple")
    s.push("banana")
    actual = s.peek()
    expected = "banana"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_peek_empty():
    s = Stack()
    with pytest.raises(InvalidOperationError) as e:
        s.peek()

    assert str(e.value) == "Method Not Allowed on an Empty Stack"


# @pytest.mark.skip("TODO")
def test_pop_empty():
    s = Stack()
    with pytest.raises(InvalidOperationError) as e:
        s.pop()

    assert str(e.value) == "Method Not Allowed on an Empty Stack"


def test_for_in():
  new_stack = Stack()
  new_stack.push("Value 1")
  new_stack.push("Value 2")
  new_stack.push("Value 3")

  values_list = []

  for item in new_stack:
    values_list.append(item)

  assert values_list == ["Value 3","Value 2","Value 1"]

def test_list_comp():
  new_stack = Stack()
  new_stack.push("Value 1")
  new_stack.push("Value 2")
  new_stack.push("Value 3")

  cap_values = [item.upper() for item in new_stack]

  assert cap_values == ["VALUE 3","VALUE 2","VALUE 1"]

def test_next():
  new_stack = Stack()
  new_stack.push("Value 1")
  new_stack.push("Value 2")
  new_stack.push("Value 3")  

  iterator = iter(new_stack)

  assert next(iterator) == "Value 3"
  assert next(iterator) == "Value 2"
  assert next(iterator) == "Value 1"

def test_stop_iteration():
  new_stack = Stack()
  new_stack.push("Value 1")
  new_stack.push("Value 2")
  new_stack.push("Value 3")

  iterator = iter(new_stack)

  with pytest.raises(StopIteration):
    while True:
      item = next(iterator)


def test_str():
  new_stack = Stack()
  new_stack.push("Value 1")
  new_stack.push("Value 2")
  new_stack.push("Value 3") 

  assert str(new_stack) == "[ Value 3 ] <- [ Value 2 ] <- [ Value 1 ] <- None"

def test_equals():
  stack_a = Stack()
  stack_a.push("Value 1")
  stack_a.push("Value 2")
  stack_a.push("Value 3") 

  stack_b = Stack()
  stack_b.push("Value 1")
  stack_b.push("Value 2")
  stack_b.push("Value 3") 

  assert stack_a == stack_b

def test_get():
  new_stack = Stack()
  new_stack.push("Value 1")
  new_stack.push("Value 2")
  new_stack.push("Value 3") 

  assert new_stack[0] == "Value 3"

def test_out_of_range():
  new_stack = Stack()
  new_stack.push("Value 1")
  new_stack.push("Value 2")
  new_stack.push("Value 3")

  with pytest.raises(IndexError):
    new_stack[50]

def test_truthy_falsy():
  new_stack = Stack()
  new_stack.push("Value 1")

  assert bool(new_stack) == True

  second_stack = Stack()

  assert bool(second_stack) == False