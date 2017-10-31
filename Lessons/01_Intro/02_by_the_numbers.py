# Numbers
print(2 + 2)    # 4
# Notice there are no quotes around them.
# These are called ints, or integers.

# Strings require quotation marks around them,
# either single ('foo') or double ("bar")
# Numbers do not have this requirement

# Some examples of what can be done numerically

print(10 + 5)   # 15
print(10 * 5)   # 50
print(10 - 5)   # 5
print(10 / 5)   # 2.0

# These data types are called integers,
# as they are all whole numbers.
# Notice the last line. The answer is correct, but there's a
# decimal point.

# This is because of a data-type called 'float'
# floats allow more precision in computation.
# All division in Python3 defaults to floating point
# However, you can override this in several ways.

print(int(10 / 3))  # 3
print(10 // 3)      # 3

# In the first example, we explicitly convert the answer (a float)
# into an int, rounding down 3.3333 to 3.
# The second example uses the // operator to implicitly process
# the result the same way.

# Operations can be chained as well
print(1 + 2 + 3 + 4 + 5)    # 15

# Just keep the order of operations in mind
print(1 + 2 * 3 - 4 / 5)        # 6.2
print(((1 + 2) * 3 - 4) / 5)    # 1.0

