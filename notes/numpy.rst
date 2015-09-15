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

Indexing, Slicing
-----------------

The items of an array can be accessed and assigned to the same way as other Python sequences (e.g. lists)::

	>>> a = np.arange(10)
	>>> a
	array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
	>>> a[0], a[2], a[-1]
	(0, 2, 9)

Similarly, array order can be reversed::

	>>> a[::-1]
	array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

For multidimensional arrays::

	>>> a = np.diag(np.arange(3))
	>>> a
	array([[0, 0, 0],
	       [0, 1, 0],
	       [0, 0, 2]])
	>>> a[1, 1]
	1
	>>> a[2, 1] = 10
	>>> a
	array([[ 0,  0,  0],
	       [ 0,  1,  0],
	       [ 0, 10,  2]])
	>>> a[1]
	array([0, 1, 0])

Arrays, like other Python sequences can also be sliced::

	>>> a = np.arange(10)
	>>> a
	array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
	>>> a[2:9:3] # [start:end:step]
	array([2, 5, 8])

All three slice components are not required: by default, ``start`` is 0, ``end`` is the last and ``step`` is 1::

	>>> a[1:3]
	array([1, 2])
	>>> a[::2]
	array([0, 2, 4, 6, 8])
	>>> a[3:]
	array([3, 4, 5, 6, 7, 8, 9])

A more sophisticated example for multidimensional array::

	>>> a = np.arange(60).reshape((6, 10))[:, :6]
	>>> a
	array([[ 0,  1,  2,  3,  4,  5],
	       [10, 11, 12, 13, 14, 15],
	       [20, 21, 22, 23, 24, 25],
	       [30, 31, 32, 33, 34, 35],
	       [40, 41, 42, 43, 44, 45],
	       [50, 51, 52, 53, 54, 55]])
	>>> a[0, 3:5]
	array([3, 4])
	>>> a[4:, 5:]
	array([[45],
	       [55]])
	>>> a[4:, 4:]
	array([[44, 45],
	       [54, 55]])
	>>> a[:, 2]
	array([ 2, 12, 22, 32, 42, 52])
	>>> a[2::2, ::2]
	array([[20, 22, 24],
	       [40, 42, 44]])

Arrrays can be sliced using boolean logic::

	>>> np.random.seed(3)
	>>> a = np.random.random_integers(0, 20, 15)
	>>> a
	array([10,  3,  8,  0, 19, 10, 11,  9, 10,  6,  0, 20, 12,  7, 14])
	>>> (a % 3 == 0)
	array([False,  True, False,  True, False, False, False,  True, False,
	        True,  True, False,  True, False, False], dtype=bool)
	>>> a[a % 3 == 0]
	array([ 3,  0,  9,  6,  0, 12])
	>>> a[a % 3 == 0] = -1
	>>> a
	array([10, -1,  8, -1, 19, 10, 11, -1, 10, -1, -1, 20, -1,  7, 14])

Copies and Views
----------------

When operating and manipulating arrays, their data is sometimes copied into a new array and sometimes not. This is often a source of confusion for beginners. There are three cases:

No Copy at All
~~~~~~~~~~~~~~

Simple assignments make no copy of array objects or of their data.::

	>>> a = arange(12)
	>>> b = a  # no new object is created
	>>> b is a  # a and b are two names for the same ndarray object
	True
	>>> b.shape = 3, 4  # changes the shape of a
	>>> a.shape
	(3, 4)

Python passes mutable objects as references, so function calls make no copy.::

	>>> def f(x):
	...     # id is a unique identifier of an object
	...     print id(x)
	...
	>>> id(a)                           
	148293216
	>>> f(a)
	148293216

View or Shallow Copy
~~~~~~~~~~~~~~~~~~~~

Different array objects can share the same data. The view method creates a new array object that looks at the same data.::

	>>> c = a.view()
	>>> c is a
	False
	>>> c.base is a  # c is a view of the data owned by a
	True
	>>> c.flags.owndata
	False
	>>> c.shape = 2, 6  # a's shape doesn't change
	>>> a.shape
	(3, 4)
	>>> c[0, 4] = 1234  # a's data changes
	>>> a
	array([[   0,    1,    2,    3],
	       [1234,    5,    6,    7],
	       [   8,    9,   10,   11]])

Slicing an array returns a view of it::

	>>> s = a[:, 1:3]
	>>> s[:] = 10  # s[:] is a view of s. Note the difference between s=10 and s[:]=10
	>>> a
	array([[   0,   10,   10,    3],
	       [1234,   10,   10,    7],
	       [   8,   10,   10,   11]])

Deep Copy
~~~~~~~~~

The copy method makes a complete copy of the array and its data.::

	>>> d = a.copy()  # a new array object with new data is created
	>>> d is a
	False
	>>> d.base is a  # d doesn't share anything with a
	False
	>>> d[0, 0] = 9999
	>>> a
	array([[   0,   10,   10,    3],
	       [1234,   10,   10,    7],
	       [   8,   10,   10,   11]])

Array manipulations
-------------------

.. todo:: Complete **Array manipulations** section


Statistics
----------

.. todo:: Complete **Statistics** section