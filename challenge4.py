# Problem 1: Simplify the following expression
a = True
b = False
c = True
# result1 = a and (b or c)
result1 = (a or b) and (a or c)

# Problem 2: Simplify the following expression
x = True
y = False
# result2 = x or (x and y)
result2 = x

# Problem 3: Simplify the following expression
p = False
q = True
# result3 = not (p or q)
result3 = (not p) and (not q)

# Problem 4: Simplify the following expression
m = True
n = False
# result4 = m and not m
result4 = False

# Problem 5: Simplify the following expression
d = True
e = False
# result5 = d or not d
result5 = True

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
