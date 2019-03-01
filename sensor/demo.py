import tkinter
import requests
from PIL import ImageTk, Image

path_to_img = 'transformer.jpg'
id =  42
size_img = (300,200)
res = (1440,900)
pad_x = 10
pad_y = 5
sld_len = 700
server_ip = 'http://127.0.0.1:5000/update-transformers'

def submit():
    """
    Modify this function to control the behaviour of
    the Submit button
    """
    print('--------')
    print(s1.get())
    print(s2.get())
    print(s3.get())
    sens_data = {
                "t_id": id,
                "new_data": {
                            "current": s1.get(),
                            "temp": s2.get(),
                            "oil": s3.get(),
                            }
                }
    r = requests.post(server_ip,json=sens_data)
    print(r)

window = tkinter.Tk()
window.title("Virtual Sensors - Demo")
window.geometry(f'{res[0]}x{res[1]}')
window.configure(background='white')

title = tkinter.Label(window, text=f'Transformer #{id}',background='white', font=('Helvetica',24,'underline'))
title.place(x=525,y=pad_y)

im = Image.open(path_to_img)
im = im.resize(size_img)
img = ImageTk.PhotoImage(im)
panel = tkinter.Label(window, image = img, borderwidth=2, relief="solid")
panel.place(x=500,y=50)

# current
t1 = tkinter.Label(window, text='Current (mA)',background='white', font=('Helvetica',16,'bold'))
t1.place(x=pad_x,y=300)
s1 = tkinter.Scale(window, from_=0, to=200, orient=tkinter.HORIZONTAL, background='gray',
                    width=25, length=sld_len)
s1.place(x=400,y=285)

# Temperature
t2 = tkinter.Label(window, text='Temperature (Celsius)',background='white', font=('Helvetica',16,'bold'))
t2.place(x=pad_x,y=375)
s2 = tkinter.Scale(window, from_=0, to=200, orient=tkinter.HORIZONTAL, background='gray',
                    width=25, length=sld_len)
s2.place(x=400,y=360)

# Oil level
t3 = tkinter.Label(window, text='Oil level (m)',background='white', font=('Helvetica',16,'bold'))
t3.place(x=pad_x,y=450)
s3 = tkinter.Scale(window, from_=0, to=200, orient=tkinter.HORIZONTAL, background='gray',
                    width=25, length=sld_len)
s3.place(x=400,y=435)

# submit button
button = tkinter.Button(window, text="Submit", foreground="white", background="black",
                        width=50, font=('Helvetica',16), command=submit)
button.place(x=375,y=650)

window.mainloop()
