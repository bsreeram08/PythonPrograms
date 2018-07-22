import random
now=int(input())
target=int(input())
nfgame=int(input())
a=[]
score=0
for i in range(0,nfgame):
     x=random.randint(20,500)
     #x=int(input())
     a.append(x)
     print x
for i in range(0,nfgame):     
     a[i]=a[i]%10
     if(a[i]%2!=0):
          a[i]=a[i]+1
     if(a[i]==0 or a[i]==10):
          now=now-1;
     if(a[i]==10 or a[i]==8):
          a[i]=0
     if(now!=0):
          score=score+a[i]
     #print(str(target)+" "+str(score)+" "+str(now))
     if now==0:
          break
if(score>target-1):
     print ("win")
elif(score<target-1):
     print("lose")
else:
     print("draw")
print score
#print(str(now)+" "+str(target)+" "+str(score))
  
