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

One-dimensional versions of multi-dimensional arrays can be generated with flatten::

	>>> a = np.array([[1, 2, 3], [4, 5, 6]], float)
	>>> a
	array([[ 1., 2., 3.],
	       [ 4., 5., 6.]])
	>>> a.flatten()
	array([ 1., 2., 3., 4., 5., 6.])

Two or more arrays can be concatenated together using the concatenate function with a tuple of the arrays to be joined::

		>>> a = np.array([1, 2], float)
		>>> b = np.array([3, 4, 5, 6], float)
		>>> c = np.array([7, 8, 9], float)
		>>> np.concatenate((a, b, c))
		array([1., 2., 3., 4., 5., 6., 7., 8., 9.])

If an array has more than one dimension, it is possible to specify the axis along which multiple arrays are concatenated. By default (without specifying the axis), NumPy concatenates along the first dimension::

	>>> a = np.array([[1, 2], [3, 4]], float)
	>>> b = np.array([[5, 6], [7, 8]], float)
	>>> np.concatenate((a,b))
	array([[ 1., 2.],
	       [ 3., 4.],
	       [ 5., 6.],
	       [ 7., 8.]])
	>>> np.concatenate((a, b), axis=0)
	array([[ 1., 2.],
	       [ 3., 4.],
	       [ 5., 6.],
	       [ 7., 8.]])
	>>> np.concatenate((a, b), axis=1)
	array([[ 1., 2., 5., 6.],
	       [ 3., 4., 7., 8.]])

Finally, the dimensionality of an array can be increased using the newaxis constant in bracket notation::

	>>> a = np.array([1, 2, 3], float)
	>>> a
	array([1., 2., 3.])
	>>> a[:,np.newaxis]
	array([[ 1.],
	       [ 2.],
	       [ 3.]])
	>>> a[:, np.newaxis].shape
	(3, 1)
	>>> b[np.newaxis, :]
	array([[ 1., 2., 3.]])
	>>> b[np.newaxis, :].shape
	(1, 3)

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

Python passes mutable objects as references, so function calls make no copy. ::

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

Different array objects can share the same data. The view method creates a new array object that looks at the same data. ::

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

Basic operations
~~~~~~~~~~~~~~~~

With scalars::

	>>> a = np.array([1, 2, 3, 4])
	>>> a + 1
	array([2, 3, 4, 5])
	>>> 2**a
	array([ 2,  4,  8, 16])

All arithmetic operates elementwise::

	>>> b = np.ones(4) + 1
	>>> a - b
	array([-1.,  0.,  1.,  2.])
	>>> a * b
	array([ 2.,  4.,  6.,  8.])
	>>> c = np.arange(5)
	>>> 2**(c + 1) - c
	array([ 2,  3,  6, 13, 28])

Array multiplication is not matrix multiplication::

	>>> c = np.ones((3, 3))
	>>> c * c
	array([[ 1.,  1.,  1.],
	       [ 1.,  1.,  1.],
	       [ 1.,  1.,  1.]])
	>>> c.dot(c)
	array([[ 3.,  3.,  3.],
	       [ 3.,  3.,  3.],
	       [ 3.,  3.,  3.]])

Other operations
~~~~~~~~~~~~~~~~

Comparisons::

	>>> a = np.array([1, 2, 3, 4])
	>>> b = np.array([4, 2, 2, 4])
	>>> a == b
	array([False,  True, False,  True], dtype=bool)
	>>> a > b
	array([False, False,  True, False], dtype=bool)

Array-wise comparisons::

	>>> a = np.array([1, 2, 3, 4])
	>>> b = np.array([4, 2, 2, 4])
	>>> c = np.array([1, 2, 3, 4])
	>>> np.array_equal(a, b)
	False
	>>> np.array_equal(a, c)
	True
	>>> np.allclose(a, a + a*1e-5)
	True
	>>> np.allclose(a, a + a*1e-4)
	False

Logical operations::

	>>> a = np.array([1, 1, 0, 0], dtype=bool)
	>>> b = np.array([1, 0, 1, 0], dtype=bool)
	>>> np.logical_or(a, b)
	array([ True,  True,  True, False], dtype=bool)
	>>> np.logical_and(a, b)
	array([ True, False, False, False], dtype=bool)

The ``where`` function forms a new array from two arrays of equivalent size using a Boolean filter to choose between elements of the two. Its basic syntax is ``where(boolarray, truearray, falsearray)``::

	>>> a = np.array([1, 3, 0], float)
	>>> np.where(a != 0, 1 / a, a)
	array([ 1. , 0.33333333, 0. ])

Broadcasting can also be used with the where function::

	>>> np.where(a > 0, 3, 2)
	array([3, 3, 2])


Broadcasting
~~~~~~~~~~~~

Arrays that do not match in the number of dimensions will be broadcasted by Python to perform mathematical operations. This often means that the smaller array will be repeated as necessary to perform the operation indicated. Consider the following::

	>>> a = np.array([[1, 2], [3, 4], [5, 6]], float)
	>>> b = np.array([-1, 3], float)
	>>> a
	array([[ 1., 2.],
	       [ 3., 4.],
	       [ 5., 6.]])
	>>> b
	array([-1., 3.])
	>>> a + b
	array([[ 0., 5.],
	       [ 2., 7.],
	       [ 4., 9.]])

Here, the one-dimensional array ``b`` was broadcasted to a two-dimensional array that matched the size of ``a``. In essence, ``b`` was repeated for each item in ``a``, as if it were given by::

	array([[-1., 3.],
	       [-1., 3.],
	       [-1., 3.]])

Python automatically broadcasts arrays in this manner. Sometimes, however, how we should broadcast is ambiguous. In these cases, we can use the newaxis constant to specify how we want to broadcast::

	>>> a = np.zeros((2,2), float)
	>>> b = np.array([-1., 3.], float)
	>>> a
	array([[ 0., 0.],
	       [ 0., 0.]])
	>>> b
	array([-1., 3.])
	>>> a + b
	array([[-1., 3.],
	       [-1., 3.]])
	>>> a + b[np.newaxis, :]
	array([[-1., 3.],
	       [-1., 3.]])
	>>> a + b[:, np.newaxis]
	array([[-1., -1.],
	       [ 3., 3.]])


Reductions
----------

We can easily compute sums and products::

	>>> a = np.array([2, 4, 3])
	>>> a.sum(), a.prod()
	(9, 24)
	>>> np.sum(a), np.prod(a)
	(9, 24)

Some basic statistics::

	>>> a = np.random.randn(100)
	>>> a.mean()
	-0.083139603089394359
	>>> np.median(a)
	-0.14321054235009417
	>>> a.std()
	1.0565446101521685
	>>> a.var()
	1.1162865132415978
	>>> a.min(), a.max()
	(-2.9157377517927121, 2.1581493420569187)
	>>> np.percentile(a, [5, 50, 95])
	array([-1.48965296, -0.08633928,  1.36836205])

For multidimensional arrays, each of the functions thus far described can take an optional argument ``axis`` that will perform an operation along only the specified axis, placing the results in a return array::

	>>> a = np.array([[0, 2], [3, -1], [3, 5]], float)
	>>> a.mean(axis=0)
	array([ 2., 2.])
	>>> a.mean(axis=1)
	array([ 1., 1., 4.])
	>>> a.min(axis=1)
	array([ 0., -1., 3.])
	>>> a.max(axis=0)
	array([ 3., 5.])

It is possible to find the index of the smallest and largest element::

	>>> a = np.array([2, 1, 9], float)
	>>> a.argmin()
	1
	>>> a.argmax()
	2

Like lists, arrays can be sorted::

	>>> a = np.array([6, 2, 5, -1, 0], float)
	>>> sorted(a)
	[-1.0, 0.0, 2.0, 5.0, 6.0]
	>>> a.sort()
	>>> a
	array([-1., 0., 2., 5., 6.])

Values in an array can be "clipped" to be within a prespecified range. This is the same as applying ``min(max(x, minval), maxval)`` to each element ``x`` in an array. ::

	>>> a = np.array([6, 2, 5, -1, 0], float)
	>>> a.clip(0, 5)
	array([ 5., 2., 5., 0., 0.])

Unique elements can be extracted from an array::

	>>> a = np.array([1, 1, 4, 5, 5, 5, 7], float)
	>>> np.unique(a)
	array([ 1., 4., 5., 7.])