# Image Compressor
Image Compressor is a versatile tool that can compress any type of image located within a specified folder. Here are some reasons why you should choose Image Compressor:
# Why should I choose Image Compressor?
##### Offline
This tool is available for use without an internet connection. We will never collect any data, meaning that your files are safe and secure. You can use this tool to compress private files without any worries!

##### Limitless
You can compress as many files as you need to, and there is no speed limit to the compression process! The speed of compression is entirely dependent on your computer's specifications.

##### Multi-Extension
Don't worry about the file extension (jpg, jpeg, png, etc.). Image Compressor can compress any combination of formats without need for additional specifications!

##### Easy to use and practical
Simply specify the folder where your files are located and the folder where you want to save the compressed images. You don't have to select each file individually. Additionally, the program offers two support options: console and graphical, making it perfect for both programmers and everyday users.

#### Free
Image Compressor is completely free to use, so you don't have to spend any money on image compression software. Despite being free, it delivers high-quality image compression and fast results, so you can compress your images quickly and efficiently!

# Operating modes

## Graphical Interface (User Friendly)

### Installation Guide
#### Windows
Download the latest release executable of Image Compressor from 
https://github.com/CrashyProjects/ImageCompressor-AnyFileExtension-Console-GraphicInterface/releases/tag/v1.0

Double click on the "ImageCompressor.exe" executable file to run Image Compressor.

#### Linux
Download the latest release executable of Image Compressor from 
https://github.com/CrashyProjects/ImageCompressor-AnyFileExtension-Console-GraphicInterface/releases/tag/v1.0

Run it with the following command:
   ```
    sudo ./ImageCompressor
   ```

### Usage
To use the Image Compressor tool, follow these steps:
1. Run "ImageCompressor.exe" to open the main menu:

   ![Main menu](/docs/menu.png)

2. Click on the "Select Folder" button to choose the folder containing the images you want to compress. You can check the currently selected directory at the bottom of the latest dropdown menu:

   ![Selected path](/docs/selected.png)

3. After selecting the folder, click on the "Compress" button to begin the compression process.
4. Once the compression is complete, the tool will automatically close after 2 seconds.
 
## Console (Advanced User)
### Requirements
-   Python 3.x
-   PIL Library

### Usage
`python3 imagecompressor.py "/input_folder" "/output_folder" [QualityFactor (0:95)]` 

Note: Make sure to enclose the folder paths in double quotes ("path") and use forward slashes (/) for folder paths.

#### Parameters
-   `input_folder`: The folder containing the images that need to be compressed.
-   `output_folder`: The folder where the compressed images will be saved.
-   `QualityFactor (optional)`: An integer value from 0 (worst quality) to 95 (best quality) that determines the level of compression to apply. If not specified, the default value of 5 will be used.
#### Example

Suppose you have a folder named `/home/USER/ImageCompressor/test/input` that contains several images you want to compress, and you want to save the compressed images to a folder named `/home/USER/ImageCompressor/test/output`. You want to use a quality factor of 30 for the compression.

1. Open a terminal or command prompt in the directory where the script is located.
2. Run the following command:

    ```
    python3 imagecompressor.py "/home/USER/ImageCompressor/test/input" "/home/USER/ImageCompressor/test/output" 30
    ```
  
    Alternatively, if you are already located in the "/home/USER/ImageCompressor/" directory, you can run the following command (not recommended*):

    ```
    python3 imagecompressor.py "/test/input" "/test/output" 30
    ```
  
    *Note: If the **output folder** doesn't exist, it will be **created without the pwd**.

The script will compress all the images in the `/home/USER/ImageCompressor/test/input` folder and save the compressed images to the `/home/USER/ImageCompressor/test/output` folder, using a quality factor of 30. Once the compression is complete, a message will be displayed indicating that the process is completed.

## Build (Advanced User) [Not necessary]
### Requirements
-   Python 3.x
-   PIL Library
-   Pyinstaller
### Before you build
Note that there are pre-built versions available for Windows and Linux (tested on Debian) in the "Releases" section. If you prefer to build the application yourself, follow the steps below.
### How to build [Option 1 - Using megerd.py] [Recommended]
1. Open a terminal and navigate to the main folder of the project.
2. Run the following command:
3. Once the compression is complete, the tool will automatically close after 2 seconds.
    ```
    pyinstaller --onefile --name=ImageCompressor ./src/megerd.py
    ```
3. To execute:
- On Linux:

    ```
    sudo ./dist/ImageCompressor
    ```
- On windows:

    Navigate to the "dist" folder and double-click on ImageCompressor.exe
    
### How to build [Option 2 - Using graphicinterface.py and imagecompressor.py]
1. Open a terminal and navigate to the main folder of the project.
2. Run the following command to create the build, dist, and .spec files:

    ```
    pyinstaller --onefile --name=ImageCompressor ./src/graphicinterface.py
    ```
3. Modify the "ImageCompressor.spec" file with the following contents (just replace a):

    ```
    a = Analysis(['./src/graphicinterface.py'],
             pathex=['./src'],
             binaries=[],
             datas=[('./src/imagecompressor.py', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=None,
             noarchive=False)
    ```

4. Run the following command to build the executable: 

    ```
    pyinstaller ImageCompressor.spec
    ```

5. To execute on Linux just do:

    ```
    sudo ./dist/ImageCompressor
    ```
## FAQ
- Does this program copy empty (0 bit) images?

  No, empty images are not copied.
- What image formats are supported by ImageCompressor?

  ImageCompressor supports the same image formats as the Pillow library, which includes popular formats such as JPEG, PNG, BMP, GIF, and TIFF, among others.
## Authors
CrashyProjects
## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
