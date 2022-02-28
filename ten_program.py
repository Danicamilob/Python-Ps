import email


menu = """
Bienvenidos al registro de usuarios, lleno los campos 
que usted prefiera a continuacion seleccionando un numero
del 1 al 3"""
print('========================')
print('----------Menu----------')
print(menu)
opcion = input('digita una opcion entre 1 y 3: ')
if opcion == '1':
    nombre= input('digita tu nombre : ');
    if nombre.isalpha():
        print('tu nombre es {}', format(nombre))
    else :
        print('Has digitado un nombre no valido...');    

elif opcion == '2':
    edad= input('digita tu edad : ');
    if edad.isnumeric():
        print('tu nombre es {}', format(edad))
    else :
        print('Has digitado una edad no valida...'); 
    
elif opcion == '3':
    email= input('digita tu email : ');
    if email.find('@')>=0 and email.find('.')>=0:
        print('tu email es {}', format(email))
    else :
        print('Has digitado un email no valido...'); 
    
else:
    print('debes diguitar un numero entre 1 y 3')
    print('=-='*20)        