# Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values

import string
d = dict(zip(string.ascii_lowercase,range(97,123)))

print(d)
