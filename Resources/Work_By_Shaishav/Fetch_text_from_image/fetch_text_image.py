# Jay Dada


import easyocr
import tkinter as tk


def fetch_text_from_image(cmd: str):
    if 'fetch text from an image' in cmd or 'fetch text from image' in cmd or \
        "get text from an image" in cmd or  "get text from image" in cmd:
        root = tk.Tk()

        canvas1 = tk.Canvas(root, width=800, height=300)
        canvas1.pack()

        entry1 = tk.Entry(root)
        canvas1.create_window(200, 140, window=entry1)


        def get_Path_and_fetch_text():
            img = entry1.get()
            reader = easyocr.Reader(['en'])

            results = reader.readtext(img)

            # print(results)
            text = ''

            for result in results:
                text += result[1] + ' '

            print(text)
            label1 = tk.Label(root, text=text)
            canvas1.create_window(200, 230, window=label1)


        button1 = tk.Button(text='Enter the Path of Your Image with extension', command=get_Path_and_fetch_text)
        canvas1.create_window(200, 180, window=button1)

        root.mainloop()


fetch_text_from_image("fetch text from an image")

