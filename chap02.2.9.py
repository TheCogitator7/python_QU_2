#control statement
x=2
if x > 0:
    print("값이 0보다 큽니다.")
    
y=-1
if y < 0:
    print("값이 0보다 작습니다.")
    
x=-1
if x > 0:
    print("The value is greater than zero")
else:
    print("The value is less than zero")
    
    
x=3
if x >= 10:
    print("The value is greater than 10")
elif x >= 0:
    print("The value is between 0 and less than 10")
else:
    print("The value is negative")
    

x = 7
print('The value is positive' if x >= 0 else 'The value is negative')


#while

num = 1
while num < 5:
    print(num)# 1 2 3 4
    num+=1
    
num=1
while num < 10:
    if num % 2 == 0:
        print(f"{num} 은 짝수입니다.")
    num+=1
    
    
money=1000
while True:
    money=money-100
    print(f'잔액은 {money}입니다.')
    
    if money <= 0:
        break