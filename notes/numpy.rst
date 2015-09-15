========================================
NumPy. Manipulations with numerical data
========================================

.. contents::

Array creation
--------------

NumPy's main object is the homogeneous multidimensional array. It is a table of elements (usually numbers), all of the same type, indexed by a tuple of positive integers. Arrays make operations with large amounts of numeric data very fast and are generally much more efficient than lists.

It is a convention to import NumPy as follows::

	>>> import numpy as np

The simplest way to create an elementary array is from a list::

	>>> a = np.array([0, 1, 2, 3])
	>>> a
	array([0, 1, 2, 3])
	>>> type(a)
	<type 'numpy.ndarray'>
	>>> a.dtype
	dtype('int64')

The type of the array can also be explicitly specified at creation time::

	>>> a = np.array([0, 1, 2, 3], float)
	>>> a.dtype
	dtype('float64')

Array transforms sequences of sequences into two-dimensional arrays, sequences of sequences of sequences into three-dimensional arrays, and so on. ::

	>>> b = np.array([[1.5,2,3], [4,5,6]])
	>>> b
	array([[ 1.5,  2. ,  3. ],
	       [ 4. ,  5. ,  6. ]])
	>>> c = np.array([[[1], [2]], [[3], [4]]])
	>>> c
	array([[[1],
	        [2]],

	       [[3],
	        [4]]])
	>>> print(a.ndim, b.ndim, c.ndim)
	1 2 3
	>>> print(a.shape, b.shape, c.shape)
	(4,) (2, 3) (2, 2, 1)

There are a lot of functions to create some standard arrays, such as filled with ones, zeros, etc. ::

	>>> a = np.arange(10)
	>>> np.arange(10)
	array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
	>>> np.arange(1, 9, 2) # start, end (exclusive), step
	array([1, 3, 5, 7])
	>>> np.linspace(0, 1, 6) # start, end, num-points
	array([ 0. ,  0.2,  0.4,  0.6,  0.8,  1. ])
	>>> np.linspace(0, 1, 5, endpoint=False)
	array([ 0. ,  0.2,  0.4,  0.6,  0.8])
	>>> np.ones((3, 3))
	array([[ 1.,  1.,  1.],
	       [ 1.,  1.,  1.],
	       [ 1.,  1.,  1.]])
	>>> np.zeros((2, 2))
	array([[ 0.,  0.],
	       [ 0.,  0.]])
	>>> np.eye(3)
	array([[ 1.,  0.,  0.],
	       [ 0.,  1.,  0.],
	       [ 0.,  0.,  1.]])
	>>> np.diag(np.array([1, 2, 3, 4]))
	array([[1, 0, 0, 0],
	       [0, 2, 0, 0],
	       [0, 0, 3, 0],
	       [0, 0, 0, 4]])
	>>> np.ones_like(np.zeros((2, 2)))
	array([[ 1.,  1.],
	       [ 1.,  1.]])
	>>> np.zeros_like(np.ones((2, 2)))
	array([[ 0.,  0.],
	       [ 0.,  0.]])
	>>> np.random.rand(4) # U[0, 1]
	array([ 0.37534773,  0.19079141,  0.80011337,  0.54003586])
	>>> np.random.randn(4) # N(0, 1)
	array([-0.2981319 , -0.06627354,  0.31080455,  0.28470444])

Array manipulations
-------------------

.. todo:: Complete **Array manipulations** section

Indexing, Slicing and Iterating
-------------------------------

.. todo:: Complete **Indexing, Slicing and Iterating** section

Statistics
----------

.. todo:: Complete **Statistics** section