import numpy as np
import matplotlib.pyplot as plt


#Wczytanie parametrów
k1 = float(input('k1: '))
k2 = float(input('k2: '))
T1 = float(input('T1: '))
T2 = float(input('T2: '))


#Inicjalizacja macierzy modelu stanowego w postaci kanonicznej sterowalnej
A = np.array([[0,1,0],[0,0,1],[-k1*k2/(T1*T2),-k1*k2/T2,-1/T2]])
B = np.array([[0],[0],[1]])
C=np.array([[k1*k2/(T1*T2),k1*k2/T2,0]])

#Krok symulacji
h=10**(-3)

#Inicjalizacja macierzy stanu, macierzy stanu poprzedniego oraz wyjscia
x_t = np.array([[0],[0],[0]])
x_t_d= np.array([[0],[0],[0]])
y_t = []

#Wypelnienienie macierzy wejscia(poki co tylko skok jednostkowy)
u = []
for i in range(10000):
    u.append(1)


#Symulacja oraz calkowanie metodą prostokątów
i=0
t=[]
while i*h<10:
    x_t=x_t_d+h*(A@x_t+B*u[i])
    y_t.append((C@x_t)[0][0])
    x_t_d=x_t
    i+=1
    t.append(i*h)

#Wyswietlenie wykresów
plt.plot(t,y_t)
plt.ylabel('Y(t)')
plt.xlabel('t [s]')
plt.show()

