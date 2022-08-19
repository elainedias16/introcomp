N = int(input())
P = int(input())
C = str(input())
Q = int(input())


if(C == '+'):
    resultado = P + Q
elif( C == '*'):
    resultado = P * Q



if(resultado > N):
    print("OVERFLOW\n")
else:
    print("OK")





    N = int(input())
     P = int(input()) 
     C = str(input())
      Q = int(input())  
      if(C == "+"):    
         res = P*Q 
         elif(C == "+"):   
              res = P+Q  if(res > N):    
               print("!OVERFLOW")
                else:   
                 print ("OK")