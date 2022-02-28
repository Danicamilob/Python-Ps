num_1 = int(input('por favor ingrese el numero 1: '))
num_2 = int(input('por favor ingrese el numero 2: '))
num_3 = int(input('por favor ingrese el numero 3: '))

if num_1 > num_2 and num_1 > num_3:
    print(f'el numero {num_1} es el numero mas grande de los tres')
elif num_2 > num_1 and num_2 > num_3:
    print(f'el numero {num_2} es el numero mas grande de los tres')  
else :
    print(f'el numero {num_3} es el numero mas grande de los tres')   