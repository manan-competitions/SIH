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
ip = '172.16.15.225:5000'
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
    data['h2_conc'] = str(scale_h2_conc.get())
    data['ch4_conc'] = str(scale_ch4_conc.get())
    data['c2h2_conc'] = str(scale_c2h2_conc.get())
    data['c2h4_conc'] = str(scale_c2h4_conc.get())
    data['c0_conc'] = str(scale_c0_conc.get())
    data['c02_conc'] = str(scale_c02_conc.get())


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
# im = Image.open(path_to_img)
# im = im.resize(size_img)
# img = ImageTk.PhotoImage(im)
# panel = tk.Label(window, image = img, borderwidth=2, relief="solid")
# panel.place(x=500,y=50)

# power
power_main = tk.Label(window, text='Dissolved Concentration (ppm)',background='white', font=('Helvetica',16,'bold'))
power_main.place(x=pad_x,y=400)
power_p1 = tk.Label(window, text='Hydrogen',background='white', font=('Helvetica',16))
power_p1.place(x=400,y=350)
power_p2 = tk.Label(window, text='Methane',background='white', font=('Helvetica',16))
power_p2.place(x=700,y=350)
power_p3 = tk.Label(window, text='Acetylene',background='white', font=('Helvetica',16))
power_p3.place(x=1000,y=350)

scale_h2_conc = tk.Scale(window, from_=100, to=1000, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=200)
scale_h2_conc.place(x=350,y=400)
scale_h2_conc.set(100)

scale_ch4_conc = tk.Scale(window, from_=20, to=80, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=200)
scale_ch4_conc.place(x=650,y=400)
scale_ch4_conc.set(100)

scale_c2h2_conc = tk.Scale(window, from_=10, to=70, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=200)
scale_c2h2_conc.place(x=950,y=400)
scale_c2h2_conc.set(100)

# voltage
diff = 150
gas1 = tk.Label(window, text='Ethylene',background='white', font=('Helvetica',16))
gas1.place(x=400,y=350+diff)
gas2 = tk.Label(window, text='CarbonMonoxide',background='white', font=('Helvetica',16))
gas2.place(x=680,y=350+diff)
gas3 = tk.Label(window, text='CarbonDioxide',background='white', font=('Helvetica',16))
gas3.place(x=980,y=350+diff)

scale_c2h4_conc = tk.Scale(window, from_=15, to=150, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=200)
scale_c2h4_conc.place(x=350,y=400+diff)
scale_c2h4_conc.set(15)

scale_c0_conc = tk.Scale(window, from_=400, to=1000, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=200)
scale_c0_conc.place(x=650,y=400+diff)
scale_c0_conc.set(15)

scale_c02_conc = tk.Scale(window, from_=9000, to=15000, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=200)
scale_c02_conc.place(x=950,y=400+diff)
scale_c02_conc.set(15)








# submit button
button = tk.Button(window, text="Submit", foreground="white", background="black",
                        width=25, font=('Helvetica',16), command=submit)
button.place(x=500,y=665)

window.mainloop()
