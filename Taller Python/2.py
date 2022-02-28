#compañia nacional las palmeras
print('==============================')
print('Compañia nacional las palmeras')
print('==============================')

nombre= input('Por favor digita tu nombre : ');
clave = input('por favor digita tu clave de departamento: ')
antiguedad = input('Por favor digita tu antiguedad: (años):')

if nombre.isalpha():
    print('tu nombre es: ', format(nombre))
else :
    print('Has digitado un nombre no valido...')

if clave == '1' :
    print('ATENCION: Usted hace parte de atencion al cliente')
    if antiguedad == '1':
        print('usted tiene derecho a 6 dias de vacaciones')
    elif antiguedad >= '2' and antiguedad <= '6':
        print('usted tiene derecho a 14 dias de vacaciones')  
    elif antiguedad >= '7':
        print('usted tiene derechoa a 20 dias de vacaciones')
    else:
        print('usted no ha elejido la opcion correcta')

if clave == '2' :
    print('ATENCION: Usted hace parte de logistica')
    if antiguedad == '1':
        print('usted tiene derecho a 7 dias de vacaciones')
    elif antiguedad >= '2' and antiguedad <= '6':
        print('usted tiene derecho a 15 dias de vacaciones')  
    elif antiguedad >= '7':
        print('usted tiene derechoa a 22 dias de vacaciones')
    else:
        print('usted no ha elejido la opcion correcta')

if clave == '3' :
    print('ATENCION: Usted hace parte de gerencia')
    if antiguedad == '1':
        print('usted tiene derecho a 10 dias de vacaciones')
    elif antiguedad >= '2' and antiguedad <= '6':
        print('usted tiene derecho a 20 dias de vacaciones')  
    elif antiguedad >= '7':
        print('usted tiene derechoa a 30 dias de vacaciones')
    else:
        print('usted no ha elejido la opcion correcta')
            

                  

