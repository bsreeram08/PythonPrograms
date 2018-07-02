string=raw_input("Enter the String:")
a=len(string)
count = 0 
for i in range(0,a,1):
     if (string[i].isupper()):
          count = count + 1
          print string[i]
print count
