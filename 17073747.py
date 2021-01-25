''''
MINI PROJECT SIF2007 NUMERICAL AND COMPUTATIONAL METHODS
Title: Motion With Air Resistance
Date of Submission: 22/January/2021
Name: Hazman Naim Bin Ahsan
Matric Number: 17073747/2
'''
#import necessary libraries
import matplotlib.pyplot as mpl

#ODE functions to describe the motion with air resistance
#Acceleration in X-component
def a1x(v1x):
     return -(k)*(v1x)**2

#Acceleration in Y-component
def a1y(v1y):
     return -(k)*(v1y)**2 - 9.81

print("MOTION WITH AIR RESISTANCE")
print("Credit Author: HAZMAN NAIM BIN AHSAN")

#Motion Parameter
# Density of medium = 1.275kg/m^3  (Air at STP) 
Rho = 1.275
# Drag coefficient = 0.50 (Assuming the object is spherical shape)
D = 0.50
# Radius of the object
R = float(input("The radius of the object (m): "))
# Cross-sectional area of the object
A = (22/7)*R**2
# Mass of object
m = float(input("The mass of the object (kg): "))

# k = (Density of medium*Drag Coefficient*Cross sectional area)/2*mass
k = (Rho*D*A)/(2*m)

#initialisation
v1y = float(input("Initial Vertical Velocity (m/s): ")) #Initial vertical velocity
v1x = float(input("Initial Horizontal Velocity (m/s): ")) #Initial horizontal velocity
y1 = float(input("Initial Height (m): "))   #Initial height
x1 = 0  #Initial horizontal distance (0 by default)
t = 0 #Time

y2i = y1
v1i = v1x
y1i = v1y

#n tells the program how many iterations needed
#The higher the iteration, the higher the accuracy of the trajectory
#The time between the points correspond to the stepsize of the calculation
n = int(input("Number of iteration(s) (Higher is more accurate): "))
h = 1/n

#Iteration
for i in range(0,n):
    v2y = v1y + t*(a1y(v1y))
    y2 = y1 + t*(v1y) + (1/2)*a1y(v1y)*t**2
    v2x = v1x + t*(a1x(v1x))
    x2 = x1 + t*v1x + (1/2)*a1x(v1x)*t**2
    print("------------------------------------------------")
    print("i = "+str(i)+"")
    print("v1y = "+str(v1y)+" m/s")
    print("y2 = "+str(y2)+" m")
    print("v1x = "+str(v1x)+" m/s")
    print("x2 = "+str(x2)+" m")
    if y2 > 0:
        mpl.scatter(x2,y2)
        v1y = v2y
        y1 = y2
        v1x = v2x
        x1 = x2
        t = t + h
    else:
        print("------------------------------------------------")
        print("At ground")
        break

print("------------------------------------------------")

#Basic information of the motion
print("BASIC INFORMATION OF THE MOTION")
print("The number of point(s) is "+str(n)+".")
print("The number of iteration(s), i = "+str(i)+"")
print("The radius of the object is "+str(R)+" m.")
print("The mass of the object is "+str(m)+" kg.")
print("The initial height is "+str(y2i)+" meters.")
print("The initial x-velocity is "+str(v1i)+" m/s.")
print("The initial y-velocity is "+str(y1i)+" m/s.")
print("The distance from the initial position is "+str(x2)+" meters.")
print("------------------------------------------------")
print("END")
print("THANK YOU")
print("Facebook Page: Astronomer Halaman")

#Graphing Settings
mpl.axvline(0,color='Black')
mpl.axhline(0,color='Black')
mpl.xlabel('Horizontal Distance (meter)')
mpl.ylabel('Height (meter)')
mpl.title('Motion with Air Resistance')

mpl.show()
