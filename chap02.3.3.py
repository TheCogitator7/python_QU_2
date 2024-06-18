var=[1, 2, 3]

for i in var:
    print(i)#1 2 3
    
    
var=[10, 15, 17, 20]

for i in var:
    if i % 2 == 0:
        print(f'{i}는 짝수입니다.')
    else:
        print(f'{i}는 홀수입니다.')
        
for i in range(5):
    print(i)#0 1 2 3 4
    
    
a=[1, 2, 3]
result=[]

for i in a:
    result.append(i**2)
    
print(result)#[1, 4, 9]

result=[i**2 for i in a]
print(result)#[1, 4, 9]

