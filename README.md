# LAB - Class 42

## Project: Pythonisms

## Author: James Brooks

## Findings

- Through this assignment I have found the most use out of the dunder methods as I can see how they could be of the most use. The use of the `__iter__` dunder with a generator in particular allowing for a for/in loop to work with the data structure is one that would be quite useful.
  - I chose to implement the following dunders into a copy of the Stack code;
    - Iteration through `__iter__` and a Generator
    - A string representation through `__str__`
    - A length of it through modifying the push/pop methods and adding a length attribute and returning it under the `__len__` dunder
    - Capability of comparing if two stacks are equal through `__eq__`
    - Can get a specific element by providing an index number through `__getitem__`
    - Make the class Truthy/Falsy with `__bool__`

- As for the decorators, I can definitely see some of the uses, especially in a testing format but to see the full potential of it's uses I would likely need a decent chunk of time working with them to see what they can truly do.
  - I created decorators to;
    - Time the function through the `time` import.
    - Slow the function down by 1 second with `sleep` import.
    - Take the output of a function and make a 1 element list from it.
    - Convert the output of a function to a string.
    - Validate the first input type by printing the type of the first arg.
