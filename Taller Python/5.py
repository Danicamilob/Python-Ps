print('='*30)
print('==========CALCULADORA==========')
print('digite el numero 1 si desea realizar una suma')
print('digite el numero 2 si desea realizar una resta')
print('digite el numero 3 si desea realizar una multiplicacion')
print('digite el numero 4 si desea realizar una division')
print('digite el numero 5 si desea realizar una operacion con exponente ')
print('digite el numero 6 si desea realizar modulo')
numero=int(input('Por favor ingrese el numero de la operacion que quiera realizar: '))

if numero ==1 :
    print('por favor ingrese los dos numero a sumar')
    n1=int(input())
    n2=int(input())

    resul= n1 + n2
    print(f'el resultado es : {resul}')
elif numero ==2:
    print('por favor ingrese los dos numero a restar')
    n1=int(input())
    n2=int(input())

    resul= n1 - n2
    print(f'el resultado es : {resul}')
elif numero ==3:
    print('por favor ingrese los dos numero a multiplicar')
    n1=int(input())
    n2=int(input())

    resul= n1 * n2
    print(f'el resultado es : {resul}')       
elif numero ==4:
    print('por favor ingrese los dos numero a dividir')
    n1=int(input())
    n2=int(input())
    if n2==0:
        print('ERROR!! no se puede dividir entre 0')

    resul= n1 / n2
    print(f'el resultado es : {resul}')
elif numero == 5:
    print('por favor ingrese los dos numeros para calcular la operacion exponencial')
    n1=int(input())
    n2=int(input())  

    resul= n1**n2
    print(f'el resultado es : {resul}')
elif numero ==6:
    print('por favor ingrese los dos numeros para calcular el modulo')
    n1=int(input())
    n2=int(input())  

    resul= n1%n2
    print(f'el resultado es : {resul}')   
    print('este es un cambio como ejemplo para git')



