=======================
Pandas. Data processing
=======================

Pandas is an essential data analysis library within Python ecosystem. For more details read `Pandas Documentation <http://pandas.pydata.org/>`_.

Data sructures
--------------

Pandas is operates with three basic datastructures: `Series`, `DataFrame`, and `Panel`. There are extensions to this list, but at the tie of writing (v0.16.2) they are all experimental.

We start by importing NumPy and Pandas using their conventional short names:

.. ipython::

	In [1]: import numpy as np

	In [2]: import pandas as pd

	In [3]: randn = np.random.rand # To shorten notation in the code that follows


Series
~~~~~~

Series is a one-dimensional labeled array capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.). The axis labels are collectively referred to as the index. The basic method to create a Series is to call::

	>>> s = Series(data, index=index)

The first mandatory argument can be

	- array-like
	- dictionary
	- scalar

Array-like
^^^^^^^^^^

If ``data`` is an array-like, ``index`` must be the same length as ``data``. If no index is passed, one will be created having values ``[0, ..., len(data) - 1]``.

.. ipython::

	In [8]: s = pd.Series(randn(5), index=['a', 'b', 'c', 'd', 'e'])

	In [9]: s
	Out[9]: 
	a   -1.237684
	b    0.619159
	c   -0.198496
	d    1.398684
	e   -0.641900
	dtype: float6

	In [10]: s.index
	Out[10]: Index(['a', 'b', 'c', 'd', 'e'], dtype='object')

	In [11]: pd.Series(randn(5))
	Out[11]: 
	0    0.338276
	1    0.017430
	2   -0.129383
	3    0.675684
	4    0.944181
	dtype: float6

Dictionary
^^^^^^^^^^

Dinctionaries already have a natural candidate for the index, so passing the ``index`` separately seems redundant, although possible.

.. ipython::

	In [12]: d = {'a' : 0., 'b' : 1., 'c' : 2.}

	In [13]: pd.Series(d)
	Out[13]: 
	a    0
	b    1
	c    2
	dtype: float64

	In [14]: pd.Series(d, index=['b', 'c', 'd', 'a'])
	Out[14]: 
	b     1
	c     2
	d   NaN
	a     0
	dtype: float6

Scalar
^^^^^^

If ``data`` is a scalar value, an index must be provided. The value will be repeated to match the length of index.

.. ipython::

	In [15]: pd.Series(5., index=['a', 'b', 'c', 'd', 'e'])
	Out[15]: 
	a    5
	b    5
	c    5
	d    5
	e    5
	dtype: float6

Series is similar to array
^^^^^^^^^^^^^^^^^^^^^^^^^^

Slicing and other operations on `Series` produce very similar results to those on ``array`` but with a twist. Index is also sliced and always remain a part of a data container.

.. ipython::

	In [16]: s[0]
	Out[16]: -1.2376835654566896

	In [17]: s[:3]
	Out[17]: 
	a   -1.237684
	b    0.619159
	c   -0.198496
	dtype: float64

	In [18]: s[s > s.median()]
	Out[18]: 
	b    0.619159
	d    1.398684
	dtype: float64

	In [19]: s[[4, 3, 1]]
	Out[19]: 
	e   -0.641900
	d    1.398684
	b    0.619159
	dtype: float64

Similarly to NumPy arrays, Series can be used to speed up loops by using vectorization.

.. ipython::

	In [26]: s + s
	Out[26]: 
	a    -2.475367
	b     1.238319
	c    -0.396993
	d     2.797368
	e    24.000000
	dtype: float64

	In [27]: s * 2
	Out[27]: 
	a    -2.475367
	b     1.238319
	c    -0.396993
	d     2.797368
	e    24.000000
	dtype: float6

	In [20]: np.exp(s)
	Out[20]: 
	a    0.290055
	b    1.857366
	c    0.819963
	d    4.049866
	e    0.526291
	dtype: float6

A key difference between Series and array is that operations between Series automatically align the data based on label. Thus, you can write computations without giving consideration to whether the Series involved have the same labels.

.. ipython::

	In [28]: s[1:] + s[:-1]
	Out[28]: 
	a         NaN
	b    1.238319
	c   -0.396993
	d    2.797368
	e         NaN
	dtype: float6

The result of an operation between unaligned Series will have the union of the indexes involved. If a label is not found in one Series or the other, the result will be marked as missing NaN. Being able to write code without doing any explicit data alignment grants immense freedom and flexibility in interactive data analysis and research. The integrated data alignment features of the pandas data structures set pandas apart from the majority of related tools for working with labeled data.

Series is similar to dictionary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A few examples t illustrate the heading.

.. ipython::

	In [21]: s['a']
	Out[21]: -1.2376835654566896

	In [22]: s['e'] = 12.

	In [23]: s
	Out[23]: 
	a    -1.237684
	b     0.619159
	c    -0.198496
	d     1.398684
	e    12.000000
	dtype: float64

	In [24]: 'e' in s
	Out[24]: True

	In [25]: 'f' in s
	Out[25]: Fals

Name attribute
^^^^^^^^^^^^^^

Series can also have a name attribute which will become very useful when summarizing data with tables and plots.

.. ipython::

	In [29]: s = pd.Series(np.random.randn(5), name='random series')

	In [30]: s
	Out[30]: 
	0    0.930582
	1   -1.769931
	2   -0.408553
	3    2.649618
	4    1.060224
	Name: random series, dtype: float64

	In [31]: s.name
	Out[31]: 'random series

DataFrame
~~~~~~~~~


Basic functions
---------------


Indexing and selecting Data
---------------------------

.. todo:: Write **Pandas** section
