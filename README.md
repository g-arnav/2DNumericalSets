# 2DNumericalSets
Provides python classes to build a tree containing all the 2D numerical semigroups up to a given genus.

## Usage
###To build a tree of max genus n and check the size of that genus,
In a python 3 interpreter:

	>>> from path/to/Tree import tree
	>>> t = Tree(n)
	>>> print(t.size())
	
###To view a list of the degrees of vertices at genus g:

	>>> print(t.genus(g))

###To build a tree with a different ordering function than the default:
First, in Ordering.py, write a new ordering function that takes in 2 input points and returns True if the first point is less than the second and False otherwise, let's call this function new_ordering_function
Then:
	
	>>> t = Tree(n, new_ordering_function)
