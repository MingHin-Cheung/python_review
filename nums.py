from math import *

a = 11
b = 30
p = -1.3193
c = b % a
for i in range(5):
    print((a + p) * a)
print(c)  # 30%11 = 30-22 = 8
print(str(a))
a = str(a)

if type(a) == str:
    print("a")

print(b, "abc")
print(str(b) + "abc")
print(abs(p))  # absolute value
print(pow(b, 2))
print(max(c, b))
print(round(p))
print(floor(3.7))
print(ceil(3.7))
print(sqrt(3.4))
