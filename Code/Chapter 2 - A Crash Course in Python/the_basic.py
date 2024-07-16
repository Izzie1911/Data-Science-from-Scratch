# module
# arithmetic
from __future__ import division

# python 2.7

# arithmetic
import re

my_regex = re.compile("[0-9]+", re.I)
# module

# whitespace_formatting
for i in [1, 2, 3, 4, 5]:
    print(i)  # first line in "for i" block
    for j in [1, 2, 3, 4, 5]:
        print(j)  # first line in "for j" block
        print(i + j)  # last line in "for j" block
    print(i)  # last line in "for i" block
print("done looping")

long_winded_computation = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 +
                           13 + 14 + 15 + 16 + 17 + 18 + 19 + 20)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
easier_to_read_list_of_lists = [[1, 2, 3],
                                [4, 5, 6],
                                [7, 8, 9]]

two_plus_three = 2 + \
                 3

for i in [1, 2, 3, 4, 5]:
    # notice the blank line
    print(i)

# whitespace_formatting

# modules
import re

my_regex = re.compile("[0-9]+", re.I)


# modules


# functions
def double(x):
    """this is where you put an optional docstring
    that explains what the function does.
    for example, this function multiplies its input by 2"""
    return x * 2


def apply_to_one(f):
    """calls the function f with 1 as its argument"""
    return f(1)


my_double = double  # refers to the previously defined function
x = apply_to_one(my_double)  # equals 2

y = apply_to_one(lambda x: x + 4)
# equals 5

another_double = lambda x: 2 * x


def another_double(x): return 2 * x


# don't do this
# do this instead

def my_print(message="my default message"):
    print(message)


my_print("hello")
my_print()


# prints 'hello'
# prints 'my default message'

def subtract(a=0, b=0):
    return a - b


subtract(10, 5)  # returns 5
subtract(0, 5)  # returns -5
subtract(b=5)
# same as previous
# functions

# string
single_quoted_string = 'data science'
double_quoted_string = "data science"

tab_string = "\t"
len(tab_string)
# represents the tab character
# is 1

not_tab_string = r"\t"  # represents the characters '\' and 't'
len(not_tab_string)  # is 2

multi_line_string = """This is the first line.
and this is the second line
and this is the third line"""

# string

# Exceptions
try:
    print (0 / 0)
except ZeroDivisionError:
    print ("cannot divide by zero")
# Exceptions

# Lists
integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [ integer_list, heterogeneous_list, [] ]
list_length = len(integer_list) # equals 3
list_sum= sum(integer_list) # equals 6



