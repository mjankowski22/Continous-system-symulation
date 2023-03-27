import numpy as np
import matplotlib.pyplot as plt
import math

# Simulation Step
H = 10**(-3)
A = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
B = np.array([[0], [0], [0]])
C = np.array([[0, 0, 0]])
x_t = np.array([[0], [0], [0]])
x_t_d = np.array([[0], [0], [0]])
y_t = []



#Inicjalizacja macierzy stanu, macierzy stanu poprzedniego oraz wyjscia
def initialize_simulation_arrays():
    global x_t, x_t_d, y_t
    x_t = np.array([[0],[0],[0]])
    x_t_d= np.array([[0],[0],[0]])
    y_t = []

#Inicjalizacja macierzy modelu stanowego w postaci kanonicznej sterowalnej

def initialize_arrays_canon(k1, k2, T1, T2):
    global A, B, C
    A = np.array([[0, 1, 0], [0, 0, 1], [-k1*k2/(T1*T2), -k1*k2/T2, -1/T2]])
    B = np.array([[0], [0], [1]])
    C = np.array([[k1*k2/(T1*T2), k1*k2/T2, 0]])

def initialize_input(type, sim_time, amplitude, period, duty_cycle):
    u = []
    if type == "heaviside_step":
        i = 0
        while i*H < sim_time:
            u.append(amplitude)
            i += 1
        return u

    elif type == "rectangle":
        i = 0
        while i*H < sim_time:
            for a in range(round(period*duty_cycle)):
                if i*H >= sim_time:
                    break
                u.append(amplitude)
                i += 1

            for b in range(round(period*(1-duty_cycle))):
                if i*H >= sim_time:
                    break
                u.append((-1)*amplitude)
                i += 1
        return u

    elif type == "sinus":
        i = 0
        while i * H < sim_time:
            u.append(amplitude*math.sin(math.pi*2*i*H*1000/period))
            i += 1
        return u

def integration_results(x_t, x_t_d, y_t, u, sim_time):
    global A, B
    i = 0
    while i * H < sim_time:
        x_t = x_t_d + H * (A @ x_t + B * u[i])
        y_t.append((C @ x_t)[0][0])
        x_t_d = x_t
        i += 1

    return y_t




def simulation(s_input, sim_time, x_t, x_t_d):
    results_ = {'sinus': [], 'rectangle': [], 'heaviside_step': []}
    inputs_ = {'sinus': [], 'rectangle': [], 'heaviside_step': []}

    for choice in range(3):

        if s_input[choice]['is_active']:
            initialize_simulation_arrays()
            current_input = s_input[choice]['type']
            amplitude = s_input[choice]['amplitude']
            period = s_input[choice]['period']
            duty_cycle = s_input[choice]["duty_cycle"]
            input_ = initialize_input(current_input, sim_time, amplitude, period, duty_cycle)
            results_[s_input[choice]['type']] = integration_results(x_t, x_t_d, y_t, input_, sim_time)
            inputs_[s_input[choice]['type']] = input_
    results(results_, s_input, sim_time, inputs_)

def results(results_, s_input, sim_time, inputs_):
    t = []
    keys=[]
    i = 0
    num_plots = 0
    while H*i < sim_time:
        t.append(i*H)
        i += 1
    for i in results_:
        if results_[i]:
            num_plots += 1
            keys.append(i)



    if num_plots == 1:
        figure,axis = plt.subplots(1,2)
        axis[0].plot(t,inputs_[keys[0]])
        axis[0].set_title(keys[0])
        axis[1].plot(t, results_[keys[0]])
        axis[1].set_title(keys[0]+" output")
        plt.tight_layout()
        plt.show()

    elif num_plots == 2:
        figure, axis = plt.subplots(2, 2)
        
        axis[0,0].plot(t, inputs_[keys[0]])
        axis[0,0].set_title(keys[0])
        axis[0][1].plot(t, results_[keys[0]])
        axis[0,1].set_title(keys[0] + " output")
        axis[1,0].plot(t, inputs_[keys[1]])
        axis[1,0].set_title(keys[1])
        axis[1,1].plot(t, results_[keys[1]])
        axis[1,1].set_title(keys[1] + " output")
        plt.tight_layout()
        plt.show()



    elif num_plots ==3:
        figure, axis = plt.subplots(3, 2)
        axis[0, 0].plot(t, inputs_[keys[0]])
        axis[0, 0].set_title(keys[0])
        axis[0, 1].plot(t, results_[keys[0]])
        axis[0, 1].set_title(keys[0] + " output")
        axis[1, 0].plot(t, inputs_[keys[1]])
        axis[1, 0].set_title(keys[1])
        axis[1, 1].plot(t, results_[keys[1]])
        axis[1, 1].set_title(keys[1] + " output")
        axis[2, 0].plot(t, inputs_[keys[2]])
        axis[2, 0].set_title(keys[2])
        axis[2, 1].plot(t, results_[keys[2]])
        axis[2, 1].set_title(keys[2] + " output")
        plt.tight_layout()
        plt.show()


def algorithm(k1, k2 , T1, T2, b_input, sim_time):
    global x_t,x_t_d
    initialize_arrays_canon(k1, k2, T1, T2)
    simulation(b_input, sim_time, x_t, x_t_d)





