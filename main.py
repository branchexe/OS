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



#Right clicks on desktop
def RightClickPos(event):
    def RightWindowDestroy(event):
        RightWindow.destroy()
    Desktop.focus_set();
    #print("Clicked at" + str(event.x) + str(event.y))
    RightWindow = Toplevel(Desktop) #create new window
    RightWindowButton1 = Button(RightWindow, text="Color options").grid(row=0)
    RightWindowButton2 = Button(RightWindow, text="Other options").grid(row=1)
    
    RightWindow.overrideredirect(1) #get rid of min/max buttons
    #set position
    x = root.winfo_x()
    y = root.winfo_y()
    RightWindow.geometry("+%d+%d" % (x + event.x, y + event.y))
    Desktop.bind("<Button-1>", RightWindowDestroy) #Destory TopLevel


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
