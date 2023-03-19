import os
import sys
import time
import subprocess
import tkinter as tk
from PIL import Image
from tkinter import filedialog

#Config
quality_param = 5

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

    #Directory checks
    if (not os.path.isdir(input_folder) or not os.path.exists(input_folder)):
        print("WARNING: Directory: " + input_folder + " doesn't exist or is not a directory")
        input_folder = os.getcwd() + input_folder
        print("Using: " + input_folder)
        if (not os.path.isdir(input_folder) or not os.path.exists(input_folder)):
             print("ERROR: Directory: " + input_folder + " folder doesn't exist or is not a directory")
             sys.exit(1)       
    if (not os.path.exists(output_folder)):
        print("WARNING: \"" + output_folder + "\" doesn't exist.")
        if (not os.path.exists(os.getcwd() + output_folder)):
            print("WARNING: \"" + os.getcwd() + output_folder + "\" doesn't exist. Creating folder...")      
            os.mkdir(output_folder)
            print("Created: " + output_folder)
        print("Using: " + input_folder)

    #Conversion
    print("Quality value set to: ", quality)
    inFiles = os.listdir(input_folder)
    for img in inFiles:
        in_path_img = input_folder   + "/" + img
        out_path_img = output_folder + "/" + img
        try:
            img = Image.open(in_path_img)
            img.save(out_path_img, optimize=True, quality=quality)
        except Exception as e:
             print("An exception occurred: {}".format(e))
        
else:
    print("#####ABORTED#####")

time.sleep(2) #Let results be known
print("Compression completed")