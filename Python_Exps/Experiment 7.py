'''
Experiment 7 : Write a python program to implement GUI Application using Tkinter.
                Name : Khan Arshad Abdulla
                Roll No : 20CO24
                Academic Year : 2021-22
'''

from tkinter import *


def convert():
    ans = float(degree.get())
    fahrenheit.set((ans*9/5)+32)


root = Tk()
root.title("Degree To Fahrenheit Celsius")
root.geometry("800x500")
root.iconbitmap("download.ico")

fahrenheit = StringVar()
degree = StringVar()

mainframe = Frame(root)
mainframe.pack()

convert_frame = Frame(root, pady=50)
convert_frame.pack()

Label(mainframe, text="Temperature Converter ",
      font="consalas 36 bold", fg="#16bdcc").grid(row=0, column=1)

fahr = Label(convert_frame, text="Fahrenheit : ",
             font="consalas 18 bold", fg="red")
fahr.grid(row=3, column=1, padx=10, pady=10)

degree_entry = Entry(convert_frame, textvariable=degree)
degree_entry.grid(row=1, column=2)

Label(convert_frame, text="To", font="consalas 18 bold").grid(row=2, column=1)

degree_label = Label(convert_frame, text="Degree Celsius : ",
                     font="consalas 18 bold", fg="blue")
degree_label.grid(row=1, column=1, padx=10, pady=10)

fahr_label = Label(convert_frame, textvariable=fahrenheit)
fahr_label.grid(row=3, column=2, padx=10, pady=10)

Button(convert_frame, text="Convert", command=convert, font="consalas 18 bold", relief="raised",
       borderwidth=7, bg="green", fg="black").grid(row=4, columnspan=4, ipadx=10, ipady=10)

root.mainloop()

'''
CONCLUSION:
I have successfully created a Temperature Converter GUI using Tkinter. 

'''