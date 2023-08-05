
from re import A
from time import sleep, time


print('*******************************')
print('*** Javier Ulises Cedano  ***')
print('*******************************')
print()
print('-----------------------------------------------')
print('-                  GOMERA UC                  -')
print('-    Mantenimiento y respaldo de vehículo     -')
print('-----------------------------------------------')

cliente = input('Ingrese su nombre y apellido:')
nombre_auto = input('Cual es el modelo de su auto?: ')
print(f'Bienvenido a nuestra gomera, veamos en que le podemos ayudar.')
print()
def cuerpo():
    a = ''
    total = 0
    print('\t\t*******************************')
    print('\t\t*** Servicios que ofrecemos ***')
    print('\t\t*******************************')
    print('---------------------------------------------------')
    print('-1.Cambio y equilibrado de neumatico.................500$-')
    print('-2.Desmontar neumaticos..............................250$-')
    print('-3.Montar neumaticos.................................300$-')
    print('-4.Cambio de aceite de motor.........................350$-')
    print('-5.Correcion de pinches en los neumaticos............100$-')
    print('-6.Cambio de valvulas de aire de los neumaticos......200$-')
    print('-7.Correcion de las averias y engrasado de los aros..400$-')
    print('-8.Ventas de aros nuevos y usados...................5,500$ & 4,000$-')
    print('-9.Venta de neumaticos nuevos y usados..............4,500$ & 2,500$-')
    print('-10.Nivelacion y chequeo de presion de aire a los neumaticos...300$-')
    print('---------------------------------------------------')

    opc = int(input('Que servicio se le ofrece? '))
    if opc == 1:  
        total =+ 500
        print('-----------------------------------')
        print('-Cambio y equilibrado de neumatico-')
        a ='-Cambio y equilibrado de neumatico-'
        print('-----------------------------------')
        print('El cambio y equilibro de neumatico van juntos porque estos se complementan.')
        print('El cambio de neumatico vale 250$ y el quilibrio de neumatico 250$')
        print()
        print('Espere un momento, estamos buscando los herramientas adecuadas para su modelo.')
        sleep(2.0)
        print('Cambios realizados.')

    if opc == 2:  
        total =+ 250
        print('-----------------------------------')
        print('-       Desmontar neumaticos      -')
        a = '-       Desmontar neumaticos      -'
        print('-----------------------------------')
        print('Desmontar neumaticos para dar mantenimiento.')
        print()
        print('Espere un momento, estamos buscando las herramientas adecuadas para su modelo.')
        sleep(2.0)
        print('Cambios realizados.')  

    if opc == 3:  
        total =+ 300
        print('------------------------------------')
        print('-          Montar neumaticos       -')
        a = '-          Montar neumaticos       -'
        print('------------------------------------')
        print('Montar neumaticos.')
        print()
        print('Espere un momento, estamos buscando las herramientas adecuadas para su modelo.')
        sleep(2.0)
        print('Cambios realizados.')
    if opc == 4:  
        total =+ 350
        print('-----------------------------------')
        print('-     Cambio de aceite de motor   -')
        a = '-     Cambio de aceite de motor   -'
        print('-----------------------------------')
        print('El cambio de aceite es una parte fundamental para que el coche se mantenga en funcionamiento por mucho tiempo.')
        print()
        print('Espere un momento, estamos buscando las herramientas adecuadas para su modelo.')
        sleep(2.0)
        print('Cambios realizados.')

    if opc == 5:  
        total =+ 100
        print('----------------------------------------------')
        print('-   Correcion de pinches en los neumaticos   -')
        a = '-   Correcion de pinches en los neumaticos   -'
        print('----------------------------------------------')
        print('Tapar pinches de neumaticos.')
        print()
        print('Espere un momento, estamos buscando las herramientas adecuadas.')
        sleep(2.0)
        print('Cambios realizados.')

    
    if opc == 6:  
        total =+ 200
        print('-------------------------------------------------')
        print('-  Cambio de valvulas de aire de los neumaticos -')
        a = '-  Cambio de valvulas de aire de los neumaticos -'
        print('-------------------------------------------------')
        print('Cambio de valvulas de los neumaticos.')
        print()
        print('Espere un momento, estamos buscando las herramientas adecuadas para su modelo.')
        sleep(2.0)
        print('Cambios realizados.')

    if opc == 7:  
        total =+ 400
        print('----------------------------------------------------')
        print('- Correcion de las averias y engrasado de los aros -')
        a = '- Correcion de las averias y engrasado de los aros -'
        print('----------------------------------------------------')
        print('Mantenimiento de aros.')
        print()
        print('Espere un momento, estamos buscando las herramientas adecuadas.')
        sleep(2.0)
        print('Cambios realizados.')

    if opc == 8:  
        print('----------------------------------')
        print('- Ventas de aros nuevos y usados -')
        a = '- Ventas de aros nuevos y usados -'
        print('----------------------------------')
        print('Venta de aros.')
        print('************************')
        print('n.Aros nuevos.....5,500$')
        print('u.Aros usados.....4,000$')
        print('************************')
        opc1 = input('Ingrese la opcion (n/u):')
        if opc1 =='n':
            total =+ 5,500
            aros = 'Aros nuevos'
            print(f'Aros nuevos para {nombre_auto}')
        if opc1 =='u':
            total =+ 4,000
            aros = 'Aros usados'
            print(f'Aros usados para {nombre_auto}')

        print('Compra realizada con exito.')

    if opc == 9:  
        print('---------------------------------------')
        print('- Venta de neumaticos nuevos y usados -')
        a = '- Venta de neumaticos nuevos y usados -'
        print('---------------------------------------')
        print('Venta de neumaticos.')
        print('******************************')
        print('n.Neumaticos nuevos.....4,500$')
        print('u.Neumaticos usados.....2,500$')
        print('******************************')
        opc1 = input('Ingrese la opcion (n/u):')
        if opc1 =='n':
            total =+ 4,500
            neum = 'Neumaticos nuevos'
            print(f'Neumaticos nuevos para {nombre_auto}')
        if opc1 =='u':
            total =+ 2,500
            neum = 'Neumaticos usados'
            print(f'Neumaticos usados para {nombre_auto}')

        print('Compra realizada con exito.')

    if opc == 10:  
        total =+ 300
        print('-----------------------------------------------------------')
        print('- Nivelacion y chequeo de presion de aire a los neumatico -')
        a = '- Nivelacion y chequeo de presion de aire a los neumatico -'
        print('-----------------------------------------------------------')
        print('Mantenimiento de aros.')
        print()
        print('Espere un momento, estamos buscando las herramientas adecuadas para su modelo.')
        sleep(2.0)
        print('Cambios realizados.')
    print('Generando factura.')
    sleep(5.0)

    print('Datos del cliente.')
    print(f'Nombre: {cliente}')
    print(f'Modelo de auto: {nombre_auto}')
    print(f'Cambios realizados: {a}')
    print(f'Total: {total}')

    itbisP = 0.18
    itbis = total * itbisP
    itbisT = itbis - (itbis / (1 + itbisP))  # Calculate itbisT correctly

    print(f'Total del ITBIS: {itbisT}')
    print(f'Total con ITBIS: {itbis}')

cuerpo()

