from math import *

# ------------------------------------------------------------------------- #
#																			#
# Question 1: Numbers														#
# ------------------------------------------------------------------------- #
def product_digits(n):
	"""
	Calculates the product of the digits of n through recursion.

	Args:
		n: a nonnegative integer
	"""
	assert n >= 0 and isinstance(n, int)
	# base case
	if ________:
		return n
	# recursive call
	else:
		right_digit = ________
		return ________ * product_digits(________)

def power(x, n):
	"""
	Calculates the power of x to the n.

	Args:
		x: base, any number
		n: nonnegative integer
	"""
	assert n >= 0 and isinstance(n, int)
	if ________:
		return 1
	else:
		return ________

def factorial(n):
	"""
	Calculates the factorial of n, n!
	n! = n * (n - 1) * (n - 2) * ... * 2 * 1

	Args:
		n: nonnegative integer
	"""
	assert n >= 0 and isinstance(n, int)
	# base case
	if ________:
		return ________
	else:
		return ________

def double_factorial(n):
	"""
	Calculates the double factorial of n, n!!
	n!! = n * (n - 2) * (n - 4) * ... * 4 * 2 for n is even
	n!! = n * (n - 2) * (n - 4) * ... * 3 * 1 for n is odd
	(-1)!! = 0!! = 1 by definition

	Args:
		n: an integer in the range of [-1, +∞)
	"""
	assert n >= -1 and isinstance(n, int)
	# base case
	if ________:
		return ________
	# recursive call
	else:
		return ________

def modulo(n, p):
	"""
	Emulates the modulo function n % p which calculates the remainder of n / p
	Perform this recursively.

	Args:
		n: nonnegative number
		p: positive integer
	"""
	assert n >= 0 and p >= 1
	assert isinstance(p, int)
	# base case
	if ________:
		return ________
	# recursive call
	else:
		return ________

def divides(a, b):
	"""
	Computes whether a divides into b evenly.

	Args:
		a: positive integer
		b: nonnegetive integer
	"""
	return ________

def gcd(x, y):
	"""
	Calculates the greatest common denominator of x and y.
	Say the answer is n; the equation a * x + b * y = n can then be satisfied
	for integer values of a and b.
	HINT: Look up Euclid's Algorithm.

	Args:
		x: a positive integer, larger than or equal to y
		y: a nonnegative integer, smaller than or equal to y

	Returns:
		a positive integer
	"""
	assert isinstance(x, int) and x >= y and x > 0
	assert isinstance(y, int) and y >= 0

	# base case 1
	if ________:
		return x
	# base case 2
	elif ________:
		return 1
	# recursive call
	else:
		return gcd(________, ________)

# ------------------------------------------------------------------------- #
#																			#
# Question 2: Strings														#
# ------------------------------------------------------------------------- #
def is_palindrome(string):
	"""
	Determines if a string is a palindrome.
	"""
	if ________:
		return ________
	else:
		return ________ and is_palindrome(________)

def repeating(string):
	"""
	Determines if the provided string has any substrings which are repeated
	throughout the string without irregularities in the pattern i.e. 'abcabc'
	has the reptetition 'abc' but 'abcabcd' has no repetition.

	Args:
		string: string we're looking to see if repeats

	Returns:
		the shorted substring which is repeated throughout; None if no repetitions
	"""
	def repetition(base_str, repeated_str):
		"""
		Helper function, determines if a specified substring is repeated
		throughout a base string.

		Args:
			base_str: string being tested for repetitions
			repeated_str: substring to test if repeated

		Returns:
			True or False if repeated_str is repeated throughout or not respectively
		"""
		if ________:
			return True
		else:
			return ________ and repetition(________, ________)

	rep = None
	for i in range(1, len(string) - 1):
		sub = ________
		if ________:
			rep = sub
	return rep

# ------------------------------------------------------------------------- #
#																			#
# Question 3: Sequences														#
# ------------------------------------------------------------------------- #
def thue_morse_sequence(n):
	"""
	Returns the first n elements of the Thue-Morse
	Sequnce through recursive calls.
	LINK: https://en.wikipedia.org/wiki/Thue–Morse_sequence

	Args:
		n: positive integer
	"""
	assert n > 0 and isinstance(n, int)
	if ________:
		return '0'
	else:
		"""
			power_of_two (p_o_2) is the largest power of two less than n
			p_o_2 examples:
			n == 4 --> p_o_2 = 2
			n == 5 --> p_o_2 = 4
			n == 7 --> p_o_2 = 4
			n == 8 --> p_o_2 = 4
			n == 9 --> p_o_2 = 8
		"""
		power_of_two = ________
		seq = thue_morse_sequence(power_of_two)
		full_seq = ________ + ________
		return full_seq[:n]

def gen_recursive_sequence(base, transform):
	"""
	Creates a function which will produce a recursive sequence similar
	to the Thue-Morse Sequence, except that each element is transformed by
	the provided function to another number (allows for larger ranges of elements).

	Args:
		base: first string in sequence
		transform: function mapping a domain of elements to a range of elements

	Returns:
		a function which will give the specified sequence up to a certain
		number of specified digits
	"""
	def sequence(n):
		"""
		Returns the first n elements of the Thue-Morse
		Sequnce through recursive calls.
		LINK: https://en.wikipedia.org/wiki/Thue–Morse_sequence
		HINT: str.join(list) might come in handy here!

		Args:
			n: positive integer
		"""
		assert n > 0 and isinstance(n, int)
		# base case
		if ________:
			return base[:n]
		else:
			"""
				power_of_two (p_o_2) is the largest power of two less than n
				p_o_2 examples:
				n == 4 --> p_o_2 = 2
				n == 5 --> p_o_2 = 4
				n == 7 --> p_o_2 = 4
				n == 8 --> p_o_2 = 4
				n == 9 --> p_o_2 = 8
			"""
			power_of_two = ________
			seq = thue_morse_sequence(power_of_two)
			full_seq = ________ + ________
			return full_seq[:n]
	return sequence

# Reproduces the Thue-Morse Sequence by passing in the proper base and
# transform function into gen_recursive_sequence
thue_morse_sequence_2 = gen_recursive_sequence(________, lambda x: str(________))

# Produces a recursive sequence similar to the T-M sequence except that we can
# use '0', '1' & '2' as sequence elements and in place of bit flipping as our
# transform function, we add one to the input number and modulo it so it remains
# in the range of {0, 1, 2}.
modulo_3_seq = general_recursive_sequence('0', lambda x: str(________))

# Produces a recursive sequence similar to the T-M sequence except that we can
# use '0', '1', '2' & '3' as sequence elements and in place of bit flipping as our
# transform function, we add two to the input number and modulo it so it remains
# in the range of {0, 1, 2, 3}.
modulo_4_skip_2_seq = general_recursive_sequence('0', lambda x: str(________))
