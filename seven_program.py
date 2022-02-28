#while
'''a= 0;

while  a<100:
    print(a)
    a += 1 #a = a + 1
    if a>20:
        break
print('el bucle a finalizado')  '''  


b= 0;

while  b<100:  
    b += 1 #a = a + 1
    if b % 2 ==0:
        continue
    print(b)   
print('el bucle a terminado')


for i in range(0,10):
    print(i**2);
    if i == 5:
        break
print('el bucle ha finalizado')    

for i in range(0,10):
    
    if i % 3 == 0:
        continue
    print(i**2);
        
print('el bucle ha finalizado') 


