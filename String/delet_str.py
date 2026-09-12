"""
delete string using 'del'
"""
str = "hello"
print(str)
del str
print(str)

print("======")

"""
update the string
"""
str1 = "hello"
str2 = "H" + str1[1:]
str3 = str1.replace("ello", "ELLO") # hELLO
str4 = str2.replace("ello", "ELLO") # HELLO
print(str1)
print(str2)
print(str3)
print(str4)