=======================
Pandas. Data processing
=======================

Pandas is an essential data analysis library within Python ecosystem. For more details read `Pandas Documentation <http://pandas.pydata.org/>`_.

.. contents::

Data structures
---------------

Pandas operates with three basic datastructures: `Series`, `DataFrame`, and `Panel`. There are extensions to this list, but for the purposes of this material even the first two are more than enough.

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

Dictionaries already have a natural candidate for the index, so passing the ``index`` separately seems redundant, although possible.

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

A few examples to illustrate the heading.

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

Here are the data sets that will be used below.

.. ipython::

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

	In [117]: df5 = pd.DataFrame({'A': np.random.randint(0, 7, size=50),
	   .....:                     'B': np.random.randint(-10, 15, size=50)})

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


Function application
--------------------

Row or Column-wise Function Application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Arbitrary functions can be applied along the axes of a DataFrame using the ``apply()`` method, which, like the descriptive statistics methods, take an optional axis argument:

.. ipython::

	In [5]: df = pd.DataFrame({'one' : pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
	   ...: 'two' : pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
	   ...: 'three' : pd.Series(np.random.randn(3), index=['b', 'c', 'd'])})

	In [6]: df
	Out[6]: 
	        one     three       two
	a  1.589450       NaN  1.117724
	b -0.252391  0.511787 -0.580168
	c -0.098049  2.785835  1.347622
	d       NaN -0.752325 -0.198108

	In [7]: df.apply(np.mean)
	Out[7]: 
	one      0.413003
	three    0.848432
	two      0.421768
	dtype: float64

	In [8]: df.apply(np.mean, axis=1)
	Out[8]: 
	a    1.353587
	b   -0.106924
	c    1.345136
	d   -0.475217
	dtype: float64

	In [9]: df.apply(lambda x: x.max() - x.min())
	Out[9]: 
	one      1.841841
	three    3.538161
	two      1.927790
	dtype: float64

	In [10]: df.apply(np.cumsum)
	Out[10]: 
	        one     three       two
	a  1.589450       NaN  1.117724
	b  1.337058  0.511787  0.537556
	c  1.239009  3.297623  1.885178
	d       NaN  2.545297  1.687070

Depending on the return type of the function passed to ``apply()``, the result will either be of lower dimension or the same dimension.

``apply()`` combined with some cleverness can be used to answer many questions about a data set. For example, suppose we wanted to extract the date where the maximum value for each column occurred:

.. ipython::

	In [11]: tsdf = pd.DataFrame(np.random.randn(1000, 3), columns=['A', 'B', 'C'],
	   ....: index=pd.date_range('1/1/2000', periods=1000))

	In [12]: tsdf.apply(lambda x: x.idxmax())
	Out[12]: 
	A   2000-03-10
	B   2002-06-26
	C   2001-12-03
	dtype: datetime64[ns]

You may also pass additional arguments and keyword arguments to the ``apply()`` method. For instance, consider the following function you would like to apply:

.. ipython::

	In [13]: def subtract_and_divide(x, sub, divide=1):
	   ....:     return (x - sub) / divide
	   ....: 

	In [14]: df.apply(subtract_and_divide, args=(5,), divide=3)
	Out[14]: 
	        one     three       two
	a -1.136850       NaN -1.294092
	b -1.750797 -1.496071 -1.860056
	c -1.699350 -0.738055 -1.217459
	d       NaN -1.917442 -1.732703

Another useful feature is the ability to pass Series methods to carry out some Series operation on each column or row:

.. ipython::

	In [19]: tsdf = pd.DataFrame(np.random.randn(10, 3), columns=['A', 'B', 'C'],
	   ....: index=pd.date_range('1/1/2000', periods=10))

	In [21]: tsdf.ix[4:8] = np.nan

	In [23]: tsdf
	Out[23]: 
	                   A         B         C
	2000-01-01 -0.275261 -0.608021  1.300469
	2000-01-02 -1.277576 -2.158026 -1.549583
	2000-01-03 -1.051528 -1.487722 -0.179801
	2000-01-04 -1.306302 -0.098408  0.262244
	2000-01-05       NaN       NaN       NaN
	2000-01-06       NaN       NaN       NaN
	2000-01-07       NaN       NaN       NaN
	2000-01-08       NaN       NaN       NaN
	2000-01-09 -1.704379  1.148818 -2.220629
	2000-01-10 -1.185733 -0.049463 -1.236132

	In [24]: tsdf.apply(pd.Series.interpolate)
	Out[24]: 
	                   A         B         C
	2000-01-01 -0.275261 -0.608021  1.300469
	2000-01-02 -1.277576 -2.158026 -1.549583
	2000-01-03 -1.051528 -1.487722 -0.179801
	2000-01-04 -1.306302 -0.098408  0.262244
	2000-01-05 -1.385917  0.151037 -0.234331
	2000-01-06 -1.465533  0.400482 -0.730905
	2000-01-07 -1.545148  0.649928 -1.227480
	2000-01-08 -1.624764  0.899373 -1.724055
	2000-01-09 -1.704379  1.148818 -2.220629
	2000-01-10 -1.185733 -0.049463 -1.236132

Applying elementwise Python functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Since not all functions can be vectorized (accept NumPy arrays and return another array or value), the methods ``applymap()`` on DataFrame and analogously ``map()`` on Series accept any Python function taking a single value and returning a single value. For example:

.. ipython::

	In [25]: df
	Out[25]: 
	        one     three       two
	a  1.589450       NaN  1.117724
	b -0.252391  0.511787 -0.580168
	c -0.098049  2.785835  1.347622
	d       NaN -0.752325 -0.198108

	In [28]: df['one'].map(lambda x: len(str(x)))
	Out[28]: 
	a    13
	b    15
	c    16
	d     3
	Name: one, dtype: int64

	In [29]: df.applymap(lambda x: len(str(x)))
	Out[29]: 
	   one  three  two
	a   13      3   12
	b   15     14   15
	c   16     13   13
	d    3     14   15

Reindexing and altering labels
------------------------------

``reindex()`` is the fundamental data alignment method in pandas. It is used to implement nearly all other features relying on label-alignment functionality. To reindex means to conform the data to match a given set of labels along a particular axis. This accomplishes several things:

	- Reorders the existing data to match a new set of labels
	- Inserts missing value (NA) markers in label locations where no data for that label existed
	- If specified, fill data for missing labels using logic (highly relevant to working with time series data)

Here is a simple example:

.. ipython::

	In [30]: s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])

	In [31]: s.reindex(['e', 'b', 'f', 'd'])
	Out[31]: 
	e   -0.056929
	b   -0.747146
	f         NaN
	d   -0.049556
	dtype: float64

With a DataFrame, you can simultaneously reindex the index and columns:

.. ipython::

	In [32]: df
	Out[32]: 
	        one     three       two
	a  1.589450       NaN  1.117724
	b -0.252391  0.511787 -0.580168
	c -0.098049  2.785835  1.347622
	d       NaN -0.752325 -0.198108

	In [33]: df.reindex(index=['c', 'f', 'b'], columns=['three', 'two', 'one'])
	Out[33]: 
	      three       two       one
	c  2.785835  1.347622 -0.098049
	f       NaN       NaN       NaN
	b  0.511787 -0.580168 -0.252391

Reindexing to align with another object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You may wish to take an object and reindex its axes to be labeled the same as another object.

.. ipython::

	In [36]: df.reindex_like(df.ix[:2, 2:])
	Out[36]: 
	        two
	a  1.117724
	b -0.580168

Aligning objects with each other with ``align``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``align()`` method is the fastest way to simultaneously align two objects. It supports a ``join`` argument (related to joining and merging):

	- ``join='outer'``: take the union of the indexes (default)
	- ``join='left'``: use the calling object’s index
	- ``join='right'``: use the passed object’s index
	- ``join='inner'``: intersect the indexes

It returns a tuple with both of the reindexed Series:

.. ipython::

	In [37]: s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])

	In [38]: s1 = s[:4]

	In [39]: s2 = s[1:]

	In [40]: s1.align(s2)
	Out[40]: 
	(a    0.776171
	 b   -1.620927
	 c   -0.727979
	 d    1.258058
	 e         NaN
	 dtype: float64, a         NaN
	 b   -1.620927
	 c   -0.727979
	 d    1.258058
	 e    1.393465
	 dtype: float64)

	In [41]: s1.align(s2, join='inner')
	Out[41]: 
	(b   -1.620927
	 c   -0.727979
	 d    1.258058
	 dtype: float64, b   -1.620927
	 c   -0.727979
	 d    1.258058
	 dtype: float64)

	In [42]: s1.align(s2, join='left')
	Out[42]: 
	(a    0.776171
	 b   -1.620927
	 c   -0.727979
	 d    1.258058
	 dtype: float64, a         NaN
	 b   -1.620927
	 c   -0.727979
	 d    1.258058
	 dtype: float64)

For DataFrames, the join method will be applied to both the index and the columns by default:

.. ipython::

	In [43]: df = pd.DataFrame({'one' : pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
	   ....: 'two' : pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
	   ....: 'three' : pd.Series(np.random.randn(3), index=['b', 'c', 'd'])})

	In [49]: df2 = pd.DataFrame({'two' : pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'e']),
	   ....: 'three' : pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd'])})

	In [49]: 

	In [50]: df2
	Out[50]: 
	      three       two
	a  1.113726 -0.373518
	b  0.940933  1.097591
	c -1.681262 -0.516124
	d -0.104200       NaN
	e       NaN -1.940613

	In [51]: df.align(df2, join='inner')
	Out[51]: 
	(      three       two
	 a       NaN -0.878554
	 b -1.269023 -1.076222
	 c -0.220628  0.606864
	 d  0.577280  0.762907,       three       two
	 a  1.113726 -0.373518
	 b  0.940933  1.097591
	 c -1.681262 -0.516124
	 d -0.104200       NaN)

You can also pass an axis option to only align on the specified ``axis``:

.. ipython::

	In [52]: df.align(df2, join='inner', axis=0)
	Out[52]: 
	(        one     three       two
	 a -0.355976       NaN -0.878554
	 b -0.235692 -1.269023 -1.076222
	 c  1.413069 -0.220628  0.606864
	 d       NaN  0.577280  0.762907,       three       two
	 a  1.113726 -0.373518
	 b  0.940933  1.097591
	 c -1.681262 -0.516124
	 d -0.104200       NaN)

Filling while reindexing
~~~~~~~~~~~~~~~~~~~~~~~~

``reindex()`` takes an optional parameter method which is a filling method chosen from the following options:

	- pad / ffill: Fill values forward
	- bfill / backfill: Fill values backward
	- nearest: Fill from the nearest index value

These methods require that the indexes are **ordered** increasing or decreasing.

We illustrate these fill methods on a simple Series:

.. ipython::

	In [53]: rng = pd.date_range('1/3/2000', periods=8)

	In [54]: ts = pd.Series(np.random.randn(8), index=rng)

	In [55]: ts2 = ts[[0, 3, 6]]

	In [56]: ts
	Out[56]: 
	2000-01-03   -0.979373
	2000-01-04   -0.371387
	2000-01-05    0.528431
	2000-01-06    0.532542
	2000-01-07    0.163115
	2000-01-08    0.876436
	2000-01-09   -0.786435
	2000-01-10   -0.258264
	Freq: D, dtype: float64

	In [57]: ts2
	Out[57]: 
	2000-01-03   -0.979373
	2000-01-06    0.532542
	2000-01-09   -0.786435
	dtype: float64

	In [58]: ts2.reindex(ts.index)
	Out[58]: 
	2000-01-03   -0.979373
	2000-01-04         NaN
	2000-01-05         NaN
	2000-01-06    0.532542
	2000-01-07         NaN
	2000-01-08         NaN
	2000-01-09   -0.786435
	2000-01-10         NaN
	Freq: D, dtype: float64

	In [59]: ts2.reindex(ts.index, method='ffill')
	Out[59]: 
	2000-01-03   -0.979373
	2000-01-04   -0.979373
	2000-01-05   -0.979373
	2000-01-06    0.532542
	2000-01-07    0.532542
	2000-01-08    0.532542
	2000-01-09   -0.786435
	2000-01-10   -0.786435
	Freq: D, dtype: float64

	In [60]: ts2.reindex(ts.index, method='bfill')
	Out[60]: 
	2000-01-03   -0.979373
	2000-01-04    0.532542
	2000-01-05    0.532542
	2000-01-06    0.532542
	2000-01-07   -0.786435
	2000-01-08   -0.786435
	2000-01-09   -0.786435
	2000-01-10         NaN
	Freq: D, dtype: float64

	In [61]: ts2.reindex(ts.index, method='nearest')
	Out[61]: 
	2000-01-03   -0.979373
	2000-01-04   -0.979373
	2000-01-05    0.532542
	2000-01-06    0.532542
	2000-01-07    0.532542
	2000-01-08   -0.786435
	2000-01-09   -0.786435
	2000-01-10   -0.786435
	Freq: D, dtype: float64

Dropping labels from an axis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A method closely related to reindex is the ``drop()`` function. It removes a set of labels from an axis:

.. ipython::

	In [62]: df
	Out[62]: 
	        one     three       two
	a -0.355976       NaN -0.878554
	b -0.235692 -1.269023 -1.076222
	c  1.413069 -0.220628  0.606864
	d       NaN  0.577280  0.762907

	In [63]: df.drop(['a', 'd'], axis=0)
	Out[63]: 
	        one     three       two
	b -0.235692 -1.269023 -1.076222
	c  1.413069 -0.220628  0.606864

	In [64]: df.drop(['one'], axis=1)
	Out[64]: 
	      three       two
	a       NaN -0.878554
	b -1.269023 -1.076222
	c -0.220628  0.606864
	d  0.577280  0.762907

Renaming / mapping labels
~~~~~~~~~~~~~~~~~~~~~~~~~

The ``rename()`` method allows you to relabel an axis based on some mapping (a dict or Series) or an arbitrary function.

.. ipython::

	In [65]: s
	Out[65]: 
	a    0.776171
	b   -1.620927
	c   -0.727979
	d    1.258058
	e    1.393465
	dtype: float64

	In [66]: s.rename(str.upper)
	Out[66]: 
	A    0.776171
	B   -1.620927
	C   -0.727979
	D    1.258058
	E    1.393465
	dtype: float64

If you pass a function, it must return a value when called with any of the labels (and must produce a set of unique values). But if you pass a dict or Series, it need only contain a subset of the labels as keys:

.. ipython::

	In [67]: df.rename(columns={'one' : 'foo', 'two' : 'bar'},
	   ....: index={'a' : 'apple', 'b' : 'banana', 'd' : 'durian'})
	Out[67]: 
	             foo     three       bar
	apple  -0.355976       NaN -0.878554
	banana -0.235692 -1.269023 -1.076222
	c       1.413069 -0.220628  0.606864
	durian       NaN  0.577280  0.762907

The ``rename()`` method also provides an ``inplace`` named parameter that is by default False and copies the underlying data. Pass ``inplace=True`` to rename the data in place.

Sorting by index and value
--------------------------

There are two obvious kinds of sorting that you may be interested in: sorting by label and sorting by actual values. The primary method for sorting axis labels (indexes) across data structures is the ``sort_index()`` method.

.. ipython::

	In [68]: unsorted_df = df.reindex(index=['a', 'd', 'c', 'b'],
	   ....: columns=['three', 'two', 'one'])

	In [69]: unsorted_df.sort_index()
	Out[69]: 
	      three       two       one
	a       NaN -0.878554 -0.355976
	b -1.269023 -1.076222 -0.235692
	c -0.220628  0.606864  1.413069
	d  0.577280  0.762907       NaN

	In [70]: unsorted_df.sort_index(ascending=False)
	Out[70]: 
	      three       two       one
	d  0.577280  0.762907       NaN
	c -0.220628  0.606864  1.413069
	b -1.269023 -1.076222 -0.235692
	a       NaN -0.878554 -0.355976

	In [71]: unsorted_df.sort_index(axis=1)
	Out[71]: 
	        one     three       two
	a -0.355976       NaN -0.878554
	d       NaN  0.577280  0.762907
	c  1.413069 -0.220628  0.606864
	b -0.235692 -1.269023 -1.076222

``DataFrame.sort_index()`` can accept an optional ``by`` argument for ``axis=0`` which will use an arbitrary vector or a column name of the DataFrame to determine the sort order:

.. ipython::

	In [72]: df1 = pd.DataFrame({'one':[2,1,1,1],'two':[1,3,2,4],'three':[5,4,3,2]})

	In [73]: df1.sort_index(by='two')
	Out[73]: 
	   one  three  two
	0    2      5    1
	2    1      3    2
	1    1      4    3
	3    1      2    4

The by argument can take a list of column names, e.g.:

.. ipython::

	In [74]: df1[['one', 'two', 'three']].sort_index(by=['one','two'])
	Out[74]: 
	   one  two  three
	2    1    2      3
	1    1    3      4
	3    1    4      2
	0    2    1      5

Smallest / largest values
~~~~~~~~~~~~~~~~~~~~~~~~~

Series has the ``nsmallest()`` and ``nlargest()`` methods which return the smallest or largest n values. For a large Series this can be much faster than sorting the entire Series and calling ``head(n)`` on the result.

.. ipython::

	In [77]: s = pd.Series(np.random.permutation(10))

	In [78]: s
	Out[78]: 
	0    5
	1    2
	2    0
	3    9
	4    6
	5    3
	6    8
	7    1
	8    4
	9    7
	dtype: int64

	In [79]: s.order()
	Out[79]: 
	2    0
	7    1
	1    2
	5    3
	8    4
	0    5
	4    6
	9    7
	6    8
	3    9
	dtype: int64

	In [80]: s.nsmallest(3)
	Out[80]: 
	2    0
	7    1
	1    2
	dtype: int64

	In [81]: s.nlargest(3)
	Out[81]: 
	3    9
	6    8
	9    7
	dtype: int64

Sorting by a multi-index column
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You must be explicit about sorting when the column is a multi-index, and fully specify all levels to ``by``.

.. ipython::

	In [83]: df1.columns = pd.MultiIndex.from_tuples([('a','one'),('a','two'),('b','three')])

	In [84]: df1.sort_index(by=('a','two'))
	Out[84]: 
	    a         b
	  one two three
	3   1   2     4
	2   1   3     2
	1   1   4     3
	0   2   5     1


Indexing and selecting data
---------------------------

Different Choices for Indexing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pandas supports three types of multi-axis indexing.

	- ``.loc`` is primarily label based, but may also be used with a boolean array. ``.loc`` will raise ``KeyError`` when the items are not found. Allowed inputs are:

		- A single label, e.g. ``5`` or ``'a'``, (note that ``5`` is interpreted as a `label` of the index. This use is not an integer position along the index)
		- A list or array of labels ``['a', 'b', 'c']``
		- A slice object with labels ``'a':'f'``, (note that contrary to usual python slices, both the start and the stop are included!)
		- A boolean array

	- ``.iloc`` is primarily integer position based (from ``0`` to ``length-1`` of the axis), but may also be used with a boolean array. ``.iloc`` will raise ``IndexError`` if a requested indexer is out-of-bounds, except slice indexers which allow out-of-bounds indexing. Allowed inputs are:

		- An integer e.g. ``5``
		- A list or array of integers ``[4, 3, 0]``
		- A slice object with ints ``1:7``
		- A boolean array

	- ``.ix`` supports mixed integer and label based access. It is primarily label based, but will fall back to integer positional access unless the corresponding axis is of integer type. ``.ix`` is the most general and will support any of the inputs in ``.loc`` and ``.iloc``. ``.ix`` also supports floating point label schemes. ``.ix`` is exceptionally useful when dealing with mixed positional and label based hierachical indexes.

	However, when an axis is integer based, ONLY label based access and not positional access is supported. Thus, in such cases, it's usually better to be explicit and use ``.iloc`` or ``.loc``.

Selection By Position
~~~~~~~~~~~~~~~~~~~~~

A few basic examples:

.. ipython::

	In [98]: s1 = pd.Series(np.random.randn(5),index=list(range(0,10,2)))

	In [99]: s1
	Out[99]: 
	0   -0.293996
	2    0.231253
	4    0.058106
	6    0.168732
	8    0.680887
	dtype: float64

	In [100]: s1.iloc[:3]
	Out[100]: 
	0   -0.293996
	2    0.231253
	4    0.058106
	dtype: float64

	In [101]: s1.iloc[3]
	Out[101]: 0.16873213597476788

	In [102]: s1.iloc[:3] = 0

	In [103]: s1
	Out[103]: 
	0    0.000000
	2    0.000000
	4    0.000000
	6    0.168732
	8    0.680887
	dtype: float64

With a DataFrame:

.. ipython::

	In [105]: df1 = pd.DataFrame(np.random.randn(6,4),
	   .....:                    index=list(range(0,12,2)),
	   .....:                    columns=list(range(0,8,2)))

	In [106]: df1
	Out[106]: 
	           0         2         4         6
	0   0.343019  0.015635  0.524095 -1.430981
	2   0.099939  1.960517 -0.809863 -0.241903
	4  -0.696110 -2.077300 -0.135080 -0.376708
	6   0.618550 -0.706869  0.667799  0.805739
	8  -0.181700  1.035451 -0.498299  0.905128
	10 -0.257736  1.314887  0.793187  1.430031

	In [107]: df1.iloc[:3]
	Out[107]: 
	          0         2         4         6
	0  0.343019  0.015635  0.524095 -1.430981
	2  0.099939  1.960517 -0.809863 -0.241903
	4 -0.696110 -2.077300 -0.135080 -0.376708

	In [108]: df1.iloc[1:5, 2:4]
	Out[108]: 
	          4         6
	2 -0.809863 -0.241903
	4 -0.135080 -0.376708
	6  0.667799  0.805739
	8 -0.498299  0.905128

	In [109]: df1.iloc[[1, 3, 5], [1, 3]]
	Out[109]: 
	           2         6
	2   1.960517 -0.241903
	6  -0.706869  0.805739
	10  1.314887  1.430031

	In [110]: df1.iloc[1:3, :]
	Out[110]: 
	          0         2         4         6
	2  0.099939  1.960517 -0.809863 -0.241903
	4 -0.696110 -2.077300 -0.135080 -0.376708

	In [111]: df1.iloc[:, 1:3]
	Out[111]: 
	           2         4
	0   0.015635  0.524095
	2   1.960517 -0.809863
	4  -2.077300 -0.135080
	6  -0.706869  0.667799
	8   1.035451 -0.498299
	10  1.314887  0.793187

	In [112]: df1.iloc[1, 1]
	Out[112]: 1.9605165206385684

	In [113]: df1.iloc[1]
	Out[113]: 
	0    0.099939
	2    1.960517
	4   -0.809863
	6   -0.241903
	Name: 2, dtype: float64

Boolean indexing
~~~~~~~~~~~~~~~~

Another common operation is the use of boolean vectors to filter the data. The operators are: ``|`` for ``or``, ``&`` for ``and``, and ``~`` for ``not``. These must be grouped by using parentheses.

Using a boolean vector to index a Series works exactly as in a numpy ndarray:

.. ipython::

	In [114]: s = pd.Series(range(-3, 4))

	In [115]: s
	Out[115]: 
	0   -3
	1   -2
	2   -1
	3    0
	4    1
	5    2
	6    3
	dtype: int64

	In [116]: s[s > 0]
	Out[116]: 
	4    1
	5    2
	6    3
	dtype: int64

	In [117]: s[(s < -1) | (s > 0.5)]
	Out[117]: 
	0   -3
	1   -2
	4    1
	5    2
	6    3
	dtype: int64

	In [118]: s[~(s < 0)]
	Out[118]: 
	3    0
	4    1
	5    2
	6    3
	dtype: int64

You may select rows from a DataFrame using a boolean vector the same length as the DataFrame's index (for example, something derived from one of the columns of the DataFrame):

.. ipython::

	In [122]: df = pd.DataFrame({'a' : ['one', 'one', 'two', 'three', 'two', 'one', 'six'],
	   .....:                    'b' : ['x', 'y', 'y', 'x', 'y', 'x', 'x'],
	   .....:                    'c' : np.random.randn(7)})

	In [123]: df
	Out[123]: 
	       a  b         c
	0    one  x  0.717041
	1    one  y -0.296828
	2    two  y -0.377718
	3  three  x -0.353044
	4    two  y -1.156507
	5    one  x -0.777970
	6    six  x  0.437026

	In [124]: df[df['c'] > 0]
	Out[124]: 
	     a  b         c
	0  one  x  0.717041
	6  six  x  0.437026

	In [125]: criterion = df['a'].map(lambda x: x.startswith('t'))

	In [128]: df[criterion]
	Out[128]: 
	       a  b         c
	2    two  y -0.377718
	3  three  x -0.353044
	4    two  y -1.156507

	In [129]: df[criterion & (df['b'] == 'x')]
	Out[129]: 
	       a  b         c
	3  three  x -0.353044

	In [130]: df.loc[criterion & (df['b'] == 'x'), 'b':'c']
	Out[130]: 
	   b         c
	3  x -0.353044

Indexing with ``isin``
~~~~~~~~~~~~~~~~~~~~~~

Consider the ``isin`` method of Series, which returns a boolean vector that is true wherever the Series elements exist in the passed list. This allows you to select rows where one or more columns have values you want:

.. ipython::

	In [131]: s = pd.Series(np.arange(5), index=np.arange(5)[::-1])

	In [132]: s
	Out[132]: 
	4    0
	3    1
	2    2
	1    3
	0    4
	dtype: int64

	In [133]: s.isin([2, 4, 6])
	Out[133]: 
	4    False
	3    False
	2     True
	1    False
	0     True
	dtype: bool

	In [134]: s[s.isin([2, 4, 6])]
	Out[134]: 
	2    2
	0    4
	dtype: int64

The same method is available for ``Index`` objects and is useful for the cases when you don't know which of the sought labels are in fact present:

.. ipython::

	In [135]: s[s.index.isin([2, 4, 6])]
	Out[135]: 
	4    0
	2    2
	dtype: int64

	In [136]: s[[2, 4, 6]]
	Out[136]: 
	2     2
	4     0
	6   NaN
	dtype: float64

In addition to that, ``MultiIndex`` allows selecting a separate level to use in the membership check:

.. ipython::

	In [138]: s_mi = pd.Series(np.arange(6),
	   .....: index=pd.MultiIndex.from_product([[0, 1], ['a', 'b', 'c']]))

	In [139]: s_mi
	Out[139]: 
	0  a    0
	   b    1
	   c    2
	1  a    3
	   b    4
	   c    5
	dtype: int64

	In [140]: s_mi.iloc[s_mi.index.isin([(1, 'a'), (2, 'b'), (0, 'c')])]
	Out[140]: 
	0  c    2
	1  a    3
	dtype: int64

	In [141]: s_mi.iloc[s_mi.index.isin(['a', 'c', 'e'], level=1)]
	Out[141]: 
	0  a    0
	   c    2
	1  a    3
	   c    5
	dtype: int64

DataFrame also has an ``isin`` method. When calling ``isin``, pass a set of values as either an array or dict. If values is an array, ``isin`` returns a DataFrame of booleans that is the same shape as the original DataFrame, with True wherever the element is in the sequence of values.

.. ipython::

	In [143]: df = pd.DataFrame({'vals': [1, 2, 3, 4], 'ids': ['a', 'b', 'f', 'n'],
	   .....: 'ids2': ['a', 'n', 'c', 'n']})

	In [146]: df
	Out[146]: 
	  ids ids2  vals
	0   a    a     1
	1   b    n     2
	2   f    c     3
	3   n    n     4

	In [144]: df.isin(['a', 'b', 1, 3])
	Out[144]: 
	     ids   ids2   vals
	0   True   True   True
	1   True  False  False
	2  False  False   True
	3  False  False  False

	In [145]: df.isin({'ids': ['a', 'b'], 'vals': [1, 3]})
	Out[145]: 
	     ids   ids2   vals
	0   True  False   True
	1   True  False  False
	2  False  False   True
	3  False  False  False

Set / Reset Index
~~~~~~~~~~~~~~~~~

DataFrame has a ``set_index`` method which takes a column name (for a regular ``Index``) or a list of column names (for a ``MultiIndex``), to create a new, indexed DataFrame:

.. ipython::

	In [153]: data = pd.DataFrame({'a' : ['bar', 'bar', 'foo', 'foo'],
	   .....:                      'b' : ['one', 'two', 'one', 'two'],
	   .....:                      'c' : ['z', 'y', 'x', 'w'],
	   .....:                      'd' : range(1, 5)})

	In [154]: data
	Out[154]: 
	     a    b  c  d
	0  bar  one  z  1
	1  bar  two  y  2
	2  foo  one  x  3
	3  foo  two  w  4

	In [156]: data.set_index('c')
	Out[156]: 
	     a    b  d
	c             
	z  bar  one  1
	y  bar  two  2
	x  foo  one  3
	w  foo  two  4

	In [157]: data.set_index(['a', 'b'])
	Out[157]: 
	         c  d
	a   b        
	bar one  z  1
	    two  y  2
	foo one  x  3
	    two  w  4

	In [158]: data.set_index(['a', 'b'], inplace=True)

``reset_index`` is the inverse operation to ``set_index``.

.. ipython::

	In [160]: data.reset_index()
	Out[160]: 
	     a    b  c  d
	0  bar  one  z  1
	1  bar  two  y  2
	2  foo  one  x  3
	3  foo  two  w  4

	In [161]: data.reset_index(level='a')
	Out[161]: 
	       a  c  d
	b             
	one  bar  z  1
	two  bar  y  2
	one  foo  x  3
	two  foo  w  4

.. todo:: Complete **Pandas** section
