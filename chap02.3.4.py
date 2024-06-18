number=[1, 2, 3, "4", 5]

#for i in number:
#   print(i**2)#1 4 9 error
    


for i in number:
    try:
        print(i**2)
    except:
        print('Error at: '+i)
        
#1
#4
#9
#Error at: 4
#25
