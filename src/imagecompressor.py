from PIL import Image
import os
import sys

#Config
quality_param = 5


#Check correct syntaxys
num_args = len(sys.argv)
if(num_args < 3):
    print("Usage: python3 imagecompressor.py \"/folderInput\" \"/FolderOutput\" [QualityFactor (0:95)]")
    print("Warning: don't forget the \" and the / ")
    print("Result: the program will compress all the images contained in \"/folderInput\" and store the result in \"/FolderOutput\"\nQualityFactor is optional. It accpets values from 0 (worst) to 95 (best), if not specified, it will take the value ", quality_param)
    sys.exit(1)

in_folder  = sys.argv[1]
out_folder = sys.argv[2]

if (not os.path.isdir(in_folder) or not os.path.exists(in_folder)):
    print("WARNING: Directory: " + in_folder + " doesn't exist or is not a directory")
    in_folder = os.getcwd() + in_folder
    print("Using: " + in_folder)
    if (not os.path.isdir(in_folder) or not os.path.exists(in_folder)):
         print("ERROR: Directory: " + in_folder + " folder doesn't exist or is not a directory")
         sys.exit(1)       
if (not os.path.exists(out_folder)):
    print("WARNING: \"" + out_folder + "\" doesn't exist.")
    if (not os.path.exists(os.getcwd() + out_folder)):
        print("WARNING: \"" + os.getcwd() + out_folder + "\" doesn't exist. Creating folder...")      
        os.mkdir(out_folder)
        print("Created: " + out_folder)
    print("Using: " + in_folder)
    
if(num_args == 4):
    try:
        new_quality_param = int(sys.argv[3])
    except ValueError:
        print("ERROR: \"",sys.argv[3], "\" is not a number or an integer!")
        sys.exit(1)
    if(new_quality_param > 95 or new_quality_param < 0):
        print("QualityFactor only accepts values in the range 0 (worst) to 95 (best)")
        sys.exit(1)
    else:
        quality_param = new_quality_param


#Conversion
print("Quality value set to: ", quality_param)

inFiles = os.listdir(in_folder)
for img in inFiles:
    in_path_img = in_folder   + "/" + img
    out_path_img = out_folder + "/" + img
    img = Image.open(in_path_img)
    img.save(out_path_img, optimize=True, quality=quality_param)

print("Compression completed")