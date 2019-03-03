import tkinter as tk
import requests
from pprint import pprint
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

#from page_1 import root_p1
#from page_2 import root_p2
#from page_3 import root_p3

path_to_img_1 = 'transformer.jpg'
path_to_img_2 = 'oil.jpg'
path_to_img_3 = 'dga.jpg'
size_img = (300,200)
defalt_id =  42
res = (1440,900)
pad_x = 10
pad_y = 5
ip = '172.16.15.91:5000'
server_ip = f'http://{ip}/update-transformers'

root = tk.Tk()
root.title("Virtual Sensors - Demo")
root.geometry(f'{res[0]}x{res[1]}')
root.configure(background='#cdd2d8')

nb = ttk.Notebook(root)

def submit_1():
    """
    Modify this function to control the behaviour of
    the Submit button
    """
    data = dict()
    t_id = entry.get()
    if not t_id:
        return
    data['power_out_p1'] = str(scale_power_out_p1.get())
    data['power_out_p2'] = str(scale_power_out_p2.get())
    data['power_out_p3'] = str(scale_power_out_p3.get())
    data['voltage_in_p1'] = str(scale_volt_in_p1.get())
    data['voltage_in_p2'] = str(scale_volt_in_p2.get())
    data['voltage_in_p3'] = str(scale_volt_in_p3.get())
    data['voltage_out_p1'] = str(scale_volt_out_p1.get())
    data['voltage_out_p2'] = str(scale_volt_out_p2.get())
    data['voltage_out_p3'] = str(scale_volt_out_p3.get())
    data['oil_level'] = str(scale_oil.get())
    data['efficiency'] = str(scale_eff.get())
    data['winding_temp_1'] = str(temp_scale_1.get())
    data['winding_temp_2'] = str(temp_scale_2.get())
    data['winding_temp_3'] = str(temp_scale_3.get())
    data['oil_temp'] = str(temp_scale_4.get())
    data['breather_moisture'] = str(temp_scale_5.get())
    if button_brelay1['relief'] == tk.SUNKEN:
        data['buchholz_relay'] = '0'
    elif button_brelay2['relief'] == tk.SUNKEN:
        data['buchholz_relay'] = '1'
    else:
        data['buchholz_relay'] = '0'

    if button_grelay1['relief'] == tk.SUNKEN:
        data['pressure_relay'] = '0'
    elif button_grelay2['relief'] == tk.SUNKEN:
        data['pressure_relay'] = '1'
    else:
        data['pressure_relay'] = '0'

    if button_vibr1['relief'] == tk.SUNKEN:
        data['vibration'] = '0'
    elif button_vibr2['relief'] == tk.SUNKEN:
        data['vibration'] = '1'
    else:
        data['vibration'] = '0'


    if button_temp1['relief'] == tk.SUNKEN:
        data['oil_pump'] = '0'
    elif button_temp2['relief'] == tk.SUNKEN:
        data['oil_pump'] = '1'
    elif button_temp3['relief'] == tk.SUNKEN:
        data['oil_pump'] = '2'
    else:
        data['oil_pump'] = '0'

    try:
        r = requests.post(server_ip,json={"t_id": str(t_id), "new_data": {"health": data}})
        print('Request sent')
    except:
        pass

    h_data = dict()
    for key,value in data.items():
        h_data[key] = {"Thu Feb 28 11:04:26 2019": value}
    pprint(data)
    #pprint(h_data)

def submit_2():
    data = dict()
    t_id = entry.get()
    if not t_id:
        return
    data['moisture'] = str(scale_moisture.get())
    data['power'] = str(scale_power.get())
    data['acidity'] = str(scale_acidity.get())
    data['interfacial_tension'] = str(scale_if_tension.get())
    data['pcb'] = str(scale_pcb_tension.get())
    data['furan'] = str(scale_furan.get())
    data['dissolved_metals'] = 0

    if mb1['relief'] == tk.SUNKEN:
        data['dissolved_metals'] += 1
    if mb2['relief'] == tk.SUNKEN:
        data['dissolved_metals'] += 1
    if mb3['relief'] == tk.SUNKEN:
        data['dissolved_metals'] += 1
    if mb4['relief'] == tk.SUNKEN:
        data['dissolved_metals'] += 1
    if mb5['relief'] == tk.SUNKEN:
        data['dissolved_metals'] += 1
    if mb6['relief'] == tk.SUNKEN:
        data['dissolved_metals'] += 1
    if mb7['relief'] == tk.SUNKEN:
        data['dissolved_metals'] += 1
    data['dissolved_metals']  = str(data['dissolved_metals'])    
    try:
        r = requests.post(server_ip,json={"t_id": str(t_id), "new_data": {"health": data}})
        print('Request sent')
    except:
        pass
    pprint(data)

def submit_3():
    data = dict()
    t_id = entry.get()
    if not t_id:
        return
    data['dga_hydrogen'] = str(scale_h2_conc.get())
    data['dga_methane'] = str(scale_ch4_conc.get())
    data['dga_acetylene'] = str(scale_c2h2_conc.get())
    data['dga_ethylene'] = str(scale_c2h4_conc.get())
    data['dga_carbon_monoxide'] = str(scale_c0_conc.get())
    data['dga_carbon_dioxide'] = str(scale_c02_conc.get())

    try:
        r = requests.post(server_ip,json={"t_id": str(t_id), "new_data": {"health": data}})
        print('Request sent')
    except:
        pass

    pprint(data)

root_p1 = ttk.Frame(nb)
#text1 = ScrolledText(root_p1)
#text1.pack(expand=1, fill="both")#root_p1.title("Virtual Sensors - Demo")
#root_p1.geometry(f'{res[0]}x{res[1]}')
#root_p1.configure(background='#cdd2d8')

title = tk.Label(root_p1, text=f'Transformer',background='#cdd2d8', font=('Helvetica',24))
title.place(x=525,y=pad_y)
entry = tk.Entry(root_p1, width=7, font=('Helvetica',16))
entry.place(x=710,y=12)
im_1 = Image.open(path_to_img_1)
im_1 = im_1.resize(size_img)
img_1 = ImageTk.PhotoImage(im_1)
panel_1 = tk.Label(root_p1, image = img_1, borderwidth=2, relief="solid")
panel_1.place(x=500,y=50)

# power
power_main = tk.Label(root_p1, text='power Output (kVA)',background='#cdd2d8', font=('Helvetica',16,'bold'))
power_main.place(x=pad_x,y=400)
power_p1 = tk.Label(root_p1, text='Phase 1',background='#cdd2d8', font=('Helvetica',16))
power_p1.place(x=400,y=350)
power_p2 = tk.Label(root_p1, text='Phase 2',background='#cdd2d8', font=('Helvetica',16))
power_p2.place(x=700,y=350)
power_p3 = tk.Label(root_p1, text='Phase 3',background='#cdd2d8', font=('Helvetica',16))
power_p3.place(x=1000,y=350)

scale_power_out_p1 = tk.Scale(root_p1, from_=25, to=2500, orient=tk.HORIZONTAL, background='#cdd2d8',
                    width=20, length=200)
scale_power_out_p1.place(x=350,y=400)
scale_power_out_p1.set(100)

scale_power_out_p2 = tk.Scale(root_p1, from_=25, to=2500, orient=tk.HORIZONTAL, background='#cdd2d8',
                    width=20, length=200)
scale_power_out_p2.place(x=650,y=400)
scale_power_out_p2.set(100)

scale_power_out_p3 = tk.Scale(root_p1, from_=25, to=2500, orient=tk.HORIZONTAL, background='#cdd2d8',
                    width=20, length=200)
scale_power_out_p3.place(x=950,y=400)
scale_power_out_p3.set(100)

# voltage
diff = 150
volt_main = tk.Label(root_p1, text='Voltage',background='#cdd2d8', font=('Helvetica',16,'bold'))
volt_main.place(x=pad_x,y=400+diff)
volt_in = tk.Label(root_p1, text='Primary (kV)',background='#cdd2d8', font=('Helvetica',16))
volt_in.place(x=200,y=360+diff)
volt_out = tk.Label(root_p1, text='Secondary (V)',background='#cdd2d8', font=('Helvetica',16))
volt_out.place(x=200,y=430+diff)

scale_volt_in_p1 = tk.Scale(root_p1, from_=4, to=35, orient=tk.HORIZONTAL, background='#cdd2d8',
                    width=20, length=200)
scale_volt_in_p1.place(x=350,y=350+diff)
scale_volt_in_p1.set(15)

scale_volt_in_p2 = tk.Scale(root_p1, from_=4, to=35, orient=tk.HORIZONTAL, background='#cdd2d8',
                    width=20, length=200)
scale_volt_in_p2.place(x=650,y=350+diff)
scale_volt_in_p2.set(15)

scale_volt_in_p3 = tk.Scale(root_p1, from_=4, to=35, orient=tk.HORIZONTAL, background='#cdd2d8',
                    width=20, length=200)
scale_volt_in_p3.place(x=950,y=350+diff)
scale_volt_in_p3.set(15)

scale_volt_out_p1 = tk.Scale(root_p1, from_=100, to=240, orient=tk.HORIZONTAL, background='#cdd2d8',
                    width=20, length=200)
scale_volt_out_p1.place(x=350,y=420+diff)
scale_volt_out_p1.set(125)

scale_volt_out_p2 = tk.Scale(root_p1, from_=100, to=240, orient=tk.HORIZONTAL, background='#cdd2d8',
                    width=20, length=200)
scale_volt_out_p2.place(x=650,y=420+diff)
scale_volt_out_p2.set(125)

scale_volt_out_p3 = tk.Scale(root_p1, from_=100, to=240, orient=tk.HORIZONTAL, background='#cdd2d8',
                    width=20, length=200)
scale_volt_out_p3.place(x=950,y=420+diff)
scale_volt_out_p3.set(125)

# Oil pump
oil_pump = tk.Label(root_p1, text='Oil Pump',background='#cdd2d8', font=('Helvetica',16,'bold'))
oil_pump.place(x=pad_x,y=120)

def temp_b1_func():
    if button_temp1['relief'] == tk.RAISED:
        button_temp1.configure({'relief': tk.SUNKEN})
        button_temp2.configure({'relief': tk.RAISED})
        button_temp3.configure({'relief': tk.RAISED})

def temp_b2_func():
    if button_temp2['relief'] == tk.RAISED:
        button_temp1.configure({'relief': tk.RAISED})
        button_temp2.configure({'relief': tk.SUNKEN})
        button_temp3.configure({'relief': tk.RAISED})
def temp_b3_func():
    if button_temp3['relief'] == tk.RAISED:
        button_temp1.configure({'relief': tk.RAISED})
        button_temp2.configure({'relief': tk.RAISED})
        button_temp3.configure({'relief': tk.SUNKEN})

button_temp1 = tk.Button(root_p1, text = 'Healthy', relief=tk.RAISED, command = temp_b1_func,
                        bg='#99ff66', fg='black', font=('Helvetica',12), borderwidth=2)
button_temp1.place(x=200,y=120)
button_temp2 = tk.Button(root_p1, text = 'Abnormal', relief=tk.RAISED, command=temp_b2_func,
                        bg='#ff9933', fg='black', font=('Helvetica',12), borderwidth=2)
button_temp2.place(x=285,y=120)
button_temp3 = tk.Button(root_p1, text = 'Failed', relief=tk.RAISED, command=temp_b3_func,
                        bg='#ff3333', fg='black', font=('Helvetica',12), borderwidth=2)
button_temp3.place(x=383,y=120)

# vibr
vibr = tk.Label(root_p1, text='Vibration',background='#cdd2d8', font=('Helvetica',16,'bold'))
vibr.place(x=pad_x,y=175)

def vibr_1_func():
    if button_vibr1['relief'] == tk.RAISED:
        button_vibr1.configure({'relief': tk.SUNKEN})
        button_vibr2.configure({'relief': tk.RAISED})

def vibr_2_func():
    if button_vibr2['relief'] == tk.RAISED:
        button_vibr1.configure({'relief': tk.RAISED})
        button_vibr2.configure({'relief': tk.SUNKEN})

button_vibr1 = tk.Button(root_p1, text = 'Normal', relief=tk.RAISED, command = vibr_1_func,
                        bg='#99ff66', fg='black', font=('Helvetica',12), borderwidth=2)
button_vibr1.place(x=200,y=175)
button_vibr2 = tk.Button(root_p1, text = 'Abnormal', relief=tk.RAISED, command=vibr_2_func,
                        bg='#ff3333', fg='black', font=('Helvetica',12), borderwidth=2)
button_vibr2.place(x=285,y=175)

# Buchholz Relay
bstate = tk.Label(root_p1, text='Buchholz relay',background='#cdd2d8', font=('Helvetica',16,'bold'))
bstate.place(x=pad_x,y=25)

def brelay_1_func():
    if button_brelay1['relief'] == tk.RAISED:
        button_brelay1.configure({'relief': tk.SUNKEN})
        button_brelay2.configure({'relief': tk.RAISED})

def brelay_2_func():
    if button_brelay2['relief'] == tk.RAISED:
        button_brelay1.configure({'relief': tk.RAISED})
        button_brelay2.configure({'relief': tk.SUNKEN})

button_brelay1 = tk.Button(root_p1, text = 'Normal', relief=tk.RAISED, command = brelay_1_func,
                        bg='#99ff66', fg='black', font=('Helvetica',12), borderwidth=2)
button_brelay1.place(x=200,y=25)
button_brelay2 = tk.Button(root_p1, text = 'Triggered', relief=tk.RAISED, command=brelay_2_func,
                        bg='#ff3333', fg='black', font=('Helvetica',12), borderwidth=2)
button_brelay2.place(x=285,y=25)

# Pressure Relay
gstate = tk.Label(root_p1, text='Pressure relay',background='#cdd2d8', font=('Helvetica',16,'bold'))
gstate.place(x=pad_x,y=70)

def grelay_1_func():
    if button_grelay1['relief'] == tk.RAISED:
        button_grelay1.configure({'relief': tk.SUNKEN})
        button_grelay2.configure({'relief': tk.RAISED})

def grelay_2_func():
    if button_grelay2['relief'] == tk.RAISED:
        button_grelay1.configure({'relief': tk.RAISED})
        button_grelay2.configure({'relief': tk.SUNKEN})

button_grelay1 = tk.Button(root_p1, text = 'Normal', relief=tk.RAISED, command = grelay_1_func,
                        bg='#99ff66', fg='black', font=('Helvetica',12), borderwidth=2)
button_grelay1.place(x=200,y=70)
button_grelay2 = tk.Button(root_p1, text = 'Triggered', relief=tk.RAISED, command=grelay_2_func,
                        bg='#ff3333', fg='black', font=('Helvetica',12), borderwidth=2)
button_grelay2.place(x=285,y=70)

# oil level
oil_level = tk.Label(root_p1, text='Oil Level (%)',background='#cdd2d8', font=('Helvetica',16,'bold'))
oil_level.place(x=pad_x,y=230)

scale_oil = tk.Scale(root_p1, from_=0, to=100, orient=tk.HORIZONTAL, background='#cdd2d8',
                    width=20, length=240)
scale_oil.place(x=200,y=220)
scale_oil.set(50)

# efficiency
eff = tk.Label(root_p1, text='Efficiency (%)',background='#cdd2d8', font=('Helvetica',16,'bold'))
eff.place(x=pad_x,y=300)

scale_eff = tk.Scale(root_p1, from_=0, to=100, orient=tk.HORIZONTAL, background='#cdd2d8',
                    width=20, length=240)
scale_eff.place(x=200,y=290)
scale_eff.set(50)

# oil Temperature

temp_1 = tk.Label(root_p1, text='Winding Temp Sensor 1',background='#cdd2d8', font=('Helvetica',16,'bold'))
temp_1.place(x=850,y=75)
temp_scale_1 = tk.Scale(root_p1, from_=0, to=110, orient=tk.HORIZONTAL, background='#cdd2d8',
                    width=20, length=240)
temp_scale_1.place(x=1111,y=70)
temp_scale_1.set(35)

temp_2 = tk.Label(root_p1, text='Winding Temp Sensor 2',background='#cdd2d8', font=('Helvetica',16,'bold'))
temp_2.place(x=850,y=135)
temp_scale_2 = tk.Scale(root_p1, from_=0, to=110, orient=tk.HORIZONTAL, background='#cdd2d8',
                    width=20, length=240)
temp_scale_2.place(x=1111, y=130)
temp_scale_2.set(35)

temp_3 = tk.Label(root_p1, text='Winding Temp Sensor 3',background='#cdd2d8', font=('Helvetica',16,'bold'))
temp_3.place(x=850,y=195)
temp_scale_3 = tk.Scale(root_p1, from_=0, to=110, orient=tk.HORIZONTAL, background='#cdd2d8',
                    width=20, length=240)
temp_scale_3.place(x=1111,y=190)
temp_scale_3.set(35)

temp_4 = tk.Label(root_p1, text='Oil Temp Sensor',background='#cdd2d8', font=('Helvetica',16,'bold'))
temp_4.place(x=850,y=15)
temp_scale_4 = tk.Scale(root_p1, from_=0, to=110, orient=tk.HORIZONTAL, background='#cdd2d8',
                    width=20, length=240)
temp_scale_4.place(x=1111,y=10)
temp_scale_4.set(35)

temp_5 = tk.Label(root_p1, text='Breather Moisture Saturation',background='#cdd2d8', font=('Helvetica',16,'bold'))
temp_5.place(x=800,y=255)
temp_scale_5 = tk.Scale(root_p1, from_=0, to=100, orient=tk.HORIZONTAL, background='#cdd2d8',
                    width=20, length=240)
temp_scale_5.place(x=1111,y=250)
temp_scale_5.set(35)

# compound

# submit button
button_1 = tk.Button(root_p1, text="Submit", foreground="white", background="black",
                        width=25, font=('Helvetica',16), command=submit_1)
button_1.place(x=500,y=635)

root_p2 = ttk.Frame(nb)

title = tk.Label(root_p2, text=f'Oil Quality',background='#cdd2d8', font=('Helvetica',24))
title.place(x=525,y=pad_y)
im_2 = Image.open(path_to_img_2)
im_2 = im_2.resize(size_img)
img_2 = ImageTk.PhotoImage(im_2)
panel_2 = tk.Label(root_p2, image = img_2, borderwidth=2, relief="solid")
panel_2.place(x=500,y=50)

moisture = tk.Label(root_p2, text='Moisture (ppm)',background='#cdd2d8', font=('Helvetica',16))
moisture.place(x=10,y=25)
scale_moisture = tk.Scale(root_p2, from_=0, to=30, orient=tk.HORIZONTAL, background='#cdd2d8',
                    width=20, length=300)
scale_moisture.place(x=160,y=20)
scale_moisture.set(50)

power = tk.Label(root_p2, text='Power Factor',background='#cdd2d8', font=('Helvetica',16))
power.place(x=10,y=150)
scale_power = tk.Scale(root_p2, from_=0, to=100, orient=tk.HORIZONTAL, background='#cdd2d8',
                    width=20, length=300)
scale_power.place(x=160,y=145)
scale_power.set(50)

acidity = tk.Label(root_p2, text='Acidity ( mgKOH/g )',background='#cdd2d8', font=('Helvetica',16))
acidity.place(x=850,y=25)
scale_acidity = tk.Scale(root_p2, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL, background='#cdd2d8',
                    width=20, length=300)
scale_acidity.place(x=1050,y=20)
scale_acidity.set(0.01)

if_tension = tk.Label(root_p2, text='Interfacial Tension',background='#cdd2d8', font=('Helvetica',16))
if_tension.place(x=850,y=150)
scale_if_tension = tk.Scale(root_p2, from_=0, to=100, orient=tk.HORIZONTAL, background='#cdd2d8',
                    width=20, length=300)
scale_if_tension.place(x=1050,y=145)
scale_if_tension.set(50)

pcb_tension = tk.Label(root_p2, text='PCB concentration',background='#cdd2d8', font=('Helvetica',16))
pcb_tension.place(x=850,y=265)
pcb_tension_2 = tk.Label(root_p2, text='(ppm by weight)',background='#cdd2d8', font=('Helvetica',16))
pcb_tension_2.place(x=850,y=295)
scale_pcb_tension = tk.Scale(root_p2, from_=0, to=60, orient=tk.HORIZONTAL, background='#cdd2d8',
                    width=20, length=300)
scale_pcb_tension.place(x=1050,y=260)
scale_pcb_tension.set(3)

metal = tk.Label(root_p2, text='Dissolved Metals',background='#cdd2d8', font=('Helvetica',16))
metal.place(x=20,y=450)

def mb1_f():
    if mb1['relief'] == tk.RAISED:
        mb1.configure({"relief": tk.SUNKEN, "bg": "#ff3333"})
    elif mb1['relief'] == tk.SUNKEN:
        mb1.configure({"relief": tk.RAISED, "bg": "#ff9933"})
def mb2_f():
    if mb2['relief'] == tk.RAISED:
        mb2.configure({"relief": tk.SUNKEN, "bg": "#ff3333"})
    elif mb2['relief'] == tk.SUNKEN:
        mb2.configure({"relief": tk.RAISED, "bg": "#ff9933"})
def mb3_f():
    if mb3['relief'] == tk.RAISED:
        mb3.configure({"relief": tk.SUNKEN, "bg": "#ff3333"})
    elif mb3['relief'] == tk.SUNKEN:
        mb3.configure({"relief": tk.RAISED, "bg": "#ff9933"})
def mb4_f():
    if mb4['relief'] == tk.RAISED:
        mb4.configure({"relief": tk.SUNKEN, "bg": "#ff3333"})
    elif mb4['relief'] == tk.SUNKEN:
        mb4.configure({"relief": tk.RAISED, "bg": "#ff9933"})
def mb5_f():
    if mb5['relief'] == tk.RAISED:
        mb5.configure({"relief": tk.SUNKEN, "bg": "#ff3333"})
    elif mb5['relief'] == tk.SUNKEN:
        mb5.configure({"relief": tk.RAISED, "bg": "#ff9933"})
def mb6_f():
    if mb6['relief'] == tk.RAISED:
        mb6.configure({"relief": tk.SUNKEN, "bg": "#ff3333"})
    elif mb6['relief'] == tk.SUNKEN:
        mb6.configure({"relief": tk.RAISED, "bg": "#ff9933"})
def mb7_f():
    if mb7['relief'] == tk.RAISED:
        mb7.configure({"relief": tk.SUNKEN, "bg": "#ff3333"})
    elif mb7['relief'] == tk.SUNKEN:
        mb7.configure({"relief": tk.RAISED, "bg": "#ff9933"})

mb1 = tk.Button(root_p2, text="Aluminium", foreground="black", bg="#ff9933",
                        width=10, font=('Helvetica',16), command=mb1_f, relief=tk.RAISED)
mb1.place(x=220,y=450)
mb2 = tk.Button(root_p2, text="Copper", foreground="black", bg="#ff9933",
                        width=5, font=('Helvetica',16), command=mb2_f, relief=tk.RAISED)
mb2.place(x=350,y=450)
mb3 = tk.Button(root_p2, text="Zinc", foreground="black", bg="#ff9933",
                        width=5, font=('Helvetica',16), command=mb3_f, relief=tk.RAISED)
mb3.place(x=437,y=450)
mb4 = tk.Button(root_p2, text="Iron", foreground="black", bg="#ff9933",
                        width=5, font=('Helvetica',16), command=mb4_f, relief=tk.RAISED)
mb4.place(x=520,y=450)
mb5 = tk.Button(root_p2, text="Lead", foreground="black", bg="#ff9933",
                        width=5, font=('Helvetica',16), command=mb5_f, relief=tk.RAISED)
mb5.place(x=600,y=450)
mb6 = tk.Button(root_p2, text="Silver", foreground="black", bg="#ff9933",
                        width=5, font=('Helvetica',16), command=mb6_f, relief=tk.RAISED)
mb6.place(x=685,y=450)
mb7 = tk.Button(root_p2, text="Tin", foreground="black", bg="#ff9933",
                        width=5, font=('Helvetica',16), command=mb7_f, relief=tk.RAISED)
mb7.place(x=770,y=450)

mb1 = tk.Button(root_p2, text="Aluminium", foreground="black", bg="#ff9933",
                        width=10, font=('Helvetica',16), command=mb1_f, relief=tk.RAISED)

furan = tk.Label(root_p2, text='Furfuraldehyde (DP)',background='#cdd2d8', font=('Helvetica',16))
furan.place(x=20,y=550)
scale_furan = tk.Scale(root_p2, from_=200, to=1000, orient=tk.HORIZONTAL, background='#cdd2d8',
                    width=20, length=300)
scale_furan.place(x=260,y=540)
scale_furan.set(50)

# submit button
button_2 = tk.Button(root_p2, text="Submit", foreground="white", background="black",
                        width=25, font=('Helvetica',16), command=submit_2)
button_2.place(x=500,y=635)

root_p3 = ttk.Frame(nb)

title = tk.Label(root_p3, text=f'Dissolved Gas Analysis',background='#cdd2d8', font=('Helvetica',24))
title.place(x=525,y=pad_y)
im_3 = Image.open(path_to_img_3)
im_3 = im_3.resize(size_img)
img_3 = ImageTk.PhotoImage(im_3)
panel_3 = tk.Label(root_p3, image = img_3, borderwidth=2, relief="solid")
panel_3.place(x=500,y=50)

# power
power_main = tk.Label(root_p3, text='Dissolved Concentration (ppm)',background='#cdd2d8', font=('Helvetica',16,'bold'))
power_main.place(x=pad_x,y=400)
power_p1 = tk.Label(root_p3, text='Hydrogen',background='#cdd2d8', font=('Helvetica',16))
power_p1.place(x=400,y=350)
power_p2 = tk.Label(root_p3, text='Methane',background='#cdd2d8', font=('Helvetica',16))
power_p2.place(x=700,y=350)
power_p3 = tk.Label(root_p3, text='Acetylene',background='#cdd2d8', font=('Helvetica',16))
power_p3.place(x=1000,y=350)

scale_h2_conc = tk.Scale(root_p3, from_=100, to=1000, orient=tk.HORIZONTAL, background='#cdd2d8',
                    width=20, length=200)
scale_h2_conc.place(x=350,y=400)
scale_h2_conc.set(100)

scale_ch4_conc = tk.Scale(root_p3, from_=20, to=80, orient=tk.HORIZONTAL, background='#cdd2d8',
                    width=20, length=200)
scale_ch4_conc.place(x=650,y=400)
scale_ch4_conc.set(100)

scale_c2h2_conc = tk.Scale(root_p3, from_=10, to=70, orient=tk.HORIZONTAL, background='#cdd2d8',
                    width=20, length=200)
scale_c2h2_conc.place(x=950,y=400)
scale_c2h2_conc.set(100)

# voltage
diff = 150
gas1 = tk.Label(root_p3, text='Ethylene',background='#cdd2d8', font=('Helvetica',16))
gas1.place(x=400,y=350+diff)
gas2 = tk.Label(root_p3, text='CarbonMonoxide',background='#cdd2d8', font=('Helvetica',16))
gas2.place(x=680,y=350+diff)
gas3 = tk.Label(root_p3, text='CarbonDioxide',background='#cdd2d8', font=('Helvetica',16))
gas3.place(x=980,y=350+diff)

scale_c2h4_conc = tk.Scale(root_p3, from_=15, to=150, orient=tk.HORIZONTAL, background='#cdd2d8',
                    width=20, length=200)
scale_c2h4_conc.place(x=350,y=400+diff)
scale_c2h4_conc.set(15)

scale_c0_conc = tk.Scale(root_p3, from_=400, to=1000, orient=tk.HORIZONTAL, background='#cdd2d8',
                    width=20, length=200)
scale_c0_conc.place(x=650,y=400+diff)
scale_c0_conc.set(15)

scale_c02_conc = tk.Scale(root_p3, from_=9000, to=15000, orient=tk.HORIZONTAL, background='#cdd2d8',
                    width=20, length=200)
scale_c02_conc.place(x=950,y=400+diff)
scale_c02_conc.set(15)

# submit button
button_3 = tk.Button(root_p3, text="Submit", foreground="white", background="black",
                        width=25, font=('Helvetica',16), command=submit_3)
button_3.place(x=500,y=635)


nb.add(root_p1, text='One')
nb.add(root_p2, text='Two')
nb.add(root_p3, text='Three')

nb.pack(expand=1, fill="both")

root.mainloop()
