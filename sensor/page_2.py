path_to_img = 'transformer.jpg'
defalt_id =  42
size_img = (300,200)
res = (1440,900)
pad_x = 10
pad_y = 5
ip = '172.16.15.225:5000'
server_ip = f'http://{ip}/update-transformers'


def submit_2():
    pass

root_p2 = tk.Tk()
root_p2.title("Virtual Sensors - Demo")
root_p2.geometry(f'{res[0]}x{res[1]}')
root_p2.configure(background='white')

title = tk.Label(root_p2, text=f'Oil Quality',background='white', font=('Helvetica',24))
title.place(x=525,y=pad_y)
im = Image.open(path_to_img)
im = im.resize(size_img)
img = ImageTk.PhotoImage(im)
panel = tk.Label(root_p2, image = img, borderwidth=2, relief="solid")
panel.place(x=500,y=50)

moisture = tk.Label(root_p2, text='Moisture (ppm)',background='white', font=('Helvetica',16))
moisture.place(x=10,y=25)
scale_moisture = tk.Scale(root_p2, from_=0, to=30, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=300)
scale_moisture.place(x=160,y=20)
scale_moisture.set(50)

power = tk.Label(root_p2, text='Power Factor',background='white', font=('Helvetica',16))
power.place(x=10,y=150)
scale_power = tk.Scale(root_p2, from_=0, to=100, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=300)
scale_power.place(x=160,y=145)
scale_power.set(50)

acidity = tk.Label(root_p2, text='Acidity ( mgKOH/g )',background='white', font=('Helvetica',16))
acidity.place(x=850,y=25)
scale_acidity = tk.Scale(root_p2, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=300)
scale_acidity.place(x=1050,y=20)
scale_acidity.set(0.01)

if_tension = tk.Label(root_p2, text='Interfacial Tension',background='white', font=('Helvetica',16))
if_tension.place(x=850,y=150)
scale_if_tension = tk.Scale(root_p2, from_=0, to=100, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=300)
scale_if_tension.place(x=1050,y=145)
scale_if_tension.set(50)

pcb_tension = tk.Label(root_p2, text='PCB concentration',background='white', font=('Helvetica',16))
pcb_tension.place(x=850,y=265)
pcb_tension_2 = tk.Label(root_p2, text='(ppm by weight)',background='white', font=('Helvetica',16))
pcb_tension_2.place(x=850,y=295)
scale_pcb_tension = tk.Scale(root_p2, from_=0, to=60, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=300)
scale_pcb_tension.place(x=1050,y=260)
scale_pcb_tension.set(3)

metal = tk.Label(root_p2, text='Dissolved Metals',background='white', font=('Helvetica',16))
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

furan = tk.Label(root_p2, text='Furfuraldehyde (DP)',background='white', font=('Helvetica',16))
furan.place(x=20,y=550)
scale_furan = tk.Scale(root_p2, from_=200, to=1000, orient=tk.HORIZONTAL, background='gray',
                    width=20, length=300)
scale_furan.place(x=260,y=540)
scale_furan.set(50)

# submit button
button = tk.Button(root_p2, text="Submit", foreground="white", background="black",
                        width=25, font=('Helvetica',16), command=submit)
button.place(x=500,y=665)

#root_p2.mainloop()
