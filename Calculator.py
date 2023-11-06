num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
print("Enter 1 for Addition")
print("Enter 2 to Subtract")
print("Enter 3 to Multiply")
print("Enter 4 to Divide")
mode=int(input(""))

def Add(num1,num2):
    sum=num1+num2
    print(sum)
def Sub(num1,num2):
    sub=num1-num2
    print(sub)
def Mul(num1,num2):
    mul=num1*num2
    print(mul)
def Div(num1,num2):
    div=num1/num2
    print(div)

if mode==1:
    # sum=num1+num2
    # print(sum)
    Add(num1,num2)
elif mode==2:
    # sub=num1-num2
    # print(sub)
    Sub(num1,num2)
elif mode==3:
    # mul=num1*num2
    # print(mul)
    Mul(num1,num2)
elif mode==4:
    # div=num1/num2
    # print(div)
    Div(num1,num2)
else:
    print("ERROR")
