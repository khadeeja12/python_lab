a= int(input("enter number1:"))
b=int(input("enter number2:"))
o=input("enter the operator:")

if o=='+':
    r=a+b
elif o=='-':
    r=a-b
elif o=='*':
    r=a*b
elif o=='/':
   if b==0 :
      print("not possible")
   r=a/b

print(r)
   
