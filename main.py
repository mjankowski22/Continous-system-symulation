import tkinter as tk
from algorithm import algorithm



#Simulation function
def simulate():
    global flag
    label17.grid_forget()
    label18.grid_forget()
    label19.grid_forget()
    button2.grid_forget()

    heaveside_active = 0
    sinus_active=0
    rectangle_active=0
    heaveside_amplitude=0
    sinus_amplitude=0
    sinus_period=0
    rectangle_amplitude=0
    rectangle_period =0
    rectangle_duty_cycle =0
    k1=0
    k2=0
    T1=0
    T2=0
    time =0

    if var1.get() ==1 :
        heaveside_active=True
    else: 
        heaveside_active=False

    if var2.get() ==1 :
        sinus_active=True
    else:
        sinus_active = False

    if var3.get() ==1 :
        rectangle_active=True
    else:
        rectangle_active=False

    if not rectangle_active and not sinus_active and not heaveside_active:
        label19.grid(row=7,column=2,columnspan=2)
        return False
    try:
        if text_input1.get("1.0",tk.END) !='\n':
            heaveside_amplitude = float(text_input1.get("1.0",tk.END))
        else:
            heaveside_amplitude=0

        if text_input2.get("1.0",tk.END) !='\n':
            sinus_amplitude = float(text_input2.get("1.0",tk.END))
        else:
            sinus_amplitude=0

        if text_input3.get("1.0",tk.END) !='\n':
            sinus_period = float(text_input3.get("1.0",tk.END))
        else:
            sinus_period=0
        
        if text_input4.get("1.0",tk.END) !='\n':
            rectangle_amplitude = float(text_input4.get("1.0",tk.END))
        else:
            rectangle_amplitude=0
        
        if text_input5.get("1.0",tk.END) !='\n':
            rectangle_period = float(text_input5.get("1.0",tk.END))
        else:
            rectangle_period=0
        
        if text_input7.get("1.0",tk.END) !='\n':
            k1 = float(text_input7.get("1.0",tk.END))
        else:
            k1=0
        
        if text_input8.get("1.0",tk.END) !='\n':
            k2 = float(text_input8.get("1.0",tk.END))
        else:
            k2=0
        
        if text_input9.get("1.0",tk.END) !='\n':
            T1 = float(text_input9.get("1.0",tk.END))
        else:
            T1=0
        
        if text_input10.get("1.0",tk.END) !='\n':
            T2 = float(text_input10.get("1.0",tk.END))
        else:
            T2=0

        if text_input11.get("1.0",tk.END) !='\n':
            time = float(text_input11.get("1.0",tk.END))
        else:
            time=0
        
        if (heaveside_active and heaveside_amplitude<=0) or (sinus_active and (sinus_amplitude<=0 or sinus_period<=0)) or (rectangle_active and (rectangle_amplitude<=0 or rectangle_period<=0)) or time <=0 or k1<=0 or k2<=0 or T1<=0 or T2<=0 :
            raise ValueError
        
    except:
        label17.grid(row=7,column=2,columnspan=2)
        return None

    try:
        if T1<=T2 and not flag:
            raise ValueError
    except:
        label18.grid(row=7,column=2,columnspan=2)
        button2.grid(row=8,column=2)
        return None

    flag = False

    params = [{'type':'sinus',
               'is_active':sinus_active,
               'amplitude':sinus_amplitude,
               'period':sinus_period*1000,
               'duty_cycle':0},
               {
                'type':'rectangle',
                'is_active':rectangle_active,
                'amplitude':rectangle_amplitude,
                'period':rectangle_period*1000,
                'duty_cycle':0.5},
               {'type':'heaviside_step',
                'is_active':heaveside_active,
                'amplitude':heaveside_amplitude,
                'period':0,
                'duty_cycle':0},
              ]
    algorithm(k1,k2,T1,T2,params,time)
    
        
#Unstable flag
flag = False

def set_flag():
    global flag
    flag=True
    simulate()


#Configuring the window
window = tk.Tk()
window.config(bg='#3f3f3f')

#Headings
label1= tk.Label(text="Wybór pobudzenia",font=('Arial',24,'normal'),bg='#3f3f3f')
label1.grid(row=0,column=0,columnspan=2,padx=10,pady=10)

label2 = tk.Label(text="Wybór parametrów",font=('Arial',24,'normal'),bg='#3f3f3f')
label2.grid(row=0,column=2,columnspan=2,padx=10,pady=10)



#Heavisde parameters
label3 = tk.Label(text='Skok jednostkowy',font=('Arial',16,'normal'),bg='#3f3f3f')
label3.grid(row=1,column=0,padx=10,pady=10)

var1 = tk.IntVar()
check_1 = tk.Checkbutton(variable=var1,onvalue=1,offvalue=0,bg='#3f3f3f')
check_1.grid(row=1,column=1,padx=10,pady=10)

label4 = tk.Label(text='Amplituda:',font=('Arial',12,'normal'),bg='#3f3f3f')
label4.grid(row=2,column=0,padx=10,pady=10)

text_input1 = tk.Text(width=5,height=2)
text_input1.grid(row=2,column=1,padx=10,pady=10)

# Sinus parameters
label5 = tk.Label(text='Sinus',font=('Arial',16,'normal'),bg='#3f3f3f')
label5.grid(row=3,column=0,padx=10,pady=10)

var2 = tk.IntVar()
check_2 = tk.Checkbutton(variable=var2,onvalue=1,offvalue=0,bg='#3f3f3f')
check_2.grid(row=3,column=1,padx=10,pady=10)

label6 = tk.Label(text='Amplituda:',font=('Arial',12,'normal'),bg='#3f3f3f')
label6.grid(row=4,column=0,padx=10,pady=10)

text_input2 = tk.Text(width=5,height=2)
text_input2.grid(row=4,column=1,padx=10,pady=10)

label7 = tk.Label(text='Okres [s]:',font=('Arial',12,'normal'),bg='#3f3f3f')
label7.grid(row=5,column=0,padx=10,pady=10)

text_input3 = tk.Text(width=5,height=2)
text_input3.grid(row=5,column=1,padx=10,pady=10)


#Rectangle parameters

label8 = tk.Label(text='Przebieg prostokatny',font=('Arial',16,'normal'),bg='#3f3f3f')
label8.grid(row=6,column=0,padx=10,pady=10)

var3=tk.IntVar()
check_3 = tk.Checkbutton(variable=var3,onvalue=1,offvalue=0,bg='#3f3f3f')
check_3.grid(row=6,column=1,padx=10,pady=10)

label9= tk.Label(text='Amplituda:',font=('Arial',12,'normal'),bg='#3f3f3f')
label9.grid(row=7,column=0,padx=10,pady=10)

text_input4 = tk.Text(width=5,height=2)
text_input4.grid(row=7,column=1,padx=10,pady=10)

label10 = tk.Label(text='Okres [s]:',font=('Arial',12,'normal'),bg='#3f3f3f')
label10.grid(row=8,column=0,padx=10,pady=10)

text_input5 = tk.Text(width=5,height=2)
text_input5.grid(row=8,column=1,padx=10,pady=10)

label11 = tk.Label(text='Wspolczynnik wypelnienia [%]:',font=('Arial',12,'normal'),bg='#3f3f3f')


text_input6= tk.Text(width=5,height=2)



#System parametrs
label12 = tk.Label(text="K1= ",font=('Arial',16,'normal'),bg='#3f3f3f')
label12.grid(row=1,column=2,padx=10,pady=10)

text_input7 = tk.Text(width=5,height=2)
text_input7.grid(row=1,column=3,padx=10,pady=10)

label13 = tk.Label(text="K2= ",font=('Arial',16,'normal'),bg='#3f3f3f')
label13.grid(row=2,column=2,padx=10,pady=10)

text_input8 = tk.Text(width=5,height=2)
text_input8.grid(row=2,column=3,padx=10,pady=10)

label14 = tk.Label(text="T1= ",font=('Arial',16,'normal'),bg='#3f3f3f')
label14.grid(row=3,column=2,padx=10,pady=10)

text_input9 = tk.Text(width=5,height=2)
text_input9.grid(row=3,column=3,padx=10,pady=10)

label15 = tk.Label(text="T2= ",font=('Arial',16,'normal'),bg='#3f3f3f')
label15.grid(row=4,column=2,padx=10,pady=10)

text_input10 = tk.Text(width=5,height=2)
text_input10.grid(row=4,column=3,padx=10,pady=10)

#Simulation time set
label16 = tk.Label(text="Czas symulacji [s]: ",font=('Arial',16,'normal'),bg='#3f3f3f')
label16.grid(row=5,column=2,padx=10,pady=10)

text_input11 = tk.Text(width=5,height=2)
text_input11.grid(row=5,column=3,padx=10,pady=10)

#Simulation button
button1 = tk.Button(text='Symuluj',highlightbackground='#3f3f3f',command=simulate)
button1.grid(row=6,column=2,columnspan=2)

label17 = tk.Label(text='Podano niepoprawne wartosci',font=('Arial',16,'normal'),bg='#3f3f3f',fg='red')

label18 = tk.Label(text='Układ nie jest stabilny. Czy chcesz symulować? ',font=('Arial',16,'normal'),bg='#3f3f3f',fg='red')
label19 = tk.Label(text='Nie wybrano zadnego pobudzenia ',font=('Arial',16,'normal'),bg='#3f3f3f',fg='red')

button2 = tk.Button(text='Tak',highlightbackground='#3f3f3f',command=set_flag)



window.mainloop()
