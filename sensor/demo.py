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
#sld_len = 700
server_ip = 'http://127.0.0.1:5000/update-transformers'

def submit():
    """
    Modify this function to control the behaviour of
    the Submit button
    """
    data = dict()
    t_id = entry.get()
    if not t_id:
        return
    data['current_in_p1'] = str(scale_curr_in_p1.get())
    data['current_in_p2'] = str(scale_curr_in_p2.get())
    data['current_in_p3'] = str(scale_curr_in_p3.get())
    data['current_out_p1'] = str(scale_curr_out_p1.get())
    data['current_out_p2'] = str(scale_curr_out_p2.get())
    data['current_out_p3'] = str(scale_curr_out_p3.get())
    data['voltage_in_p1'] = str(scale_volt_in_p1.get())
    data['voltage_in_p2'] = str(scale_volt_in_p2.get())
    data['voltage_in_p3'] = str(scale_volt_in_p3.get())
    data['voltage_out_p1'] = str(scale_volt_out_p1.get())
    data['voltage_out_p2'] = str(scale_volt_out_p2.get())
    data['voltage_out_p3'] = str(scale_volt_out_p3.get())
    data['oil_level'] = str(scale_oil.get())
    data['temp_1'] = str(temp_scale_1.get())
    data['temp_2'] = str(temp_scale_2.get())
    data['temp_3'] = str(temp_scale_3.get())
    if button_relay1['relief'] == tk.SUNKEN:
        data['Buchholz_relay'] = 'normal'
    elif button_relay2['relief'] == tk.SUNKEN:
        data['Buchholz_relay'] = 'triggered'
    else:
        data['Buchholz_relay'] = 'normal'

    if button_state1['relief'] == tk.SUNKEN:
        data['state'] = 'normal'
    elif button_state2['relief'] == tk.SUNKEN:
        data['state'] = 'triggered'
    else:
        data['state'] = 'normal'

    if button_temp1['relief'] == tk.SUNKEN:
        data['oil_pump'] = 'normal'
    elif button_temp2['relief'] == tk.SUNKEN:
        data['oil_pump'] = 'abnormal'
    elif button_temp3['relief'] == tk.SUNKEN:
        data['oil_pump'] = 'failed'
    else:
        data['oil_pump'] = 'normal'

    #print(t_id)
    #pprint(data)

    r = requests.post(server_ip,json={"t_id": str(t_id), "new_data": {"health": data}})

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

# current
curr_main = tk.Label(window, text='Current (mA)',background='white', font=('Helvetica',16,'bold'))
curr_main.place(x=pad_x,y=400)
curr_in = tk.Label(window, text='Input',background='white', font=('Helvetica',16))
curr_in.place(x=250,y=360)
curr_out = tk.Label(window, text='Output',background='white', font=('Helvetica',16))
curr_out.place(x=250,y=430)
curr_p1 = tk.Label(window, text='Phase 1',background='white', font=('Helvetica',16))
curr_p1.place(x=400,y=300)
curr_p2 = tk.Label(window, text='Phase 2',background='white', font=('Helvetica',16))
curr_p2.place(x=700,y=300)
curr_p3 = tk.Label(window, text='Phase 3',background='white', font=('Helvetica',16))
curr_p3.place(x=1000,y=300)

scale_curr_in_p1 = tk.Scale(window, from_=0, to=200, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=200)
scale_curr_in_p1.place(x=350,y=350)
scale_curr_in_p1.set(100)

scale_curr_in_p2 = tk.Scale(window, from_=0, to=200, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=200)
scale_curr_in_p2.place(x=650,y=350)
scale_curr_in_p2.set(100)

scale_curr_in_p3 = tk.Scale(window, from_=0, to=200, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=200)
scale_curr_in_p3.place(x=950,y=350)
scale_curr_in_p3.set(100)

scale_curr_out_p1 = tk.Scale(window, from_=0, to=200, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=200)
scale_curr_out_p1.place(x=350,y=420)
scale_curr_out_p1.set(100)

scale_curr_out_p2 = tk.Scale(window, from_=0, to=200, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=200)
scale_curr_out_p2.place(x=650,y=420)
scale_curr_out_p2.set(100)

scale_curr_out_p3 = tk.Scale(window, from_=0, to=200, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=200)
scale_curr_out_p3.place(x=950,y=420)
scale_curr_out_p3.set(100)

# voltage
diff = 150
volt_main = tk.Label(window, text='Primary Voltage (kV)',background='white', font=('Helvetica',16,'bold'))
volt_main.place(x=pad_x,y=400+diff)
volt_in = tk.Label(window, text='Input',background='white', font=('Helvetica',16))
volt_in.place(x=250,y=360+diff)
volt_out = tk.Label(window, text='Output',background='white', font=('Helvetica',16))
volt_out.place(x=250,y=430+diff)

scale_volt_in_p1 = tk.Scale(window, from_=6, to=132, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=200)
scale_volt_in_p1.place(x=350,y=350+diff)
scale_volt_in_p1.set(15)

scale_volt_in_p2 = tk.Scale(window, from_=6, to=132, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=200)
scale_volt_in_p2.place(x=650,y=350+diff)
scale_volt_in_p2.set(15)

scale_volt_in_p3 = tk.Scale(window, from_=6, to=132, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=200)
scale_volt_in_p3.place(x=950,y=350+diff)
scale_volt_in_p3.set(15)

scale_volt_out_p1 = tk.Scale(window, from_=6, to=132, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=200)
scale_volt_out_p1.place(x=350,y=420+diff)
scale_volt_out_p1.set(15)

scale_volt_out_p2 = tk.Scale(window, from_=6, to=132, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=200)
scale_volt_out_p2.place(x=650,y=420+diff)
scale_volt_out_p2.set(15)

scale_volt_out_p3 = tk.Scale(window, from_=6, to=132, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=200)
scale_volt_out_p3.place(x=950,y=420+diff)
scale_volt_out_p3.set(15)

# Oil pump
oil_pump = tk.Label(window, text='Oil Pump',background='white', font=('Helvetica',16,'bold'))
oil_pump.place(x=pad_x,y=100)

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
button_temp1.place(x=200,y=100)
button_temp2 = tk.Button(window, text = 'Abnormal', relief=tk.RAISED, command=temp_b2_func,
                        bg='#ff9933', fg='black', font=('Helvetica',12), borderwidth=2)
button_temp2.place(x=285,y=100)
button_temp3 = tk.Button(window, text = 'Failed', relief=tk.RAISED, command=temp_b3_func,
                        bg='#ff3333', fg='black', font=('Helvetica',12), borderwidth=2)
button_temp3.place(x=383,y=100)

# State
state = tk.Label(window, text='State',background='white', font=('Helvetica',16,'bold'))
state.place(x=pad_x,y=175)

def state_1_func():
    if button_state1['relief'] == tk.RAISED:
        button_state1.configure({'relief': tk.SUNKEN})
        button_state2.configure({'relief': tk.RAISED})

def state_2_func():
    if button_state2['relief'] == tk.RAISED:
        button_state1.configure({'relief': tk.RAISED})
        button_state2.configure({'relief': tk.SUNKEN})

button_state1 = tk.Button(window, text = 'Normal', relief=tk.RAISED, command = state_1_func,
                        bg='#99ff66', fg='black', font=('Helvetica',12), borderwidth=2)
button_state1.place(x=200,y=175)
button_state2 = tk.Button(window, text = 'Triggered', relief=tk.RAISED, command=state_2_func,
                        bg='#ff3333', fg='black', font=('Helvetica',12), borderwidth=2)
button_state2.place(x=285,y=175)

# Relay
state = tk.Label(window, text='Buchholz relay',background='white', font=('Helvetica',16,'bold'))
state.place(x=pad_x,y=25)

def relay_1_func():
    if button_relay1['relief'] == tk.RAISED:
        button_relay1.configure({'relief': tk.SUNKEN})
        button_relay2.configure({'relief': tk.RAISED})

def relay_2_func():
    if button_relay2['relief'] == tk.RAISED:
        button_relay1.configure({'relief': tk.RAISED})
        button_relay2.configure({'relief': tk.SUNKEN})

button_relay1 = tk.Button(window, text = 'Healthy', relief=tk.RAISED, command = relay_1_func,
                        bg='#99ff66', fg='black', font=('Helvetica',12), borderwidth=2)
button_relay1.place(x=200,y=25)
button_relay2 = tk.Button(window, text = 'Abnormal', relief=tk.RAISED, command=relay_2_func,
                        bg='#ff3333', fg='black', font=('Helvetica',12), borderwidth=2)
button_relay2.place(x=285,y=25)

# oil level
oil_level = tk.Label(window, text='Oil Level (%)',background='white', font=('Helvetica',16,'bold'))
oil_level.place(x=pad_x,y=250)

scale_oil = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=240)
scale_oil.place(x=200,y=240)
scale_oil.set(50)

# oil Temperature

temp_1 = tk.Label(window, text='Temp Sensor 1 (Celsius)',background='white', font=('Helvetica',16,'bold'))
temp_1.place(x=850,y=75)
temp_scale_1 = tk.Scale(window, from_=0, to=110, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=240)
temp_scale_1.place(x=1111,y=70)
temp_scale_1.set(35)

temp_2 = tk.Label(window, text='Temp Sensor 2 (Celsius)',background='white', font=('Helvetica',16,'bold'))
temp_2.place(x=850,y=135)
temp_scale_2 = tk.Scale(window, from_=0, to=110, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=240)
temp_scale_2.place(x=1111, y=130)
temp_scale_2.set(35)

temp_3 = tk.Label(window, text='Temp Sensor 3 (Celsius)',background='white', font=('Helvetica',16,'bold'))
temp_3.place(x=850,y=195)
temp_scale_3 = tk.Scale(window, from_=0, to=110, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=240)
temp_scale_3.place(x=1111,y=190)
temp_scale_3.set(35)

# compound

# submit button
button = tk.Button(window, text="Submit", foreground="white", background="black",
                        width=25, font=('Helvetica',16), command=submit)
button.place(x=500,y=665)

window.mainloop()
