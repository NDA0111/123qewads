# Basic data types: integer, float, string and boolean
a = 10 # a is an integer
b = 4.5 # b is a float 
c = 'hello' # c is a string
d = True # d is a boolean

e = "10" # e is a string    
f = 'False' # f is a string 

# g = hello # errol, hello is not defined 

g = a + b # g is a float 
# g = a + e # errol cannot have a sum of integer and string 
g = e * 3 # g is a string: hellohellohello


# Integer (number) operator
a = int(input('Enter a: '))
b = int(input('Enter b: '))
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} % {b} = {a % b}')

# string operator: +, *
s1 = 'hello'
s2 = 'world'
msg = s1 + ' ' + s2
print(msg)

line = '$' * 11 # but 11 * '$' is errol
print(line)

# Boolean operator: and, or, not 
a = True 
b = False

print(f'{a} and {b} = {a and b}')
print(f'{a} or {b} = {a or b}')
print(f'not {a} = {not a}')

# align output: left, right or center
s = 'hello'
a = 4
f = 4.5

print(f'|{s:20}|') # string is left-aligned by default
print(f'|{a:20}|') # integer is right-aligned by default 
print(f'|{f:20}|') # float is right-aligned by default

# specific output alignment
print(f'|{s:>20}|') # print s align on the right 
print(f'|{a:<20}|') # print a align on the left
print(f'|{f:^20}|') # print f align on the center