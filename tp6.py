#
#1. Escriba una función redondear() que permita redondear un número
#decimal de acuerdo al criterio: Si el número es mayor a 3.50, devolver el
#entero siguiente (en este caso, 4), si no devolver el entero inmediatamente
#anterior(3). 
#numero=round(3.20)
#print(numero)
#3. Usando el módulo datetime, escribe un programa que muestre la fecha
#y hora actuales del sistema
#import datetime
#fecha_actual = datetime.datetime.now()
#print(fecha_actual)
#4. Escriba un programa que devuelva un número par al azar entre 2 y 10
#(pista: para comprobar si se pueden generar todos los números, pruebe
#ejecutar el programa dentro de un ciclo infinito).
#import random
#lo=random.randrange(1,10)
#print(lo)
#5. Bola mágica: La bola mágica (Magic 8 ball) es un popular juguete usado
#para la adivinación o para buscar consejo. Su mecanismo es muy simple:
#ante una pregunta del usuario, la bola responde con una de 8 posibles
#respuestas:
#- Es seguro que sí
#- Las chances son buenas
#- Puedes contar con ello
#- Pregúntame de nuevo más tarde
#- Concéntrate y pregunta de nuevo
#- No veo con claridad, intenta de nuevo
#- Mi respuesta es no
#- Mis fuentes me dicen que no
#Escriba una función en Python para simular la bola mágica.
#timeit.timeit(
 #   
#respuesta=["Es seguro que sí","Las chances son buenas","Puedes contar con ello","Pregúntame de nuevo más tarde"," No veo con claridad, intenta de nuevo","Mi respuesta es no","Mis fuentes me dicen que no"]
#import random
#import timeit
#input("preguntale algo a la bola magica:")
#azar=random.randrange(1,10)
#print(respuesta[azar])
#2. Coloque el módulo del ejercicio anterior dentro de un paquete. En un
#módulo que esté fuera de ese paquete, cree una función de suma de
#decimales que redondee el resultado haciendo uso de la función
#redondear() del paquete recién creado.
#num1=float(input(("dame un numerin:")))
#num2=float(input(("dame otro numerin:")))
#import redondeo
#print(redondeo.redondeo(num1,num2))
#7. (Opcional) Sorteo: Escriba un programa que simule un sorteo donde
#toman uno o más papeles al azar de un pozo para elegir los ganadores.
usuario=int(input("dame un numero del 1 al 100 haber si ganas el sorteo:"))
import random
resultado=random.randrange(1,2)
if (resultado==usuario):
    print("ganaste")
else:
    print("perdiste volve a intentar")