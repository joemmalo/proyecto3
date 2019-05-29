#-*- coding: utf-8 -*-
import math

#Las curvas con las que trabajaremos son de la forma: y² = x³ + Ax + B
#Un punto P consistirá de los atributos x1 y y1

p = 31 #modulo
A = 2
B = 7

#La siguiente función recibe dos puntos y aplicará los 4 casos para realizar la suma entre ellos
#Un punto al infinito se representa utilizando las biblioteca math.inf
#La función devuelve -1 cuando algún inverso no exista dentro del grupo

def sumaPuntos(x1,y1,x2,y2):
	if(x1 != x2):
		b, i = inverso((x2-x1),p) #la función inverso devuelve una bandera y el inverso 
		if (b == 1):	#si existe el inverso, continuamos
			m = ((y2 - y1) * i	) % p 	#pendiente
			x3 = (pow(m,2) - x1 - x2) % p
			y3 = ((m(x1 - x3)) - y1) % p 
			return x3,y3	#de
		else:
			return -1, i 	#no se pudo calcular la pendiente porque el inverso no existe

	if((x1 == x2) and (y1 != y2)):
		return math.inf, math.inf 	#devolvemos el punto al infinito

	if(x1 == x2 and y1 != 0):
		b, i = inverso((2*y1),p) #la función inverso devuelve una bandera y el inverso 
		if (b == 1):	#si existe el inverso, continuamos
			m = (((3*pow(x1,2)) + A) * i) % p 	#pendiente
			x3 = (pow(m,2) - (2*x1)) % p
			y3 = ((m*(x1 - x3)) - y1) % p 
			return x3,y3	
		else:
			return -1, i 	#no se pudo calcular la pendiente porque el inverso no existe

	if(x1 == x2 and y1 == 0):
		return -1,-1	#Devolvemos el punto al infinito

	if(x1==-1 and y1==-1): 	#caso: infinito + P = P
		return x2,y2

	if(x2==-1 and y2==-1):  	#caso: P + infinito = P
		return x1,y1


#Función inverso, devuelve dos valores:
#Un indicador (1 ó -1) que avisa si fué posible obtener el inverso
#El inverso obtenido o en su defecto el número 'n' que se recibió como parámetro
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
		print("El inverso no existe")
		return -1, n 	#No existe el inverso

#La siguiente función multiplica un escalar k por un punto P = (x1,y1

def multiplicaPunto(k,x1,y1):


if __name__ == '__main__':

	print("\nPruebas\n")
	print(sumaPuntos(28,6,28,6))
	
