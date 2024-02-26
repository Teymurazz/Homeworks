"""
Note. All tasks should be written as in the following example (you can
use variable naming method or adding a comment after the expression):
# A
expression = True and False or True
step_one = (True and False) or (True)
step_two = (False) or (True)
step_three = True
print(step_three == expression)

At the end, your program should only print 'True's, so that will mean
you have accomplished and simplified all expressions correctly.

- Booleans -
Simplify these expressions:
A. True or False and True

expression = True or False and True
step_one = True or False
step_two = True
print(step_two == expression)

B. False and False or False

expression = False and False or False
step_one = False and False
step_two = False
print(step_two == expression)

C. (True or False) and True

expression = (True or False) and True
step_one = True and True
step_two = True
print(step_two == expression)

D. True or (True or False and True) and True
expression = True or (True or False and True) and True
step_one = True or (True or False) and True
step_two = True or True and True
step_three = True and True
step_four = True
print(step_four == expression)

E. False or False and False and not False
expression = False or False and False and not False
step_one = False or False and False and True
step_two = False or False and False
step_three = False and False
step_four = False
print(step_four == expression)

F. (True or True or False) and True

expression = (True or True or False) and True
step_one = (True or True) and True
step_two = True and True
step_three = True
print(step_three == expression)

G. False or (True and False)

expression = False or (True and False)
step_one = False or False
step_two = False
print(step_two == expression)

H. False and False and False and False and False or True and False

expression = False and False and False and False and False or True and False
step_one = False and False and False and False and False or False
step_two = False or False
step_three = False
print(step_three == expression)

I. True or False or True

expression = True or False or True
step_one = True or True
step_two = True
print(step_two == expression)

J. False or (not False)

expression = False or (not False)
step_one = False or True
step_two = True
print(step_two == expression)


K. not True or not False

expression = not True or not False
step_one = False or True
step_two = True
print(step_two == expression)

L. False and not False or not False

expression = False and not False or not False
step_one = False and not False or True
step_two = False and True or True
step_three = False or True
step_four = True
print(step_four == expression)

M. True or not False and True or not not True

expression = True or not False and True or not not True
step_one = True or not False and True or not False
step_two = True or not False and True or True
step_three = True or not False and True
step_four = True or True and True
step_five = True or True
step_six = True
print(step_six == expression)

N. not not not False

expression = not not not False
step_one = not not True
step_two = not False
step_three = True
print(step_three == expression)

O. not N (previous task N's value)
expression = not not not not False
step_one = not not not True
step_two = not not False
step_three = not True
step_four = False
print(step_four == expression)

P. True or False and not True or (not True and False) and not True or False

expression = True or False and not True or (not True and False) and not True or False
step_one = True or False and not True or (False and False) and False or False
step_two = True or False and False or False and False or False
step_three = True or False and False
step_four = True or False
step_five = True
print(step_five == expression)

Q. True or not False or not True or True

expression = True or not False or not True or True
step_one = True or not False or False or True
step_two = True or True or False or True
step_three = True or True or True
step_four = True
print(step_four == expression)

R. False and (not True or False or (False or not True and True or False)) and True

expression = False and (not True or False or (False or not True and True or False)) and True
step_one = False and (False or False or (False or False and True or False)) and True
step_two = False and (False or False or (False or False or False)) and True
step_three = False and (False or False or False) and True
stpe_four = False and False and True
step_five = False and False
step_six = False
print(step_six == expression)

S. False and not not not True and (False or True or not False) and True or False

expression = False and not not not True and (False or True or not False) and True or False
step_one = False and not not False and (False or True or True) and True 
step_two = False and not True and (True or True) and True
step_three = False and False and True and True
step_four = False and True and True
step_five = False and True
step_six = False
print(step_six == expression)

T. not (True or False) or not False or (True and False or False)

expression = not (True or False) or not False or (True and False or False)
step_one = not True or True or (True and False)
step_two = False or True or False
step_three = False or True
step_four = True
print(step_four == expression)

U. (True or not not False) and (True or (True or (False)))

expression = (True or not not False) and (True or (True or (False)))
step_one = (True or not True) and (True or True)
step_two = (True or False) and True
step_three = True and True
step_four = True
print(step_four == expression)

V. False and False or (not False and (not False))

expression = False and False or (not False and (not False))
step_one = False and False or (True and True)
step_two = False and False or True
step_three = False or True
step_four = True
print(step_four == expression)

W. (not True or not False) and (not True or (not False))

expression = (not True or not False) and (not True or (not False))
step_one = (False or True) and (False or True)
step_two = True and True
step_three = True
print(step_three == expression)

X. False or False and not True or not False and (not True and False)

expression = False or False and not True or not False and (not True and False)
step_one = False or False and False or True and (False and False)
step_two = False or False and False or True and False
step_three = False or False and False or False
step_four = False or False
step_five = False
print(step_five == expression)

Y. True and True and True and True and not True and True and True or False

expression = True and True and True and True and not True and True and True or False
step_one = True and True and True and True and False and True and True or False
step_two = True and True and True and True and False and True or False
step_three = True and True and True and True and False or False
step_four = True and True and True and False or False
step_five = True and True and False or False
step_six = True and False or False
step_seven = False and False
step_eight = False
print(step_eight == expression)

Z. False and False and (True or not False and (True or False and True)) or not True and False and (not False or not True)

expression = False and False and (True or not False and (True or False and True)) or not True and False and (not False or not True)
step_one = False and False and (True or True and (True and True)) or False and False and (True or False)
step_two = False and False and (True or True and True or False and False and True)
step_three = False and False and (True or False and False)
step_four = False and False and (True and False)
step_five = False and False and False
step_six = False
print(step_six == expression)

"""