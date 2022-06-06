import numpy as np
import random as rd
flag = True
flag2 = True
precioN = 78900
precioV = 240000

def calculodescNormal(precioN):
  descuentoN = precioN * 0.15
  totalN = precioN - descuentoN
  return totalN

def calculodescVip(precioV):
  descuentoV = precioV * 0.15
  totalV = precioV - descuentoV
  return totalV

Normales = [[1,2,3],
            [4,5,6],
            [7,8,9],
            [10,11,12],
            [13,14,15],
            [16,17,18],
            [19,20,21],
            [22,23,24],
            [25,26,27],
            [28,29,30]]

ladoA = np.array(Normales)

vip = [[31,32,33],
       [34,35,36],
       [37,38,39],
       [40,41,42]]


ladoB = np.array(vip)
asiento_ocupado = False

def calculoPosicion(n_asiento):
  if n_asiento == 1:
    if Normales[0][0] == 'X':
      return True
    else:
      return False

  if n_asiento == 2:
    if Normales[0][1] == 'X':
      return True
    else:
      return False

  if n_asiento == 3:
    if Normales[0][2] == 'X':
      return True
    else:
      return False

  if n_asiento == 4:
    if Normales[1][0] == 'X':
      return True
    else:
      return False

  if n_asiento == 5:
    if Normales[1][1] == 'X':
      return True
    else:
      return False


while flag:
  print('')
  print("\t\tMENU AEREOLINEAS DUOC")
  print("*"*50)
  print("1.-Ver asientos disponibles\n2.-Comprar asientos\n3.-Anular vuelo\n4.-Modificar datos de pasajeros\n5.-Salir")
  print("*"*50)
  opcionM = int(input("\t\tIngrese una opcion: "))
  print("\n")
  print("\t\tPRECIOS\nAsiento normal:\t\t$78.900\nAsiento VIP:\t\t$240.000")


  if opcionM == 1:
        print("\n")
        print("\t\t\tAsientos")
        print("-"*52)
        print("| 1\t2\t3\t\t4\t5\t6  |\n| 7\t8\t9\t\t10\t11\t12 |\n| 13\t14\t15\t\t16\t17\t18 |\n| 19\t20\t21\t\t22\t23\t24 |\n| 25\t26\t27\t\t28\t29\t30 |")
        print("-"*19, "\t\t", "-"*19)
        print("| 31\t32\t33\t\t34\t35\t36 |\n| 37\t38\t39\t\t40\t41\t42 |")
        print("-"*52)
        print("\t\tAsientos disponibles")
        print("TIPO NORMAL:")
        print(ladoA)
        print("-"*10)
        print("TIPO VIP:")
        print(ladoB)

        volver = input("Desea volver al MENU principal?(si/no)").lower().strip()
        if volver == "si":
            print("")
            flag = True
        else:
          if volver == "no":
              print("")
              flag = False

  if opcionM == 2:
    while flag2:
      print("\t\tMENU COMPRAR ASIENTOS ")
      nombrePasajero = input("Ingrese su nombre:\t").upper()
      rutPasajero = int(input("Ingrese su rut sin digito verificador:\t\t"))
      if rutPasajero > 5000000 and rutPasajero < 99999999:
        telefonoPasajero = int(input("Ingrese su N° celular(9 digitos):\t"))
        if telefonoPasajero > 0 and telefonoPasajero < 999999999:
            bancoPasajero = input("Ingrese nombre de su banco:\t").upper()

            print("ASIENTOS DISPONIBLES TIPO NORMAL")
            print('')
            for i in Normales:
                  print(i)
                  print("-"*12)
            print("ASIENTOS DISPONIBLES TIPO VIP")
            print('')
            for l in vip:
              print(l)
              print("-"*12)

            numeroAsiento = int(input("Ingrese el numero del asiento que desea comprar:\t"))
            calculoPosicion(numeroAsiento)
            while calculoPosicion(numeroAsiento) == True:
              print('Asiento N°:', numeroAsiento, ' Ocupado!!')
              numeroAsiento = int(input("Ingrese el numero del asiento que desea comprar:\t"))
              calculoPosicion(numeroAsiento)

            if numeroAsiento >= 0 and numeroAsiento < 31:
                print("Su asiento es de clase Normal")

                for fila in Normales:
                  for asiento in fila:
                    if asiento == numeroAsiento:
                        ind_asiento = fila.index(asiento)
                        fila[ind_asiento] = "X"

            if numeroAsiento >= 31 and numeroAsiento <= 42:
              print("Su asiento es de clase VIP")
            else:
              print("Solo puede escoger asientos del 1 al 42")

        else:
          print("Numero de celular no valido")
          volver = input("Desea volver al MENU de compra?(si/no)").lower().strip()
          if volver == "si":
              print("")
              flag2 = True
          else:
            if volver == "no":
                print("")
                flag2 = False

      else:
        print("rut no valido")
        volver = input("Desea volver al MENU de compra?(si/no)").lower().strip()
        if volver == "si":
            print("")
            flag2 = True
        else:
          if volver == "no":
              print("")
              flag2 = False

  if opcionM == 3:
      print("")

  if opcionM == 4:
      print("")

print("Hasta pronto")
