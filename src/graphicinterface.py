import os
import sys
import tkinter as tk
import subprocess
from tkinter import filedialog
import time

menu = tk.Tk()
menu.title("Image Compressor")
#Window dimensions
width = 300
height = 200
#Center
menu.geometry(f"{width}x{height}+{int(menu.winfo_screenwidth()/2 - width/2)}+{int(menu.winfo_screenheight()/2 - height/2)}")

#Variables to store the inputs
input_folder = ""
output_folder = ""
quality = ""

#Variables to check if values were introduced
b_input   = False
b_output  = False
b_quality = False

#Functions to do OnClick
def choose_input_folder():
    global input_folder, b_input
    input_folder = filedialog.askdirectory()
    b_input = True
def choose_output_folder():
    global output_folder, b_output
    output_folder = filedialog.askdirectory()
    b_output = True
def enter():
    global b_quality, quality
    if b_input == False:
        label_input.config(fg="red")
    else:
        label_input.config(fg="black")
    if b_output == False:
        label_output.config(fg="red")
    else:
        label_output.config(fg="black")
    quality = entry_quality.get()
    if not quality.isdigit() or int(quality) > 95:
        label_quality.config(fg="red")
        return
    else:
        label_quality.config(fg="black")
        b_quality = True
    if (b_input and b_output and b_quality):
        menu.destroy()

#Create widgets
label_input = tk.Label(menu, text="Input folder:")
label_output = tk.Label(menu, text="Output folder:")
label_quality = tk.Label(menu, text="Compression quality (0-95):")
button_input = tk.Button(menu, text="Choose folder", command=choose_input_folder)
button_output = tk.Button(menu, text="Choose folder", command=choose_output_folder)
entry_quality = tk.Entry(menu)
button_enter = tk.Button(menu, text="Compress", command=enter)
entry_quality.insert(0, "5")

#Pack widgets
label_input.pack()
button_input.pack()
label_output.pack()
button_output.pack()
label_quality.pack()
entry_quality.pack()
button_enter.pack()


menu.mainloop()

print("Input folder:", input_folder)
print("Output folder:", output_folder)
print("Quality:", quality)

exe_path = os.path.dirname(sys.executable)

if(b_input and b_output and b_quality):
    print("#####Running Script#####")
    if(os.path.exists("imagecompressor.py")):
        subprocess.call(["python3", "../imagecompressor.py", input_folder, output_folder, quality])
    elif(os.path.exists("./src/imagecompressor.py")):
        subprocess.call(["python3", "./src/imagecompressor.py", input_folder, output_folder, quality])
    else:
        print("Conversion failed. Script unreachable. Current path: ", exe_path)

        time.sleep(4)
else:
    print("#####ABORTED#####")
    
time.sleep(2)
print("Compression finished")