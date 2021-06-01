# 3.2 Stack Min: How would you design a stack which, in addition to push and pop, has a function min
# which returns the minimum element? Push, pop and min should all operate in 0(1) time.

# My First thoughts: Keep track of the minimum value as you push the values onto the stack, 
# when you pop a value, off of the stack, re-evaluate the stack and determine what the minimum is.