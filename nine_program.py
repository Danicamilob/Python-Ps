from traceback import print_stack


def diHola():
    print('Hello!!')

diHola() #llama la funcion diHola con sus argumentos


def holaConNombre(name):
    print('Hola ' + name)
holaConNombre('Daniel')    

def multiplica(val1 , val2):
    res= val1*val2;
    print(res)
    #return res;
    
multiplica(2,5)  

def multiplicaPorCinco(num):
    res = num*5;
    print(f'{num} *5 = {res}')

print('comienzo del programa')
multiplicaPorCinco(6);
print('siguiente ');
multiplicaPorCinco(3);
print('fin!!');

def suma (n1, n2):
    return n1 + n2;
result = suma(2,8)
print(result)    




