from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
from tkinter import filedialog
import tkinter as tk
import os


def add_icon():
    global root
    image_icon = PhotoImage(file="images\\logo.png")
    root.iconphoto(False, image_icon)


def set_xy(work):
    global current_x, current_y
    current_x =work.x
    current_y= work.y


def addline(work):
    global current_x, current_y, canvas
    canvas.create_line((current_x, current_y, work.x, work.y),
        width=get_current_value(),fill=color, capstyle=ROUND, smooth=True)
    set_xy(work)


def show_color(new_color):
    global color
    color = new_color


def new_canvas():
    global canvas
    canvas.delete('all')
    display_pallete()


def display_pallete():
    global colors
    id = colors.create_rectangle((10,10,30,30),fill="black")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('black'))
    id = colors.create_rectangle((10,40,30,60),fill="brown4")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('brown4'))
    id = colors.create_rectangle((10,70,30,90),fill="red")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('red'))
    id = colors.create_rectangle((10,100,30,120),fill="orange")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('orange'))
    id = colors.create_rectangle((10,130,30,150),fill="yellow")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('yellow'))
    id = colors.create_rectangle((10,160,30,180),fill="green")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('green'))
    id = colors.create_rectangle((10,190,30,210),fill="blue")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('blue'))
    id = colors.create_rectangle((10,220,30,240),fill="purple")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('purple'))
    id = colors.create_rectangle((10,250,30,270),fill="pink")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('pink'))
    id = colors.create_rectangle((10,280,30,300),fill="grey")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('grey'))


def get_current_value():
    global current_value
    return '{: .2f}'.format(current_value.get())


def slider_changed(event):
    global value_label
    value_label.configure(text=get_current_value())


def insert_image():
    global root, canvas, filename, f_img
    filename=filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetypes=(("PNG file","*.png"), ("All files", "new.txt")))
    f_img = tk.PhotoImage(file=filename)
    my_img = canvas.create_image(180,50,image = f_img)
    root.bind("<B3-Motion>", show_image)


def show_image(event):
    global f_img, filename, canvas
    f_img = tk.PhotoImage(file=filename)
    my_img = canvas.create_image(event.x, event.y,image = f_img)


def runWhiteBoard():
    global root
    root.mainloop()

anti_flash_white = "#f2f3f5"
root = Tk()
root.title("White Board")
root.geometry("1050x570+150+50")
root.config(bg=anti_flash_white)
root.resizable(False,False)
add_icon()

current_x = 0
current_y = 0
color = "black"

filename = ""
f_img = tk.PhotoImage()

# sidebar
color_box = PhotoImage(file="images\\color section.png")
Label(root, image=color_box, bg=anti_flash_white).place(x=10,y=10)
eraser = PhotoImage(file="images\\eraser.png")
Button(root,image=eraser,bg=anti_flash_white, command=new_canvas).place(x=30,y=400)
import_image = PhotoImage(file="images\\addimage.png")
Button(root,image=import_image,bg=anti_flash_white, command=insert_image).place(x=30,y=450)
colors=Canvas(root, bg="#fff",width=37,height=305,bd=0)
colors.place(x=30,y=60)
display_pallete()

#slider
current_value = tk.DoubleVar()
slider = ttk.Scale(root,from_=0,to=100,orient='horizontal',command=slider_changed,variable=current_value)
slider.place(x=30,y=530)

value_label = ttk.Label(root, text=get_current_value())
value_label.place(x=27,y=550)

#main screen
canvas = Canvas(root, width=930, height=500, background="white", cursor="hand2")
canvas.place(x=100, y=10)
canvas.bind('<Button-1>', set_xy)
canvas.bind('<B1-Motion>', addline)