import tkinter as tk
from datetime import timedelta
from PIL import Image, ImageTk
import os

total_time = timedelta()

started = False

def countdown_timer():
    global total_time

    if total_time.total_seconds() > 0:
        hours, remainder = divmod(total_time.total_seconds(), 3600)
        minutes, seconds = divmod(remainder, 60)

        timer.config(text=f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}")

        total_time -= timedelta(seconds=1)

        root.after(1000, countdown_timer)
    else:
        timer.config(text="--:--:--")
        start.config(text="START")
        os.system('notify-send -a timey "time\'s up!"')

def handle_timer():
    global total_time
    global time_vars
    global started


    total_time = timedelta(hours=int(time_vars[0].get()),
                           minutes=int(time_vars[1].get()),
                           seconds=int(time_vars[2].get()))

    if total_time.total_seconds() > 0:
        started = not started

    if started == True:
        start.config(text="STOP")
        countdown_timer()
    else:
        total_time = timedelta(0)
        timer.config(text="--:--:--")
        start.config(text="START")

def incr(text_var):
    current_value = int(text_var.get())

    if current_value != 59:
        text_var.set(f"{current_value + 1:02d}")
    else:
        text_var.set("00")

def decr(text_var):
    current_value = int(text_var.get())

    if current_value != 0:
        text_var.set(f"{current_value - 1:02d}")
    else:
        text_var.set("59")

##################################################

def create_inner_box(parent, text_var):
    inner_frame = tk.Frame(parent, borderwidth=2)
    inner_frame.configure(bg="black")
    inner_frame.pack(fill="both", expand=True, side=tk.LEFT)

    plus_button = tk.Button(inner_frame, text="🞁",
                            command=lambda: incr(text_var),
                             bg="black", fg="gray", borderwidth=0, highlightthickness=0, font=("Barlow Condensed", 25))
    plus_button.pack(side="top")

    label = tk.Label(inner_frame, textvariable=text_var, font=("Barlow Condensed", 30), bg="black", fg="gray")
    label.pack()

    minus_button = tk.Button(inner_frame, text="🞃",
                             command=lambda: decr(text_var),
                             bg="black", fg="gray", borderwidth=0, highlightthickness=0, font=("Barlow Condensed", 25))
    minus_button.pack(side="bottom")

###################################################

root = tk.Tk()
root.title("Tempo")
root.wm_geometry('1200x700')
root.configure(bg="black")

time_vars = [tk.StringVar() for _ in range(3)]

time_vars[0].set("00")
time_vars[1].set("00")
time_vars[2].set("00")

main_frame = tk.Frame(root)
main_frame.configure(bg="black")
main_frame.pack(padx=0, pady=(0, 10), fill="both", expand=True)

image = Image.open(os.path.dirname(__file__) + "/" + "ol.png")
photo = ImageTk.PhotoImage(image)

image_label = tk.Label(main_frame, image=photo, borderwidth=0, relief='flat')
image_label.image = photo

image_label.place(relx=1.0, rely=0.0, anchor='ne')

timer = tk.Label(main_frame, text="--:--:--",
               font=("Barlow Condensed", 80), bg="black", fg="gray")
timer.place(relx=0.5, rely=0.5, anchor='center')

start = tk.Button(main_frame, text="START", bg="black", fg="gray",
                  font=("Barlow Condensed", 18),
                  command=handle_timer)
start.config(highlightbackground="black", highlightcolor="black")
start.pack(side="bottom")

inner_boxes_frame = tk.Frame(main_frame)
inner_boxes_frame.configure(bg="black")
inner_boxes_frame.pack(side="bottom", anchor="center")

for i in range(3):
    create_inner_box(inner_boxes_frame, time_vars[i])

root.mainloop()
