#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y==0:
        return "Error"
    else:
        return x/y

print(".....................Calculator by Bhaskar Bajaj.......................")

def calculator():
    while True:
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
    
        choice=int(input("Enter your choice: "))
        if choice==5:
            break
        else:
            
            a=float(input("Enter the first number: "))
            b=float(input("Enter the second number: "))
                
            if choice==1:
                    result=add(a,b)
                    print("The final result of addition is : ",result)
        
            elif choice==2:
                    result=subtract(a,b)
                    print("The final result of subtraction is : ",result)
        
            elif choice==3:
                    result=multiply(a,b)
                    print("The final result of multiplication is : ",result)
                    
            elif choice==4:
                    result=divide(a,b)
                    print("The final result of division is : ",result)
        
            elif choice==5:
                    break
                    
            else:
                    print("Wrong choice")
            
            
calculator()


# In[ ]:




