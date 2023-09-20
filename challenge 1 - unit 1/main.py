year=int(input("enter the year to be checked:"))
if(year%400==0):
  print("%d is a leaf year"%year)
elif(year%100==0):
  print("%d is not the leaf year"%year)
elif(year % 4 ==0):
  print("%d is a leaf year"%year)
else:
  print("%d is not the leaf year"%year)