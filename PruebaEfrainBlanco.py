#Prueba tecnica Efrain Blanco   
#########################################################################################################
#Solicitar nombres de jugadores

#Validar que usuario escriba nombre de jugador 1
a=0
while a!=1:
  jugador1=input("Escribe el nombre del jugador 1: ").lower()
  
  if jugador1 =="":
    print(" ")
    print(" Escribe un nombre por favor")

  else:
    a=1
  
  
#Validar que usuario escriba nombre de jugador 2
b=0
while b!=1:
  jugador2=input("Escribe el nombre del jugador 2: ").lower()
  
  if jugador2 =="":
    print(" ")
    print(" Escribe un nombre por favor")

  else:
    b=1



#################################################################################

#iniciar variables
a1=0
auxn=0
nombre_aux=False   
auxi=0
auxo=0
puntaje1=0
puntaje2=0
marcador1=0
marcador2=0
juegos1=0
juegos2=0
ventaja1=0
ventaja2=0
ventajasets1=0
ventajasets2=0
sets1=0
sets2=0
#Iniciar juego
#while 1 (Iniciar juego)
while a1!=1:
  historial_de_puntajes=[]
  print(" ")
  iniciar=input("¿Desea iniciar el juego? si/no: ").lower()
  #if 1 (De iniciar juego)
  if iniciar=="si":
    print(" ")
    #Mostrar nombres de jugadores
    print("Jugador #1: ",jugador1)
    print("Jugador #2: ",jugador2)
    print(" ")

    #Funcion 1 para validar que nombre es correcto
    def validar_nombre(nombre):
      auxi=0
      if nombre==jugador1:
        auxi=1
        print(" ")
          
      elif nombre==jugador2:
        auxi=2
        print(" ")
      else:
        auxi=0
        print("nombre incorrecto")
        
      return auxi
      
    #codigo de funcion 1
    print("------------------- ")  
    #Preguntar jugador ganador del punto
    while auxo!=1:
      puntaje=input("¿Ganador del punto?: ")
      auxi= validar_nombre(puntaje)
      #Añadir puntos  jugador 1
      if auxi==1:
        print("Punto para ",jugador1, " +1")
        puntaje1+=1
        if puntaje1==1: #15 puntos
          marcador1=15
        elif puntaje1==2: #30 puntos
          marcador1=marcador1+15
        elif puntaje1==3: #40 puntos
          marcador1=marcador1+10

      #ganar juego sin empate ni ventaja
      if puntaje1==4 and puntaje2<=2:
        juegos1+=1
        print("El ganador del juego es ",jugador1)
        historial_de_puntajes.append((marcador1,marcador2))
        puntaje1=0
        puntaje2=0
        marcador1=0
        marcador2=0
        
      #separador de codigo
      
      
      #ganar juego con empates y ventajas
      if (puntaje1-puntaje2)==1 and puntaje1>=4:
        ventaja1+=1
        print("******",ventaja1," ventaja para ",jugador1," *******")
        if ventaja2==1:
          ventaja1=0
          ventaja2=0
          puntaje1=3
          puntaje2=3
      elif (puntaje1==puntaje2) and puntaje1>=4:
        ventaja2=0
        print("Jugador #2 ",jugador2," pierde ventaja")
      elif puntaje2 >=3 and (puntaje1-puntaje2)==2:
        juegos1+=1
        print("El ganador del juego es ",jugador1)
        historial_de_puntajes.append((marcador1,marcador2))
        puntaje1=0
        puntaje2=0
        marcador1=0
        marcador2=0
        ventaja1=0
        ventaja2=0
        
      #Añadir puntos a jugador 2  
      elif auxi==2:
        print("Punto para ",jugador2, " +1")
        puntaje2+=1
        if puntaje2==1: #15 puntos
          marcador2=15
        elif puntaje2==2: #30 puntos
          marcador2=marcador2+15
        elif puntaje2==3: #40 puntos
          marcador2=marcador2+10
          
      #ganar juego sin empate ni ventaja
      if puntaje2==4 and puntaje1<=2:
          juegos2+=1
          print("El ganador del juego es ",jugador2)
          historial_de_puntajes.append((marcador1,marcador2))
          puntaje1=0
          puntaje2=0
          marcador1=0
          marcador2=0
          
        
      #ganar juego con empates y ventajas
      #ganar juego con empates y ventajas
      if puntaje2>1 and (puntaje2-puntaje1)==1:
        ventaja2+=1
        print("******",ventaja2," ventaja para ",jugador2," *******")
        if ventaja1==1:
          ventaja1=0
          ventaja2=0
          puntaje1=3
          puntaje2=3
      elif (puntaje2==puntaje1) and puntaje2>=4:
        ventaja1=0
        print("Jugador #1 ",jugador1," pierde ventaja")
      elif puntaje1>=3 and (puntaje2-puntaje1)==2:
        juegos2+=1
        print("El ganador del juego es ",jugador2)
        historial_de_puntajes.append((marcador1,marcador2))
        puntaje1=0
        puntaje2=0
        marcador1=0
        marcador2=0 
        ventaja1=0
        ventaja2=0
      #Imprimir resultados
      print("Marcador actual #1 ",jugador1, " es [",marcador1, "] puntos") 
      print("Juegos ganados #1 ", jugador1, " [",juegos1,"] ")
      print("Sets ",sets1)
      print("----------------------------------")
      print("Marcador actual #2 ",jugador2, " es [",marcador2, "] puntos") 
      print("Juegos ganados #2 ", jugador2, " [",juegos2,"] ")
      print("Sets ",sets2)
      print(" ")

      if juegos1==7:
        print("El ganador de este set actual es: ",jugador1, " con ",juegos1, " juegos ganados")
        print("El historial de marcadores entre ambos jugadores es: ",historial_de_puntajes)
        sets1+=1
        juegos1=0
      elif juegos2==7:
        print("El ganador de este set actual es: ",jugador2, " con ",juegos2, " juegos ganados")
        print("El historial de marcadores entre ambos jugadores es: ",historial_de_puntajes) 
        sets2+=1
        juegos2=0

      #Ganar partida sin sets con empate o ventaja
      if sets1==3 and (sets1-sets2)>=3:
        print("EL GRAN GANADOR DEL JUEGO DE TENIS ES: ",jugador1, "CON ",sets1," SETS")
        auxo=1
        a1=1
      elif sets1==3 and (sets1-sets2)>=3:
        print("EL GRAN GANADOR DEL JUEGO DE TENIS ES: ",jugador2, " CON ", sets2, " SETS")
        auxo=1
        a1=1
      #ganar partida con empates y ventajas en sets 1
      if (sets1-sets2)==1:
        ventajasets1+=1
        if ventajasets2==1:
          ventajasets1=0
      elif (sets1-sets2)==2:
        print("EL GRAN GANADOR DEL JUEGO DE TENIS ES: ",jugador1, "CON ",sets1," SETS")
        auxo=1
        a1=1
      #ganar partida con empates y ventajas sets 2  
      if (sets2-sets1)==1:
        ventajasets2+=1
        if ventajasets1==1:
          ventajasets2=0
      elif (sets2-sets1)==2:
        print("EL GRAN GANADOR DEL JUEGO DE TENIS ES: ",jugador2, "CON ",sets2," SETS")
        auxo=1
        a1=1
    a1=1 #finalizar juego total (while 1)
    #codigo if 1
  else:
    print("El juego no fue iniciado, adiós.")
    a1=1 #finalizar juego total (while 1)

    
  
print("Juego terminado :)")  
#while 1 fin

#fin de codigo
