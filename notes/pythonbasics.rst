=============
Python basics
=============

.. contents::


Your first program
------------------

Launch your favorite environment:

	- **IPython** shell by typing "ipython" from a Linux/Mac terminal, or from the Windows cmd shell
	- **Python** shell by typing "python" from a Linux/Mac terminal, or from the Windows cmd shell
	- **Spyder** includes both **IPython** and **Python** as interactive shells
	- `Wakari.io`_ has a variety of shells, including **Ipython** and **Python**
	
Once you have started the interpreter (wait for ``>>>`` is you use pure Python, or ``In [1]:`` if you use IPython), type::

	>>> print('Hello world!')
	Hello world!

Let's play around and see what we can get without any knowledge of programming. Try some simple math calculations::

	>>> 2*2
	4
	>>> 2+3
	5
	>>> 4*(2+3)
	20
	>>> 1/2
	0.5
	>>> 1/3
	0.3333333333333333
	>>> 5-10
	-5
	>>> 0/0
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	ZeroDivisionError: division by zero

Everything seems to work as expected. The last line produces some internal complaints - we will get back to it later.

We can define some variables and ask the shell who they are::

	>>> a = 2
	>>> type(a)
	<class 'int'>
	>>> b = .1
	>>> type(b)
	<class 'float'>
	>>> c = 'Hello'
	>>> type(c)
	<class 'str'>

Just to test the sanity of the language we can try adding up different variable types::

	>>> a + b
	2.1
	>>> c + c
	'HelloHello'
	>>> a + c
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: unsupported operand type(s) for +: 'int' and 'str'

Clearly, Python does not know how to add up integers to strings. Neither do we...

What if we call something that does not exist yet? ::

	>>> d
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	NameError: name 'd' is not defined

Variable names can only contain numbers, letters (both upper and lower case), and underscores (_). They must begin with a letter or an underscore and are CaSe SeNsItIve. Some words are reserved in Python and so cannot be used for variable names.


Native Data Types
-----------------

Numbers
~~~~~~~

There are three numeric types:

	- integers (``int``)
	- floating point (``float``)
	- complex (``complex``)

Hopefully, we will not need the last one. But if you see something like ``3+5j`` or ``6-7J``, you know you are looking at ``complex`` type.

Note that if you want to define a ``float``, you have to use the dot (``.``), otherwise the output is an integer. For example, ::

	>>> type(1)
	<class 'int'>
	>>> type(1.)
	<class 'float'>
	>>> type(float(1))
	<class 'float'>
	>>> type(int(1.))
	<class 'int'>
	>>> type(0)
	<class 'int'>
	>>> type(0.)
	<class 'float'>
	>>> type(.0)
	<class 'float'>
	>>> type(0.0)
	<class 'float'>

This was extremely important in Python 2 and was the source of many inadvertent errors (try dividing 1 by 2 - you'd be surprised). With Python 3 not anymore, but the general advice of being explicit in what you mean is still there.

Division (``/``) always returns a ``float``. To do floor division and get an integer result (discarding any fractional result) you can use the ``//`` operator; to calculate the remainder you can use ``%``::

	>>> 17 / 3  # classic division returns a float
	5.666666666666667
	>>>
	>>> 17 // 3  # floor division discards the fractional part
	5
	>>> 17 % 3  # the % operator returns the remainder of the division
	2
	>>> 5 * 3 + 2  # result * divisor + remainder
	17

Notice one way of commenting your code: just use ``#`` after the code and before any text.

Calculating powers is done with ``**`` operator. ::

	>>> 2**2
	4
	>>> 3**3
	27
	>>> 4**.5
	2.0


Booleans
~~~~~~~~

``bool`` type is essential for any programming logic. Normally, truth and falcity are defined as ``True`` and ``False``::

	>>> print(x)
	True
	>>> x = True
	>>> print(x)
	True
	>>> type(x)
	<class 'bool'>
	>>> y = False
	>>> print(y)
	False
	>>> type(y)
	<class 'bool'>

Additionally, all non-empty and non-zero values are interpreted by ``bool()`` function as ``True``, while all empty and zero values are ``False``::

	>>> print(bool(1), bool(1.), bool(-.1))
	True True True
	>>> print(bool(0), bool(.0), bool(None), bool(''), bool([]))
	False False False False False


Strings
~~~~~~~

Strings can be difined using both single (``'...'``) or double quotes (``"..."``). Backslash can be used to escape quotes. ::

	>>> 'spam eggs'  # single quotes
	'spam eggs'
	>>> 'doesn\'t'  # use \' to escape the single quote...
	"doesn't"
	>>> "doesn't"  # ...or use double quotes instead
	"doesn't"
	>>> '"Yes," he said.'
	'"Yes," he said.'
	>>> "\"Yes,\" he said."
	'"Yes," he said.'
	>>> '"Isn\'t," she said.'
	'"Isn\'t," she said.'

The ``print()`` function produces a more readable output, by omitting the enclosing quotes and by printing escaped and special characters::

	>>> '"Isn\'t," she said.'
	'"Isn\'t," she said.'
	>>> print('"Isn\'t," she said.')
	"Isn't," she said.
	>>> s = 'First line.\nSecond line.'  # \n means newline
	>>> s  # without print(), \n is included in the output
	'First line.\nSecond line.'
	>>> print(s)  # with print(), \n produces a new line
	First line.
	Second line.

If you don't want characters prefaced by ``\`` to be interpreted as special characters, you can use `raw strings` by adding an ``r`` before the first quote:

	>>> print('C:\some\name')  # here \n means newline!
	C:\some
	ame
	>>> print(r'C:\some\name')  # note the r before the quote
	C:\some\name

Python is very sensitive to code aesthetics (see `Style Guide`_). In particular, you shoud restrict yourself to 79 characters in one line! Use parenthesis to break long strings::

	>>> text = ('Put several strings within parentheses '
	            'to have them joined together.')
	>>> text
	'Put several strings within parentheses to have them joined together.'

Strings can be constructed using math operators and by converting numbers into strings via ``str()`` function::

	>>> 2 * 'a' + '_' + 3 * 'b' + '_' + 4 * (str(.5) + '_')
	'aa_bbb_0.5_0.5_0.5_0.5_'

Note that Python can not convert numbers into strings automatically. Unless you use ``print()`` function or convert explicitely.::

	>>> 'a' + 1
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: Can't convert 'int' object to str implicitly
	>>> 'a' + str(1)
	'a1'
	>>> print('a', 1)
	a 1


Lists
~~~~~

.. todo:: Write **Lists** section

Tuples
~~~~~~

.. todo:: Write **Tuples** section

Dictionaries
~~~~~~~~~~~~

.. todo:: Write **Dictionaries** section

Sets
~~~~

.. todo:: Write **Sets** section


Indexing
--------

Python data containers (including strings and lists) can be `sliced` to access their specific parts. Counting in Python starts from zero. Keep this in mind when you want to access a specific charcter of a string::

	>>> word = 'Python'
	>>> word[0]  # character in position 0
	'P'
	>>> word[5]  # character in position 5
	'n'

Indices may also be negative numbers, to start counting from the right::

	>>> word[-1]  # last character
	'n'
	>>> word[-2]  # second-to-last character
	'o'
	>>> word[-6]
	'P'

Going beyond a single charcter::

	>>> word[0:2]  # characters from position 0 (included) to 2 (excluded)
	'Py'
	>>> word[2:5]  # characters from position 2 (included) to 5 (excluded)
	'tho'

Slice indices have useful defaults; an omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced.::

	>>> word[:2]  # character from the beginning to position 2 (excluded)
	'Py'
	>>> word[4:]  # characters from position 4 (included) to the end
	'on'
	>>> word[-2:] # characters from the second-last (included) to the end
	'on'

One could be interested only in even/odd characters in the string. In that case, we need a third index in the slice::

	>>> word[::2]
	'Pto'
	>>> word[1::2]
	'yhn'

Negative index in the third position of the slice reverses the count::

	>>> word[::-1]
	'nohtyP'
	>>> word[::-2]
	'nhy'

One way to remember how slices work is to think of the indices as pointing between characters, with the left edge of the first character numbered 0. Then the right edge of the last character of a string of n characters has index n, for example::

	 +---+---+---+---+---+---+
	 | P | y | t | h | o | n |
	 +---+---+---+---+---+---+
	 0   1   2   3   4   5   6
	-6  -5  -4  -3  -2  -1


Control flow
------------

.. todo:: Write **Control flow** section

if/elif/else

for/range

while/break/continue

list comprehensions

Functions
---------

.. todo:: Write **Functions** section

def, return, default values, keyword variables

Classes
-------

.. todo:: Write **Classes** section

def, methods, attributes, inheritance

Modules and Packages
--------------------

.. todo:: Write **Modules and Packages** section

import, ``__all__``, ``__main__``

Documenenting your code
-----------------------

.. todo:: Write **Documenenting your code** section

docstrings, numpydoc


.. _`Wakari.io`: https://www.wakari.io
.. _`Style Guide`: https://www.python.org/dev/peps/pep-0008/
