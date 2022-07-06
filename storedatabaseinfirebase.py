from firebase import firebase
import time
    
    print("Enter your name")
    x=input()
   
d=firebase.FirebaseApplication('https://cpudata-publish-default-rtdb.firebaseio.com/',None)
data= {str(time.time()):x}
result  = d.post('/mydata/',data)
print(result)