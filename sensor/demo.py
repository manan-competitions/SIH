import tkinter as tk
import requests
from pprint import pprint
from PIL import ImageTk, Image

path_to_img = 'transformer.jpg'
defalt_id =  42
size_img = (300,200)
res = (1440,900)
pad_x = 10
pad_y = 5
ip = '172.16.15.91:5000'
server_ip = f'http://{ip}/update-transformers'

def submit():
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

    #pprint(h_data)

window = tk.Tk()
window.title("Virtual Sensors - Demo")
window.geometry(f'{res[0]}x{res[1]}')
window.configure(background='white')

title = tk.Label(window, text=f'Transformer',background='white', font=('Helvetica',24))
title.place(x=525,y=pad_y)
entry = tk.Entry(window, width=7, font=('Helvetica',16))
entry.place(x=710,y=12)
im = Image.open(path_to_img)
im = im.resize(size_img)
img = ImageTk.PhotoImage(im)
panel = tk.Label(window, image = img, borderwidth=2, relief="solid")
panel.place(x=500,y=50)

# power
power_main = tk.Label(window, text='power Output (kVA)',background='white', font=('Helvetica',16,'bold'))
power_main.place(x=pad_x,y=400)
power_p1 = tk.Label(window, text='Phase 1',background='white', font=('Helvetica',16))
power_p1.place(x=400,y=350)
power_p2 = tk.Label(window, text='Phase 2',background='white', font=('Helvetica',16))
power_p2.place(x=700,y=350)
power_p3 = tk.Label(window, text='Phase 3',background='white', font=('Helvetica',16))
power_p3.place(x=1000,y=350)

scale_power_out_p1 = tk.Scale(window, from_=25, to=2500, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=200)
scale_power_out_p1.place(x=350,y=400)
scale_power_out_p1.set(100)

scale_power_out_p2 = tk.Scale(window, from_=25, to=2500, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=200)
scale_power_out_p2.place(x=650,y=400)
scale_power_out_p2.set(100)

scale_power_out_p3 = tk.Scale(window, from_=25, to=2500, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=200)
scale_power_out_p3.place(x=950,y=400)
scale_power_out_p3.set(100)

# voltage
diff = 150
volt_main = tk.Label(window, text='Voltage',background='white', font=('Helvetica',16,'bold'))
volt_main.place(x=pad_x,y=400+diff)
volt_in = tk.Label(window, text='Primary (kV)',background='white', font=('Helvetica',16))
volt_in.place(x=200,y=360+diff)
volt_out = tk.Label(window, text='Secondary (V)',background='white', font=('Helvetica',16))
volt_out.place(x=200,y=430+diff)

scale_volt_in_p1 = tk.Scale(window, from_=4, to=35, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=200)
scale_volt_in_p1.place(x=350,y=350+diff)
scale_volt_in_p1.set(15)

scale_volt_in_p2 = tk.Scale(window, from_=4, to=35, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=200)
scale_volt_in_p2.place(x=650,y=350+diff)
scale_volt_in_p2.set(15)

scale_volt_in_p3 = tk.Scale(window, from_=4, to=35, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=200)
scale_volt_in_p3.place(x=950,y=350+diff)
scale_volt_in_p3.set(15)

scale_volt_out_p1 = tk.Scale(window, from_=100, to=240, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=200)
scale_volt_out_p1.place(x=350,y=420+diff)
scale_volt_out_p1.set(125)

scale_volt_out_p2 = tk.Scale(window, from_=100, to=240, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=200)
scale_volt_out_p2.place(x=650,y=420+diff)
scale_volt_out_p2.set(125)

scale_volt_out_p3 = tk.Scale(window, from_=100, to=240, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=200)
scale_volt_out_p3.place(x=950,y=420+diff)
scale_volt_out_p3.set(125)

# Oil pump
oil_pump = tk.Label(window, text='Oil Pump',background='white', font=('Helvetica',16,'bold'))
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

button_temp1 = tk.Button(window, text = 'Healthy', relief=tk.RAISED, command = temp_b1_func,
                        bg='#99ff66', fg='black', font=('Helvetica',12), borderwidth=2)
button_temp1.place(x=200,y=120)
button_temp2 = tk.Button(window, text = 'Abnormal', relief=tk.RAISED, command=temp_b2_func,
                        bg='#ff9933', fg='black', font=('Helvetica',12), borderwidth=2)
button_temp2.place(x=285,y=120)
button_temp3 = tk.Button(window, text = 'Failed', relief=tk.RAISED, command=temp_b3_func,
                        bg='#ff3333', fg='black', font=('Helvetica',12), borderwidth=2)
button_temp3.place(x=383,y=120)

# vibr
vibr = tk.Label(window, text='Vibration',background='white', font=('Helvetica',16,'bold'))
vibr.place(x=pad_x,y=175)

def vibr_1_func():
    if button_vibr1['relief'] == tk.RAISED:
        button_vibr1.configure({'relief': tk.SUNKEN})
        button_vibr2.configure({'relief': tk.RAISED})

def vibr_2_func():
    if button_vibr2['relief'] == tk.RAISED:
        button_vibr1.configure({'relief': tk.RAISED})
        button_vibr2.configure({'relief': tk.SUNKEN})

button_vibr1 = tk.Button(window, text = 'Normal', relief=tk.RAISED, command = vibr_1_func,
                        bg='#99ff66', fg='black', font=('Helvetica',12), borderwidth=2)
button_vibr1.place(x=200,y=175)
button_vibr2 = tk.Button(window, text = 'Abnormal', relief=tk.RAISED, command=vibr_2_func,
                        bg='#ff3333', fg='black', font=('Helvetica',12), borderwidth=2)
button_vibr2.place(x=285,y=175)

# Buchholz Relay
bstate = tk.Label(window, text='Buchholz relay',background='white', font=('Helvetica',16,'bold'))
bstate.place(x=pad_x,y=25)

def brelay_1_func():
    if button_brelay1['relief'] == tk.RAISED:
        button_brelay1.configure({'relief': tk.SUNKEN})
        button_brelay2.configure({'relief': tk.RAISED})

def brelay_2_func():
    if button_brelay2['relief'] == tk.RAISED:
        button_brelay1.configure({'relief': tk.RAISED})
        button_brelay2.configure({'relief': tk.SUNKEN})

button_brelay1 = tk.Button(window, text = 'Normal', relief=tk.RAISED, command = brelay_1_func,
                        bg='#99ff66', fg='black', font=('Helvetica',12), borderwidth=2)
button_brelay1.place(x=200,y=25)
button_brelay2 = tk.Button(window, text = 'Triggered', relief=tk.RAISED, command=brelay_2_func,
                        bg='#ff3333', fg='black', font=('Helvetica',12), borderwidth=2)
button_brelay2.place(x=285,y=25)

# Pressure Relay
gstate = tk.Label(window, text='Pressure relay',background='white', font=('Helvetica',16,'bold'))
gstate.place(x=pad_x,y=70)

def grelay_1_func():
    if button_grelay1['relief'] == tk.RAISED:
        button_grelay1.configure({'relief': tk.SUNKEN})
        button_grelay2.configure({'relief': tk.RAISED})

def grelay_2_func():
    if button_grelay2['relief'] == tk.RAISED:
        button_grelay1.configure({'relief': tk.RAISED})
        button_grelay2.configure({'relief': tk.SUNKEN})

button_grelay1 = tk.Button(window, text = 'Normal', relief=tk.RAISED, command = grelay_1_func,
                        bg='#99ff66', fg='black', font=('Helvetica',12), borderwidth=2)
button_grelay1.place(x=200,y=70)
button_grelay2 = tk.Button(window, text = 'Triggered', relief=tk.RAISED, command=grelay_2_func,
                        bg='#ff3333', fg='black', font=('Helvetica',12), borderwidth=2)
button_grelay2.place(x=285,y=70)

# oil level
oil_level = tk.Label(window, text='Oil Level (%)',background='white', font=('Helvetica',16,'bold'))
oil_level.place(x=pad_x,y=230)

scale_oil = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=240)
scale_oil.place(x=200,y=220)
scale_oil.set(50)

# efficiency
eff = tk.Label(window, text='Efficiency (%)',background='white', font=('Helvetica',16,'bold'))
eff.place(x=pad_x,y=300)

scale_eff = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=240)
scale_eff.place(x=200,y=290)
scale_eff.set(50)

# oil Temperature

temp_1 = tk.Label(window, text='Winding Temp Sensor 1',background='white', font=('Helvetica',16,'bold'))
temp_1.place(x=850,y=75)
temp_scale_1 = tk.Scale(window, from_=0, to=110, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=240)
temp_scale_1.place(x=1111,y=70)
temp_scale_1.set(35)

temp_2 = tk.Label(window, text='Winding Temp Sensor 2',background='white', font=('Helvetica',16,'bold'))
temp_2.place(x=850,y=135)
temp_scale_2 = tk.Scale(window, from_=0, to=110, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=240)
temp_scale_2.place(x=1111, y=130)
temp_scale_2.set(35)

temp_3 = tk.Label(window, text='Winding Temp Sensor 3',background='white', font=('Helvetica',16,'bold'))
temp_3.place(x=850,y=195)
temp_scale_3 = tk.Scale(window, from_=0, to=110, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=240)
temp_scale_3.place(x=1111,y=190)
temp_scale_3.set(35)

temp_4 = tk.Label(window, text='Oil Temp Sensor',background='white', font=('Helvetica',16,'bold'))
temp_4.place(x=850,y=15)
temp_scale_4 = tk.Scale(window, from_=0, to=110, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=240)
temp_scale_4.place(x=1111,y=10)
temp_scale_4.set(35)

temp_5 = tk.Label(window, text='Breather Moisture Saturation',background='white', font=('Helvetica',16,'bold'))
temp_5.place(x=800,y=255)
temp_scale_5 = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=240)
temp_scale_5.place(x=1111,y=250)
temp_scale_5.set(35)

# compound

# submit button
button = tk.Button(window, text="Submit", foreground="white", background="black",
                        width=25, font=('Helvetica',16), command=submit)
button.place(x=500,y=665)

window.mainloop()
