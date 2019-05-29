#-*- coding: utf-8 -*-
import math
import sys
from random import randint, uniform,random


"""
La siguiente función generauna curva aleatoria que siempre contenga al punto (1,1)
Es decir, el punto inicial siempre será (1,1) esto siempre se cumplirá porque la curva será del tipo y²=x³+Ax-A

Parámetros: un entero que indica el módulo de la curva
"""
def obtenerCurva(mod):
	A = randint(1,100) # valor lineal de la curva (Ax)
	B = (-A  % mod) #valor constante de la curva (-A)	
	return A,B


"""La siguiente función recibe dos puntos y un módulo p
Aplicará los 4 casos para realizar la suma entre dos puntos

Un punto al infinito se representa utilizando las biblioteca math.inf
La función devuelve -1 cuando algún inverso no exista dentro del grupo
"""

def sumaPuntos(x1,y1,x2,y2,p):
	#Generamos una curva aleatoria
	A,B = obtenerCurva(p)

	if(x1 != x2):
		b, i = inverso((x2-x1)%p , p) #la función inverso devuelve una bandera y el inverso 
		if (b == 1):	#si existe el inverso, continuamos
			m = ((y2 - y1) * i	) % p 	# pendiente de la curva
			x3 = (pow(m,2) - x1 - x2) % p
			y3 = ((m * (x1 - x3)) - y1) % p 
			return x3,y3	#devolvemos el resultado de la suma
		else:
			#no se pudo calcular la pendiente porque el inverso no existe
			return -1, i 	#Devolvemos la bandera -1 y el número que no tiene inverso 

	if((x1 == x2) and (y1 != y2)):
		return math.inf, math.inf 	#devolvemos el punto al infinito

	if(x1 == x2 and y1 != 0):
		b, i = inverso((2*y1)%p , p) #la función inverso devuelve una bandera y el inverso 
		if (b == 1):	#si existe el inverso, continuamos
			m = (((3*pow(x1,2)) + A) * i) % p 	#pendiente
			x3 = (pow(m,2) - (2*x1)) % p
			y3 = ((m*(x1 - x3)) - y1) % p 
			return x3,y3	
		else:
			#no se pudo calcular la pendiente porque el inverso no existe 
			return -1, i 	#Devolvemos la bandera -1 y el número que no tiene inverso 

	if(x1 == x2 and y1 == 0):
		return math.inf, math.inf 	#Devolvemos el punto al infinito

	if(x1== math.inf and y1== math.inf): 	#caso: infinito + P = P
		return x2,y2

	if(x2== math.inf and y2== math.inf):  	#caso: P + infinito = P
		return x1,y1


#Función inverso, devuelve dos valores:
#Devuelve un indicador (1 ó -1) que avisa si fué posible obtener el inverso
#DEvuleve también el inverso obtenido o en su defecto el número 'n' que se recibió como parámetro
def inverso(n,m):
	r = m%n
	x = n
	y = r
	c1 = 1
	c2 = -(m//n)
	t1 = 0
	t2 = 1
	c=0
	while(r!=0):
		c = x//y
		r = x%y

		c1 *= -c
		c2 *= -c

		c1 += t1
		c2 += t2

		t1 = -(c1-t1)//c
		t2 = -(c2-t2)//c
		x=y
		y=r
	if(x==1):
		if (t2<0):
			return 1, t2+m #Si existe el inverso
		else:
			return 1, t2 	#Si existe el inverso
	else:
		return -1, n 	#No existe el inverso, devolvemos la bandera -1 y la n que recibimos como parámetro

"""
Implementción el algoritmo de Lenstra
Parámetros: n, el número a factorizar
			B, un entero que servirá para calcular (B!)P, B indica el número de iteraciónes

Salida: Un factor de n o un mensaje "No se pudo factorizar..."

Paso 1: Elegir una curva eliptica y un punto inicial que esté en la curva
(En nuestro caso el punto inicial siempre será (1,1) esto siempre se cumplirá porque la curva será del tipo y²=x³+Ax-A)
paso 2: Elegir un entero aleatorio B (de preferencia un entero muy grande) y calcular B*P
Paso 3: Si el paso 2 falla, significa que no existe alguna pendiente (mod n) y que por lo tanto hemos
		encontrado un factor de n
Paso 4: Si el paso 2 se puede completar, significa que no se pudo factorizar n y es necesario elegir otra curva y empezar
		 de nuevo desde el paso 1

"""
def lenstra(n,B):
	#Definimos nuestro punto inicial P = (1,1)
	p = 1,1 #x1 = 1, y1 = 1

	#Punto Q
	q = p[0],p[1]	#x3 = x1, y3 = y1

	#Intentamos Calculamos B*P
	for x in range(2,B):
		q = sumaPuntos(q[0],q[1],p[0],p[1],n)
		if(q[0] == -1):	#La pendiente no se pudo calcular, significa que podemos obtener un factor
			m = math.gcd(q[1],n)
			print("Encontré el factor ",m,"\n")
			return m 	#devolvemos el factor

		if(q[0] == (math.inf)):
			#rompemos el ciclo for
			break
	print("No se pudo factorizar ",n," Cambia la curva e intenta de nuevo")
	return 0
	



"""
Para ejecutar el programa se deben pasar como parámetros el número que se desea factorizar y el 
número de veces que queremos sumar al punto P (número de iteraciónes)

Ya que las curvas se generan aleatoriamente, puede que se requiera más de una ejecución para encontrar la factorización
de un número, esto es, si se obtiene el mensaje "Argumentos invalidos, ingresa el número a factorizar y una cota de suma" se recomienda
ejecutar el programa al menos 5 veces para obtener la factorización.

Ejemplo de ejecución: python3 Lenstra.py 4453 20
Significa que queremos factorizar el número 4453 y sumar 20 veces el punto P

"""

#----------INTRUCCIÓNES DEL MAIN-------------

if(len(sys.argv)== 3):
	n = int(sys.argv[1]) #número a factorizar
	B = int(sys.argv[2]) #Número de veces que se va a sumar el punto P
	

	print("______________________________\n",
		 "|Criptografía y Seguridad     |\n",
		 "|Proyecto 03                  |\n",
		 "|Guerrero Chávez Diana Lucía  |\n",
		 "|Jovanni Emir Martínez Lorenzo|\n",
		 "|_____________________________|\n")


	factor1 = lenstra(n,B)
	if(factor1 != 0):	#si se encontró un factor
		factor2 = int(n/factor1) #Calculamos el factor 2 mediante esta división
		print("∴ Los factores de ",n," son:\t",factor1 ,",",factor2)
		
	
else:	#No se pudo factorizar n con la curva actual, (se sugiere correr de nuevo el programa)
	print ("Argumentos invalidos, ingresa el número a factorizar y una cota de suma")	
