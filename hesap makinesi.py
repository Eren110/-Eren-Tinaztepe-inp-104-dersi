def add(a,b):
  print(a+b)
def sub(a,b):
  print(a-b)
def mul(a,b):
  print(a*b)
def div(a,b):
  print(a/b)
a=int(input("zahl1="))
b=int(input("zahl2="))
operator=input("operation:")
if operator=="+":
  add(a,b)
elif operator=="-":
  sub(a,b)
elif operator=="*":
  mul(a,b)
elif operator=="/":
  div(a,b)
else:
 print("fehler")
 