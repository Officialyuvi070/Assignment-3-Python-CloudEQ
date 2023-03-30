# Explain the difference between == and === in python.
# there is no === operator in python. but we discuss
# the difference between in is and ==. In  simply word
# == operator is a value equality. means two objects have same value.
# is operator is a reference equality. means two reference refer to the same object.


a = [34,45,"yuvi"]
b = [34,45,"yuvi"]
print(a is b) # OUTPUT: False
print(a == b) # OUTPUT: True