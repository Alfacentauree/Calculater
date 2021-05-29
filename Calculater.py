num = int(input("Enter: "))
op = input("op: ")
num1 = int(input("Enter: "))

def calu(num,num1,op):
    if op == '+':
        print(num + num1)
    elif op == '-':
        print(num-num1)
    elif op == '*':
        print(num*num1) 
    elif op == '/':
        print(num/num1)   
    else:
        print("Invalid Enrty!")              
        

calu(num,num1,op)        


 


    

