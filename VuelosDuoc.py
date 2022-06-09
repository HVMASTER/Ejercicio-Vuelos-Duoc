import numpy as np

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
  if n_asiento == 6:
    if Normales[1][2] == 'X':
      return True
    else:
      return False

  if n_asiento == 7:
    if Normales[2][0] == 'X':
      return True
    else:
      return False

  if n_asiento == 8:
    if Normales[2][1] == 'X':
      return True
    else:
      return False

  if n_asiento == 9:
    if Normales[2][2] == 'X':
      return True
    else:
      return False

  if n_asiento == 10:
    if Normales[3][0] == 'X':
      return True
    else:
      return False

  if n_asiento == 11:
    if Normales[3][1] == 'X':
      return True
    else:
      return False

  if n_asiento == 12:
    if Normales[3][2] == 'X':
      return True
    else:
      return False

  if n_asiento == 13:
    if Normales[4][0] == 'X':
      return True
    else:
      return False

  if n_asiento == 14:
    if Normales[4][1] == 'X':
      return True
    else:
      return False

  if n_asiento == 15:
    if Normales[4][2] == 'X':
      return True
    else:
      return False

  if n_asiento == 16:
    if Normales[5][0] == 'X':
      return True
    else:
      return False

  if n_asiento == 17:
    if Normales[5][1] == 'X':
      return True
    else:
      return False

  if n_asiento == 18:
    if Normales[5][2] == 'X':
      return True
    else:
      return False

  if n_asiento == 19:
    if Normales[6][0] == 'X':
      return True
    else:
      return False

  if n_asiento == 20:
    if Normales[6][1] == 'X':
      return True
    else:
      return False
  if n_asiento == 21:
    if Normales[6][2] == 'X':
      return True
    else:
      return False

  if n_asiento == 22:
    if Normales[7][0] == 'X':
      return True
    else:
      return False

  if n_asiento == 23:
    if Normales[7][1] == 'X':
      return True
    else:
      return False

  if n_asiento == 24:
    if Normales[7][2] == 'X':
      return True
    else:
      return False

  if n_asiento == 25:
    if Normales[8][0] == 'X':
      return True
    else:
      return False
  if n_asiento == 26:
    if Normales[8][1] == 'X':
      return True
    else:
      return False

  if n_asiento == 27:
    if Normales[8][2] == 'X':
      return True
    else:
      return False

  if n_asiento == 28:
    if Normales[9][0] == 'X':
      return True
    else:
      return False

  if n_asiento == 29:
    if Normales[9][1] == 'X':
      return True
    else:
      return False

  if n_asiento == 30:
    if Normales[9][2] == 'X':
      return True
    else:
      return False

  ### ASIENTOS VIP

  if n_asiento == 31:
    if vip[0][0] == 'X':
      return True
    else:
      return False

  if n_asiento == 32:
    if vip[0][1] == 'X':
      return True
    else:
      return False

  if n_asiento == 33:
    if vip[0][2] == 'X':
      return True
    else:
      return False
  if n_asiento == 34:
    if vip[1][0] == 'X':
      return True
    else:
      return False

  if n_asiento == 35:
    if vip[1][1] == 'X':
      return True
    else:
      return False

  if n_asiento == 36:
    if vip[1][2] == 'X':
      return True
    else:
      return False

  if n_asiento == 37:
    if vip[2][0] == 'X':
      return True
    else:
      return False

  if n_asiento == 38:
    if vip[2][1] == 'X':
      return True
    else:
      return False
  if n_asiento == 39:
    if vip[2][2] == 'X':
      return True
    else:
      return False

  if n_asiento == 40:
    if vip[3][0] == 'X':
      return True
    else:
      return False

  if n_asiento == 41:
    if vip[3][1] == 'X':
      return True
    else:
      return False

  if n_asiento == 42:
    if vip[3][2] == 'X':
      return True
    else:
      return False


def EncuentraPosicion(n_asiento):
  if n_asiento == 1:
    Normales[0][0] = 1
    return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 2:
    Normales[0][1] = 2
    return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 3:
    Normales[0][2] = 3
    return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 4:
   Normales[1][0] = 4
   return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 5:
   Normales[1][1] = 5
   return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 6:
   Normales[1][2] = 6
   return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 7:
   Normales[2][0] = 7
   return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 8:
   Normales[2][1] = 8
   return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 9:
   Normales[2][2] = 9
   return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 10:
   Normales[3][0] = 10
   return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 11:
   Normales[3][1] = 11
   return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 12:
   Normales[3][2] = 12
   return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 13:
   Normales[4][0] = 13
   return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 14:
   Normales[4][1] = 14
   return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 15:
   Normales[4][2] = 15
   return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 16:
   Normales[5][0] = 16
   return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 17:
   Normales[5][1] = 17
   return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 18:
   Normales[5][2] = 18
   return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 19:
   Normales[6][0] = 19
   return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 20:
   Normales[6][1] = 20
   return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 21:
   Normales[6][2] = 21
   return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 22:
   Normales[7][0] = 22
   return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 23:
   Normales[7][1] = 23
   return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 24:
   Normales[7][2] = 24
   return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 25:
   Normales[8][0] = 25
   return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 26:
   Normales[8][1] = 26
   return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 27:
   Normales[8][2] = 27
   return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 28:
   Normales[9][0] = 28
   return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 29:
   Normales[9][1] = 29
   return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 30:
   Normales[9][2] = 30
   return print('Asiento N°', n_asiento, ' Anulado..')

   ### ASIENTOS VIP

  if n_asiento == 31:
   vip[0][0] == 31
   return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 32:
   vip[0][1] == 32
   return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 33:
   vip[0][2] == 33
   return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 34:
   vip[1][0] == 34
   return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 35:
   vip[1][1] == 35
   return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 36:
   vip[1][2] == 36
   return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 37:
   vip[2][0] == 37
   return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 38:
   vip[2][1] == 38
   return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 39:
   vip[2][2] == 39
   return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 40:
   vip[3][0] == 40
   return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 41:
   vip[3][1] == 41
   return print('Asiento N°', n_asiento, ' Anulado..')

  if n_asiento == 42:
   vip[3][2] == 42
   return print('Asiento N°', n_asiento, ' Anulado..')


ladoB = np.array(vip)
asiento_ocupado = False


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
    flag2 = True
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

            if numeroAsiento >= 0 and numeroAsiento < 42:
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

            volver = input("Desea volver al MENU?(si/no)").lower().strip()
            if volver == "si":
                print("")
                flag2 = False
            else:
              if volver == "no":
                  print("")
                  flag2 = True

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
    print('')
    print("Indique el numero del asiento que desea anular: ")
    print('')
    anulacion = int(input("Ingrese el numero de asiento: "))

    if anulacion > 0 and anulacion < 31:
      while calculoPosicion(anulacion) == True:
        EncuentraPosicion(anulacion)
      print('Asiento Disponible.. !No se puede Anular¡ ')

  if opcionM == 4:
      print("")

print("Hasta pronto")
