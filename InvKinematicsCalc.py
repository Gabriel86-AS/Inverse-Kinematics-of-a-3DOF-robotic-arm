## this is a python script to calculate the inverse kinematics of a 3-DOF robotic arm
##import libaries
import numpy as np
import matplotlib.pyplot as pyplot
##Definir parametros (L1, L2, L3)
L1 = 0
L2 = 15
L3 = 15
##Definir coordenadas del objetivo(x, y, z)
x = 15
y = 0
z = 0
##definir r k y q
k = np.sqrt(x**2 + y**2) 
q = z - L1
r = np.sqrt(x**2 + y**2 + q**2)
##valores por defecto de los angulos
theta1 = 0
theta2 = 0
theta3 = 0
##Verificar si objetivo esta dentro del alcance del robot
if(r < L2 + L3):
    
     ## Calcular angulos
     theta1 = np.atan2(y,x)

     alpha = np.atan2(q,k)
     beta = np.acos((L2**2 + r**2 - L3**2 )/(2*r*L2))
     theta2 = alpha + beta
     theta3 = np.pi -np.acos((L2**2 + L3**2 - r**2)/(2*L2*L3))
     
     ##convertir los angulos a grados de 0 a 180

     ##checar limites fisicos

     ##graficar la solucion con matplotlib
     #pasar al grados al robot    

else:   
    print("Objetivo fuera del alcance")

