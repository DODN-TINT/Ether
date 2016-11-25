"""
This is my first python code 3.5.2
ever on pycharm community version and Windows
"""

testvalue = 3.1415926
testvalue *= 4
teststr = "PI"

print("\n")
print("Hello World")
print("The quick brown fox jumps over the lazy dog\n\n",teststr, testvalue, end='  ')
print(testvalue/4)

pi_tuple = (3,1,4,5,9,2,9)
new_list = list(pi_tuple)
new_tuple =  tuple(new_list)

print("\n\n\nlists are printed with square brackets, lists with parentheses")

print("pi tuple", pi_tuple)
print("New Tuple  - ",new_tuple)
print("New List  %s - last entry %s",new_list, new_list[len(new_list)-1])

