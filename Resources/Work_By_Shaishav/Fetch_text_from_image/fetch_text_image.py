# Jay Dada


import easyocr
import tkinter as tk
import pyperclip
import time

def fetch_text_from_image(cmd: str):
    from tkinter.filedialog import askopenfilename


    if 'fetch text from an image' in cmd or 'fetch text from image' in cmd or \
        "get text from an image" in cmd or  "get text from image" in cmd:
        root = tk.Tk()
        canvas1 = tk.Canvas(root, width=800, height=300)
        canvas1.pack()

        pathLabel = tk.Label(root, text="Path: ")
        canvas1.create_window(111, 120, window=pathLabel)
        entry1 = tk.Entry(root)
        canvas1.create_window(200, 120, window=entry1)

        def get_Path_and_fetch_text():
            img = entry1.get()
            reader = easyocr.Reader(['en'])

            results = reader.readtext(img)

            # print(results)
            text = ''

            for result in results:
                text += result[1] + ' '

            print(text)
            pyperclip.copy(text)
            w.insert(1.0, text)
            label1 = tk.Label(root, text="Text Has Been Copied To the Clipboard")
            canvas1.create_window(200, 260, window=label1)

        def select_a_file():
            filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
            print("Selcted File Is: " + filename)
            entry1.insert(0, filename)
            time.sleep(1)
            get_Path_and_fetch_text()

        w = tk.Text(root, height=15, width=50)
        canvas1.create_window(568, 140, window=w)

        button1 = tk.Button(text='Select File', command=select_a_file)
        canvas1.create_window(200, 160, window=button1)

        button2 = tk.Button(text='Enter the Path of Your Image with extension', command=get_Path_and_fetch_text)
        canvas1.create_window(200, 200, window=button2)


        root.mainloop()

fetch_text_from_image("fetch text from an image")

