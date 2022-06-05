import numpy as np
import random as rd

loteA = [[1,2,3],
         [7,8,9],
         [13,14,15],
         [19,20,21],
         [25,26,27]]

ladoA = np.array(loteA)

loteB = [[4,5,6],
         [10,11,12],
         [16,17,18],
         [22,23,24],
         [28,29,30]]

ladoB = np.array(loteB)

loteC = [[31,32,33],
         [37,38,39]]

ladoC = np.array(loteC)

loteD = [[34,35,36],
         [40,41,42]]

ladoD = np.array(loteD)



print("\t\tMENU AEREOLINEAS DUOC")
print("*"*50)
print("1.-Ver asientos disponibles\n2.-Comprar asientos\n3.-Anular vuelo\n4.-Modificar datos de pasajeros\n5.-Salir")
print("*"*50)
opcionM = int(input("\t\tIngrese una opcion: "))
print("\n")
print("\t\tPRECIOS\nAsiento normal:\t\t$78.900\nAsiento VIP:\t\t$240.000")
while opcionM != 4:
    print("\n")
    print("\t\t\tAsientos")
    print("-"*52)
    print("| 1\t2\t3\t\t4\t5\t6  |\n| 7\t8\t9\t\t10\t11\t12 |\n| 13\t14\t15\t\t16\t17\t18 |\n| 19\t20\t21\t\t22\t23\t24 |\n| 25\t26\t27\t\t28\t29\t30 |")
    print("-"*19, "\t\t", "-"*19)
    print("| 31\t32\t33\t\t34\t35\t36 |\n| 37\t38\t39\t\t40\t41\t42 |")
    print("-"*52)
    

    if opcionM == 1:
        numAsiento = int(input("Ingrese el numero de asiento que desea reservar: "))


        if numAsiento >= 31 and numAsiento <= 42:
            print("Usted ha escogido el tipo de asiento VIP")
            cantAsientoV = int(input("Ingrese cuantos asientos VIP reservara: "))
            if cantAsientoV > 0:
                print("Usted ha reservado", cantAsientoV, "asientos VIP")

        else:
            if numAsiento > 0 and numAsiento <= 30:
                print("Usted ha escogido el tipo de asiento NORMAL")
                cantAsientoN = int(input("Indique cuantos asientos NORMALES reservara: "))
                if cantAsientoN > 0:
                    print("Usted ha reservado", cantAsientoN, "asientos NORMALES")

    if opcionM == 2:
        print("")

    if opcionM == 3:
        print("")

    if opcionM == 4:
        print("")




