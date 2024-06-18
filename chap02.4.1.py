def sqrt(x):
    res=x**(1/2)
    return res

print(sqrt(4))#2.0

print(sqrt(9))#3.0



def multiply(x, y):
    res=x**y
    return res

print(multiply(x=3, y=4))#81

print(multiply(5, 2))#25


def divide(x, n=2):
    res=x/n
    return res

print(divide(3))#1.5

print(divide(6, 3))#2.0


#lambda function

divide_lam=lambda x, n: x/n

print(divide_lam(6, 3))#2.0