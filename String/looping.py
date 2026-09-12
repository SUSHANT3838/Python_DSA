"""
Looping through string
loop itteret over the string
"""
string = "Welcome to my coding chaanel"
for ch in string:
    print(ch, end=" ")
print()

"""
Strings are immutable
"""
s = "aBCD"
s = "A" + s[1:]
print(s)