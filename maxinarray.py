Array=[]
max=0
n=int(input("enter the no of elements in the list"))
for i in range(n):
     i=int(input())
     Array.append(i)
     if (i > max):
          max=i
print max
