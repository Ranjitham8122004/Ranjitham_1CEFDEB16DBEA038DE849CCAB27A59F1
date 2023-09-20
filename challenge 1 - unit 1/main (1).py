def factorial(x):
  """this is a reqursie function to find the factorial of an integer"""
  if x==1:
    return 1
  else:
    return(x*factorial(x-1)) 
  num=int(input("enter the numbertofind factorial:"))
  result=factorial(num)
  print("the factorial of",num,"is",
         result)