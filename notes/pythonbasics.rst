=============
Python basics
=============

Your first program
------------------

Launch your favorite environment:

	- **Ipython** shell by typing "ipython" from a Linux/Mac terminal, or from the Windows cmd shell
	- **Python** shell by typing "python" from a Linux/Mac terminal, or from the Windows cmd shell
	- **Spyder** includes both **IPython** and **Python** as interactive shells
	- `Wakari.io`_ has a variety of shells, including **Ipython** and **Python**
	
.. _`Wakari.io`: https://www.wakari.io

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
