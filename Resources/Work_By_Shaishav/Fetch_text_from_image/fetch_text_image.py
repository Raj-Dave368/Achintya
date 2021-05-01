# Jay Dada


import easyocr
import tkinter as tk
import pyperclip
import time
from tkinter.filedialog import askopenfilename
from Resources.UsedForBoth import text_to_speech

def fetch_text_from_image():
        root = tk.Tk()
        canvas1 = tk.Canvas(root, width=1368, height=568)
        canvas1.pack()

        pathLabel = tk.Label(root, text="Path: ")
        canvas1.create_window(86, 120, window=pathLabel)
        entry1 = tk.Entry(root)
        canvas1.create_window(236, 120, width=256, window=entry1)

        def select_a_file():
            filepath = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
            entry1.insert(0, filepath)
            print("Selcted File Is: " + filepath)

            img = filepath
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
            canvas1.create_window(220, 220, window=label1)

        w = tk.Text(root, height=20, width=68)
        canvas1.create_window(768, 236, window=w)

        button1 = tk.Button(text='Select File', command=select_a_file)
        canvas1.create_window(220, 168, window=button1)


        root.mainloop()

if __name__ == '__main__':
    fetch_text_from_image()

