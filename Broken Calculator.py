import sys
from tkinter import * #importing tkinter stuff

root = Tk() #Base of program
frame = Frame(root)
frame.pack()

root.title("Calculator")

num1=StringVar()

topframe = Frame(root)
topframe.pack(side = TOP)

txtDisplay = Entry(frame,textvariable = num1, bd= 20, insertwidth = 1, font = 30)
txtDisplay.pack(side = TOP)

button1 = Button(topframe, padx = 16, pady = 16, bd = 8, text = "1", fg="black") #Defines first button, can copypaste for remaining buttons.
button1.pack(side = LEFT)
button2 = Button(topframe, padx = 16, pady = 16, bd = 8, text = "2", fg="black") #Defines second button.
button2.pack(side = LEFT)
button3 = Button(topframe, padx = 16, pady = 16, bd = 8, text = "3", fg="black") #Defines third button.
button3.pack(side = LEFT)
button4 = Button(topframe, padx = 16, pady = 16, bd = 8, text = "4", fg="black") #Defines fourth button.
button4.pack(side = LEFT)

frame1 = Frame(root) #Redifining next row
frame1.pack(side = TOP)

button1 = Button(frame1, padx = 16, pady = 16, bd = 8, text = "5", fg="black") #Defines fifth button
button1.pack(side = LEFT)
button2 = Button(frame1, padx = 16, pady = 16, bd = 8, text = "6", fg="black") #Defines sixth button
button2.pack(side = LEFT)
button3 = Button(frame1, padx = 16, pady = 16, bd = 8, text = "7", fg="black") #Defines seventh.
button3.pack(side = LEFT)
button4 = Button(frame1, padx = 16, pady = 16, bd = 8, text = "8", fg="black") #This is tiring, you should get the point by now.
button4.pack(side = LEFT)

#End of Frame 1
frame2 = Frame(root) #Redifining next row
frame2.pack(side = TOP)

button1 = Button(frame2, padx = 16, pady = 16, bd = 8, text = "9", fg="black")
button1.pack(side = LEFT)
button2 = Button(frame2, padx = 16, pady = 16, bd = 8, text = "0", fg="black")
button2.pack(side = LEFT)
button3 = Button(frame2, padx = 16, pady = 16, bd = 8, text = "C", fg="black")
button3.pack(side = LEFT)
button4 = Button(frame2, padx = 16, pady = 16, bd = 8, text = "-", fg="black") #This is negative, NOT subtraction
button4.pack(side = LEFT)

#End of Frame 2
frame3 = Frame(root) #Redifining next row
frame3.pack(side = TOP)

button1 = Button(frame3, padx = 16, pady = 16, bd = 8, text = "+", fg="black")
button1.pack(side = LEFT)
button2 = Button(frame3, padx = 16, pady = 16, bd = 8, text = "-", fg="black") #This is subtraction, not negative
button2.pack(side = LEFT)
button3 = Button(frame3, padx = 16, pady = 16, bd = 8, text = "*", fg="black")
button3.pack(side = LEFT)
button4 = Button(frame3, padx = 16, pady = 16, bd = 8, text = "/", fg="black")
button4.pack(side = LEFT)

root.mainloop()
