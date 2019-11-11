"""
s_age = input("please input your age :")
age = int(s_age)
assert 20 < age < 80
print("your name is in 20 and 80")

if age :
    print("age is ", age)

"""
def frace(n) :
    if n == 1 :
        return 1
    else :
        return n * frace(n-1)

print(frace(5))

import functools
def fn(x,y):
    return x*y

def frace1(n):
    return functools.reduce(fn,range(1,n+1))

print(frace1(5))