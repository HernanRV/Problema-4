def arreglo(n):
    print('Arreglo: ', n)
    cant = len(n)
    n_par = 0
    n_impar = 0
    n_mil = 0
    
    print('\na. Cantidad de elementos: ',cant)
    
    for i in range(len(n)):
        if n[i]%2 == 0:
            n_par += 1
        else:
            n_impar += 1
    print('\nb. Números pares: ', (n_par*100)/cant,'%')
    print('   Números impares: ', (n_impar*100)/cant,'%')
    
    for i in range(len(n)):
        if n[i] > 1000:
            n_mil += 1
    print('\nc. Números mayores a 1000: ', (n_mil*100)/cant,'%')

    n_mayor = max(n)
    n_menor = min(n)
    print('\nd. Valor mayor: ', n_mayor)
    print('   Valor menor: ', n_menor)

    print('\ne. 100%: ', n_mayor)
    n_menor_porc = (n_menor*100)/n_mayor
    print('   Porcentaje del valor mínimo: ', round(n_menor_porc,2),'%')
    n.remove(n_mayor)
    n.remove(n_menor)
    porc_prom = 0
    for i in range(len(n)):
        porc_prom += (n[i]*100)/n_mayor
    print('   Porcentaje promedio números restantes: ', round(porc_prom,2),'%')
