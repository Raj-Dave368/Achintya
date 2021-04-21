from Crypto.Cipher import DES
from tkinter import *
import pyperclip as pc

root = Tk()
root.geometry("300x300")
root.title(" Store Information After Encryption ")


def Take_input():
    text = inputtxt.get("1.0", "end-1c")
    print(text)
    

    # text = b""
    cipher = DES.new(b'mycipher', DES.MODE_OFB)
    # enc_pass = cipher.encrypt(text)
    msg = cipher.encrypt(text.encode("utf8"))

    # print(msg)
    # print(msg)
    Output.config(text = "Encrypted Cipher: "+str(msg))

    cipher = DES.new(b'mycipher', DES.MODE_OFB)
    decrypt_pass = cipher.decrypt(msg)
    print(decrypt_pass)

    pc.copy('The text to be copied to the clipboard.')
    spam = pyperclip.paste()

# print('Encrypted message: '+enc_pass)


# l = Label(text="for Enryption text input")
# inputtxt = Text(root, height=10,
#                 width=25,
#                 bg="light yellow")

# Output = Text(root, height=5,
#               width=25,
#               bg="light cyan")

# Display = Button(root, height=2,
#                  width=20,
#                  text="Show",
#                  command=lambda: Take_input())

# l.pack()

# Output.pack()


inputtxt = Text(root, height=5,
                width=25,
                bg="light yellow")

Display = Button(root, height=2,
                 width=20,
                 text="Encrypt",
                 command=lambda: Take_input())

# my_entry = Entry(root,font=("Helvetica",20),bd=0,state="readonly",textvariable="")
# my_entry.pack(pady=20)

# w = Text(root, height=1, borderwidth=0)
# w.insert(1.0, "")
# w.pack()


Output = Label(root, height=5,
              width=25,
              bg="light cyan")
op = Label(root,height=2,width=5,text="")

Outputtext = Text(root,height=5,width=25,bg="Light yellow")
Displayop= Button(root,height=2,width=20,text="Decrypt",command=lambda: Take_input())

inputtxt.pack()
Display.pack()
Output.pack()
op.pack()
Outputtext.pack()
Displayop.pack()
mainloop()


# cipher = DES.new('mycipher')


# decrypt_pass = cipher.decrypt(enc_pass)

# print("Decrypted Message: "+decrypt_pass)
