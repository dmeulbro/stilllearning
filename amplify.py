"""
    Author:     Daniel Meulbroek
    Purpose:    Trying to animate a cool amplification process I saw in ECE 255
    Date:       2/15/2019

"""
from Tkinter import *

def get_params():  #STILL DON"T KNOW HOW TO CLOSE WINDOW AND KEEP DATA
    print vcc
    root.Destroy()

#create the window
root = Tk()

#modify root window
root.title("BJT Parameters")
root.geometry("500x400")

#initial setup and label
app = Frame(root)
app.grid()
label = Label(  app, 
                text = "Please enter in the following parameters:")
label.grid()

# Entries and entry labels
Label(app, text="V_cc").grid(row=1, sticky=W)
vcc = Entry(app)
vcc.grid(row=1,column=1)



# Enter and cancel buttons
button1 = Button(   app, 
                    text = "Enter",
                    command=get_params)
button1.grid(row=450, column=0)
button2 = Button(   app, 
                    text = "Cancel",
                    command=quit)
button2.grid(row=450, column=1)


#start the event loop
root.mainloop()
