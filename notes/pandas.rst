=======================
Pandas. Data processing
=======================

Pandas is an essential data analysis library within Python ecosystem. For more details read `Pandas Documentation <http://pandas.pydata.org/>`_.

.. contents::

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

DataFrame is a 2-dimensional labeled data structure with columns of potentially different types. Like Series, DataFrame accepts many different kinds of input:

	- Dict of 1D ndarrays, lists, dicts, or Series
	- 2-D numpy.ndarray
	- A Series
	- Another DataFrame

Along with the data, you can optionally pass **index** (row labels) and **columns** (column labels) arguments. If you pass an index and / or columns, you are guaranteeing the index and / or columns of the resulting DataFrame. Thus, a dict of Series plus a specific index will discard all data not matching up to the passed index.

If axis labels are not passed, they will be constructed from the input data based on common sense rules.

From dict of Series or dicts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The result index will be the union of the indexes of the various Series. If there are any nested dicts, these will be first converted to Series. If no columns are passed, the columns will be the sorted list of dict keys.

.. ipython::

	In [38]: d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
	   ....:      'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}

	In [40]: df = pd.DataFrame(d)

	In [41]: df
	Out[41]: 
	   one  two
	a    1    1
	b    2    2
	c    3    3
	d  NaN    4

	In [42]: pd.DataFrame(d, index=['d', 'b', 'a'])
	Out[42]: 
	   one  two
	d  NaN    4
	b    2    2
	a    1    1

	In [43]: pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three'])
	Out[43]: 
	   two three
	d    4   NaN
	b    2   NaN
	a    1   NaN

The row and column labels can be accessed respectively by accessing the index and columns attributes:

.. ipython::

	In [44]: df.index
	Out[44]: Index(['a', 'b', 'c', 'd'], dtype='object')

	In [45]: df.columns
	Out[45]: Index(['one', 'two'], dtype='object'

From dict of array-likes
^^^^^^^^^^^^^^^^^^^^^^^^

The ndarrays must all be the same length. If an index is passed, it must clearly also be the same length as the arrays. If no index is passed, the result will be ``range(n)``, where ``n`` is the array length.

.. ipython::

	In [46]: d = {'one' : [1., 2., 3., 4.], 'two' : [4., 3., 2., 1.]}

	In [47]: pd.DataFrame(d)
	Out[47]: 
	   one  two
	0    1    4
	1    2    3
	2    3    2
	3    4    1

	In [48]: pd.DataFrame(d, index=['a', 'b', 'c', 'd'])
	Out[48]: 
	   one  two
	a    1    4
	b    2    3
	c    3    2
	d    4    1

From a list of dicts
^^^^^^^^^^^^^^^^^^^^

.. ipython::

	In [49]: data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]

	In [50]: pd.DataFrame(data2)
	Out[50]: 
	   a   b   c
	0  1   2 NaN
	1  5  10  20

	In [51]: pd.DataFrame(data2, index=['first', 'second'])
	Out[51]: 
	        a   b   c
	first   1   2 NaN
	second  5  10  20

	In [52]: pd.DataFrame(data2, columns=['a', 'b'])
	Out[52]: 
	   a   b
	0  1   2
	1  5  10

From a dict of tuples
^^^^^^^^^^^^^^^^^^^^^

.. ipython::

	In [53]: pd.DataFrame({('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},
	   ....:               ('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},
	   ....:               ('a', 'c'): {('A', 'B'): 5, ('A', 'C'): 6},
	   ....:               ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
	   ....:               ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}})
	Out[53]: 
	      a           b    
	      a   b   c   a   b
	A B   4   1   5   8  10
	  C   3   2   6   7 NaN
	  D NaN NaN NaN NaN   9

From a Series
^^^^^^^^^^^^^

The result will be a DataFrame with the same index as the input Series, and with one column whose name is the original name of the Series (only if no other column name provided).


Basic functionality
-------------------

.. ipython::

Here are the data sets that will be used below.

	In [58]: index = pd.date_range('1/1/2000', periods=8)

	In [59]: s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])

	In [60]: df = pd.DataFrame(np.random.randn(8, 3), index=index,
	   ....:                   columns=['A', 'B', 'C'])


Head and Tail
~~~~~~~~~~~~~

To view a small sample of a Series or DataFrame object, use the ``head()`` and ``tail()`` methods. The default number of elements to display is five, but you may pass a custom number.

.. ipython::

	In [61]: long_series = pd.Series(np.random.randn(1000))

	In [62]: long_series.head()
	Out[62]: 
	0   -0.755628
	1    0.256718
	2   -0.400233
	3   -0.901375
	4    1.419292
	dtype: float64

	In [63]: long_series.tail(3)
	Out[63]: 
	997    1.568994
	998   -0.021591
	999    0.401315
	dtype: float64

Attributes and the raw values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pandas objects have a number of attributes enabling you to access the metadata

	- ``shape``: gives the axis dimensions of the object, consistent with ndarray
	- Axis labels

		- Series: ``index`` (only axis)
		- DataFrame: ``index`` (rows) and ``columns``

Note, these attributes can be safely assigned to!

.. ipython::

	In [64]: df[:2]
	Out[64]: 
	                   A         B         C
	2000-01-01 -0.720869 -1.625032  1.217513
	2000-01-02 -0.159141 -0.130845 -0.349405

	In [65]: df.columns = [x.lower() for x in df.columns]

	In [66]: df
	Out[66]: 
	                   a         b         c
	2000-01-01 -0.720869 -1.625032  1.217513
	2000-01-02 -0.159141 -0.130845 -0.349405
	2000-01-03  0.178766  0.955791 -0.026645
	2000-01-04  0.251469 -1.224634 -2.068661
	2000-01-05 -0.367191  0.339624  0.740954
	2000-01-06 -1.094821  1.220938  1.040498
	2000-01-07 -1.253747 -0.215979  0.633734
	2000-01-08  0.531562  0.599597 -0.278515

To get the actual data inside a data structure, one need only access the values property:

.. ipython::

	In [67]: s.values
	Out[67]: array([ 1.60809988,  0.89314247, -0.41259431, -0.51164044,  0.63815301])

	In [68]: df.values
	Out[68]: 
	array([[-0.72086916, -1.62503155,  1.21751252],
	       [-0.1591411 , -0.13084532, -0.34940464],
	       [ 0.17876557,  0.95579106, -0.02664479],
	       [ 0.25146863, -1.22463399, -2.06866112],
	       [-0.36719088,  0.33962437,  0.74095404],
	       [-1.09482136,  1.22093767,  1.04049764],
	       [-1.25374681, -0.21597943,  0.63373357],
	       [ 0.53156235,  0.599597  , -0.2785151 ]])

Descriptive statistics
~~~~~~~~~~~~~~~~~~~~~~

A large number of methods for computing descriptive statistics and other related operations on Series and DataFrame. Most of these are aggregations (hence producing a lower-dimensional result) like ``sum()``, ``mean()``, and ``quantile()``, but some of them, like ``cumsum()`` and ``cumprod()``, produce an object of the same size. Generally speaking, these methods take an axis argument, just like ``ndarray.{sum, std, ...}``, but the axis can be specified by name or integer:

	- Series: no axis argument needed
	- DataFrame: "index" (axis=0, default), "columns" (axis=1)

.. ipython::

	In [70]: df = pd.DataFrame({'one' : pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
	   ....:                    'two' : pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
	   ....:                    'three' : pd.Series(np.random.randn(3), index=['b', 'c', 'd'])})

	In [71]: df.mean(0)
	Out[71]: 
	one      0.902130
	three   -0.581931
	two     -0.077073
	dtype: float64

	In [72]: df.mean(1)
	Out[72]: 
	a    0.564020
	b    0.703984
	c   -0.303257
	d   -0.838956
	dtype: float64

All such methods have a ``skipna`` option signaling whether to exclude missing data (``True`` by default):

.. ipython::

	In [73]: df.sum(0, skipna=False)
	Out[73]: 
	one          NaN
	three        NaN
	two     -0.30829
	dtype: float64

	In [74]: df.sum(axis=1, skipna=True)
	Out[74]: 
	a    1.128039
	b    2.111951
	c   -0.909770
	d   -1.677912
	dtype: float64

Combined with the broadcasting / arithmetic behavior, one can describe various statistical procedures, like standardization (rendering data zero mean and standard deviation 1), very concisely:

.. ipython::

	In [75]: ts_stand = (df - df.mean()) / df.std()

	In [76]: ts_stand.std()
	Out[76]: 
	one      1
	three    1
	two      1
	dtype: float6

	In [81]: xs_stand = df.sub(df.mean(1), axis=0).div(df.std(1), axis=0)

	In [82]: xs_stand.std(1)
	Out[82]: 
	a    1
	b    1
	c    1
	d    1
	dtype: float64

Series also has a method ``nunique()`` which will return the number of unique non-null values:

.. ipython::

	In [83]: series = pd.Series(np.random.randn(500))

	In [84]: series[20:500] = np.nan

	In [85]: series[10:20] = 5

	In [86]: series.nunique()
	Out[86]: 11

Summarizing data: ``describe``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There is a convenient ``describe()`` function which computes a variety of summary statistics about a Series or the columns of a DataFrame:

.. ipython::

	In [87]: series = pd.Series(np.random.randn(1000))

	In [88]: series[::2] = np.nan

	In [89]: series.describe()
	Out[89]: 
	count    500.000000
	mean       0.075883
	std        0.995142
	min       -3.239942
	25%       -0.596217
	50%        0.068842
	75%        0.745957
	max        2.891859
	dtype: float64

	In [90]: frame = pd.DataFrame(np.random.randn(1000, 5),
	   ....:                      columns=['a', 'b', 'c', 'd', 'e'])

	In [91]: frame.ix[::2] = np.nan

	In [92]: frame.describe()
	Out[92]: 
	                a           b           c           d           e
	count  500.000000  500.000000  500.000000  500.000000  500.000000
	mean     0.013695   -0.016458   -0.001245    0.030559    0.025056
	std      0.976916    0.977952    0.986296    1.012748    0.938989
	min     -3.546203   -3.006170   -2.632051   -2.667590   -3.176698
	25%     -0.648926   -0.673880   -0.651576   -0.599431   -0.629356
	50%      0.019921   -0.066348    0.064648    0.019820    0.030337
	75%      0.660501    0.608011    0.623423    0.731639    0.668216
	max      3.071626    2.897954    2.955093    3.423565    2.466419

You can select specific percentiles to include in the output:

.. ipython::

	In [93]: series.describe(percentiles=[.05, .25, .75, .95])
	Out[93]: 
	count    500.000000
	mean       0.075883
	std        0.995142
	min       -3.239942
	5%        -1.502234
	25%       -0.596217
	50%        0.068842
	75%        0.745957
	95%        1.743120
	max        2.891859
	dtype: float64

For a non-numerical Series object, ``describe()`` will give a simple summary of the number of unique values and most frequently occurring values:

.. ipython::

	In [94]: s = pd.Series(['a', 'a', 'b', 'b', 'a', 'a', np.nan, 'c', 'd', 'a'])

	In [95]: s.describe()
	Out[95]: 
	count     9
	unique    4
	top       a
	freq      5
	dtype: object

Note that on a mixed-type DataFrame object, ``describe()`` will restrict the summary to include only numerical columns or, if none are, only categorical columns:

.. ipython::

	In [96]: frame = pd.DataFrame({'a': ['Yes', 'Yes', 'No', 'No'], 'b': range(4)})

	In [97]: frame.describe()
	Out[97]: 
	              b
	count  4.000000
	mean   1.500000
	std    1.290994
	min    0.000000
	25%    0.750000
	50%    1.500000
	75%    2.250000
	max    3.000000


This behaviour can be controlled by providing a list of types as ``include/exclude`` arguments. The special value all can also be used:

.. ipython::

	In [98]: frame.describe(include=['object'])
	Out[98]: 
	         a
	count    4
	unique   2
	top     No
	freq     2

	In [99]: frame.describe(include=['number'])
	Out[99]: 
	              b
	count  4.000000
	mean   1.500000
	std    1.290994
	min    0.000000
	25%    0.750000
	50%    1.500000
	75%    2.250000
	max    3.000000

	In [100]: frame.describe(include='all')
	Out[100]: 
	          a         b
	count     4  4.000000
	unique    2       NaN
	top      No       NaN
	freq      2       NaN
	mean    NaN  1.500000
	std     NaN  1.290994
	min     NaN  0.000000
	25%     NaN  0.750000
	50%     NaN  1.500000
	75%     NaN  2.250000
	max     NaN  3.000000

Index of Min/Max Values
~~~~~~~~~~~~~~~~~~~~~~~

The ``idxmin()`` and ``idxmax()`` functions on Series and DataFrame compute the index labels with the minimum and maximum corresponding values:

.. ipython::

	In [101]: s1 = pd.Series(np.random.randn(5))

	In [102]: s1
	Out[102]: 
	0   -0.285582
	1    0.561600
	2   -0.698818
	3    1.895033
	4    0.696276
	dtype: float64

	In [103]: s1.idxmin(), s1.idxmax()
	Out[103]: (2, 3)

	In [104]: df1 = pd.DataFrame(np.random.randn(5,3), columns=['A','B','C'])

	In [105]: df1
	Out[105]: 
	          A         B         C
	0 -0.260848  0.829572 -1.228782
	1 -0.133263  0.057332 -1.198091
	2  0.373924 -1.851239 -1.063831
	3  0.203525 -0.203526 -0.050572
	4  1.039559  1.380611  0.976727

	In [106]: df1.idxmin(axis=0)
	Out[106]: 
	A    0
	B    2
	C    0
	dtype: int64

	In [107]: df1.idxmin(axis=1)
	Out[107]: 
	0    C
	1    C
	2    B
	3    B
	4    C
	dtype: object

When there are multiple rows (or columns) matching the minimum or maximum value, ``idxmin()`` and ``idxmax()`` return the first matching index:

.. ipython::

	In [108]: df3 = pd.DataFrame([2, 1, 1, 3, np.nan], columns=['A'], index=list('edcba'))

	In [109]: df3
	Out[109]: 
	    A
	e   2
	d   1
	c   1
	b   3
	a NaN

	In [110]: df3['A'].idxmin()
	Out[110]: 'd'

Value counts (histogramming) / Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``value_counts()`` Series method and top-level function computes a histogram of a 1D array of values.

.. ipython::

	In [111]: data = np.random.randint(0, 7, size=50)

	In [112]: data
	Out[112]: 
	array([1, 5, 5, 2, 4, 0, 4, 1, 2, 5, 0, 4, 2, 5, 3, 5, 6, 3, 0, 4, 4, 4, 6,
	       0, 1, 6, 5, 4, 0, 1, 5, 0, 6, 1, 4, 2, 5, 4, 6, 3, 1, 1, 4, 4, 4, 0,
	       1, 0, 4, 6])

	In [113]: s = pd.Series(data)

	In [114]: s.value_counts()
	Out[114]: 
	4    13
	5     8
	1     8
	0     8
	6     6
	2     4
	3     3
	dtype: int64

Similarly, you can get the most frequently occurring value(s) (the mode) of the values in a Series or DataFrame:

.. ipython::

	In [115]: s5 = pd.Series([1, 1, 3, 3, 3, 5, 5, 7, 7, 7])

	In [116]: s5.mode()
	Out[116]: 
	0    3
	1    7
	dtype: int64

	In [117]: df5 = pd.DataFrame({'A': np.random.randint(0, 7, size=50), 'B': np.random.randint(-10, 15, size=50)})

	In [118]: df5.mode()
	Out[118]: 
	    A   B
	0   0 -10
	1 NaN   2
	2 NaN  11

Discretization and quantiling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Continuous values can be discretized using the ``cut()`` (bins based on values) and ``qcut()`` (bins based on sample quantiles) functions:

.. ipython::

	In [119]: arr = np.random.randn(20)

	In [120]: factor = pd.cut(arr, 4)

	In [121]: factor
	Out[121]: 
	[(-0.543, 0.42], (0.42, 1.383], (-0.543, 0.42], (-0.543, 0.42], (-0.543, 0.42], ..., (-0.543, 0.42], (-0.543, 0.42], (-0.543, 0.42], (0.42, 1.383], (0.42, 1.383]]
	Length: 20
	Categories (4, object): [(-2.474, -1.507] < (-1.507, -0.543] < (-0.543, 0.42] < (0.42, 1.383]]

	In [122]: factor = pd.cut(arr, [-5, -1, 0, 1, 5])

	In [123]: factor
	Out[123]: 
	[(-1, 0], (0, 1], (-1, 0], (-1, 0], (-1, 0], ..., (0, 1], (0, 1], (0, 1], (1, 5], (1, 5]]
	Length: 20
	Categories (4, object): [(-5, -1] < (-1, 0] < (0, 1] < (1, 5]]

``qcut()`` computes sample quantiles. For example, we could slice up some normally distributed data into equal-size quartiles like so:

.. ipython::

	In [125]: factor = pd.qcut(arr, [0, .25, .5, .75, 1])

	In [126]: factor
	Out[126]: 
	[[-1.672, -0.553], [-1.672, -0.553], (-0.0296, 0.509], (-0.553, -0.0296], [-1.672, -0.553], ..., (-0.553, -0.0296], [-1.672, -0.553], (0.509, 1.591], (-0.553, -0.0296], (0.509, 1.591]]
	Length: 30
	Categories (4, object): [[-1.672, -0.553] < (-0.553, -0.0296] < (-0.0296, 0.509] < (0.509, 1.591]]

	In [127]: pd.value_counts(factor)
	Out[127]: 
	(0.509, 1.591]       8
	[-1.672, -0.553]     8
	(-0.0296, 0.509]     7
	(-0.553, -0.0296]    7
	dtype: int64

We can also pass infinite values to define the bins:

.. ipython::

	In [128]: arr = np.random.randn(20)

	In [129]: factor = pd.cut(arr, [-np.inf, 0, np.inf])

	In [130]: factor
	Out[130]: 
	[(0, inf], (-inf, 0], (-inf, 0], (0, inf], (-inf, 0], ..., (-inf, 0], (-inf, 0], (-inf, 0], (0, inf], (-inf, 0]]
	Length: 20
	Categories (2, object): [(-inf, 0] < (0, inf]]



Indexing and selecting Data
---------------------------

.. todo:: Write **Pandas** section
