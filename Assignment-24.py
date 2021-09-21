# import library
import re

# make a pattern
pattern = "^[A-Za-z0-9]*$"

# input
string = "Shrawani31"
string1 = "shra_wani"

state = bool(re.match(pattern, string))
state1 = bool(re.match(pattern, string1))

print(state)
print(state1)
