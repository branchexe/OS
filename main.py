from tkinter import *
from time import *

#gets current time and updates display
def displayTime():
    currentTime = strftime("%I:%M:%S")
    currentDate = strftime("%m/%d/%Y")
    timeLabel.config(text=currentTime + "  " + currentDate)
    root.after(200,displayTime)

#       ~~~~~~~~~~~~~~~setup stuff~~~~~~~~~~~~~~~
root = Tk(); #create window

#create window size
root.geometry("512x512")

#name window
root.title("NathOS");

#set bgcolor
root.configure(bg="yellow")


def RightClickPos(event):
    Desktop.focus_set();
    print("Clicked at" + str(event.x) + str(event.y))


#create desktop frame
Desktop = Frame(root, bg="#0059b3", width=512, height=512-25)
Desktop.bind("<Button-3>", RightClickPos) #call rightclick event
Desktop.pack()


#       ~~~~~~~~~~~~~~~toolbar~~~~~~~~~~~~~~~
toolbar = Frame(root, bg="#dedede", height=25);

#time
time = Frame(toolbar, bg="#dedede", width=150);
timeLabel = Label(time, text="time", bg="#dedede", fg="black")
timeLabel.pack(side=RIGHT, pady=5);
displayTime()



#button placeholders
insertButt = Button(toolbar, text="Insert Image", borderwidth=0)
insertButt.pack(side=LEFT, padx=2,pady=2);
iButt = Button(toolbar, text="Insert Image", borderwidth=0)
iButt.pack(side=LEFT, padx=2,pady=2);


#display toolbar
time.pack(side=RIGHT, fill=Y)
toolbar.pack(side=BOTTOM, fill=X);


#keep window running
root.mainloop()
