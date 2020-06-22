from tkinter import *
from time import *
from functools import partial;

#gets current time and updates display
def displayTime():
    currentTime = strftime("%I:%M:%S")
    currentDate = strftime("%m/%d/%Y")
    timeLabel.config(text=currentTime + "  " + currentDate, padx=5)
    root.after(200,displayTime) #set timer to redo function


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

    #Desktop Color Change Menu
    def ChangeDesktopColor():
        def DesktopColorDestroy(event):
            DesktopColorOptionMenu.destroy();
        RightWindowDestroy(event) #get rid of rightclick window
        DesktopColorOptionMenu = Toplevel(root);
        DesktopColorOptionMenu.overrideredirect(1) #get rid of min/max buttons

        DesktopRedButton = Button(DesktopColorOptionMenu, text="Red", bg="Red", fg="white", padx=20,pady=20, command=partial(DesktopColorRed, DesktopColorOptionMenu)).grid(row=0, column=0);
        DesktopGreenButton = Button(DesktopColorOptionMenu, text="Green", bg="Green", fg="white", padx=20,pady=20, command=partial(DesktopColorGreen, DesktopColorOptionMenu)).grid(row=0, column=1);
        DesktopBlueButton = Button(DesktopColorOptionMenu, text="Blue", bg="Blue", fg="white", padx=20,pady=20, command=partial(DesktopColorBlue, DesktopColorOptionMenu)).grid(row=0, column=2);
        DesktopYellowButton = Button(DesktopColorOptionMenu, text="yellow", bg="yellow", fg="black", padx=20,pady=20, command=partial(DesktopColorYellow, DesktopColorOptionMenu)).grid(row=1, column=0);
        DesktopPurpleButton = Button(DesktopColorOptionMenu, text="purple", bg="purple", fg="white", padx=20,pady=20, command=partial(DesktopColorPurple, DesktopColorOptionMenu)).grid(row=1, column=1);
        DesktopOrangeButton = Button(DesktopColorOptionMenu, text="orange", bg="orange", fg="white", padx=20,pady=20, command=partial(DesktopColorOrange, DesktopColorOptionMenu)).grid(row=1, column=2);

        #position
        x = root.winfo_x()
        y = root.winfo_y()
        DesktopColorOptionMenu.geometry("+%d+%d" % (x+50, y+50))
        Desktop.bind("<Button-1>", DesktopColorDestroy)


        #desktop color change
    def DesktopColorRed(ColorMenu):
        Desktop.config(bg="red")
        ColorMenu.destroy()
    def DesktopColorGreen(ColorMenu):
        Desktop.config(bg="green")
        ColorMenu.destroy()
    def DesktopColorBlue(ColorMenu):
        Desktop.config(bg="blue")
        ColorMenu.destroy()
    def DesktopColorYellow(ColorMenu):
        Desktop.config(bg="yellow")
        ColorMenu.destroy()
    def DesktopColorPurple(ColorMenu):
        Desktop.config(bg="purple")
        ColorMenu.destroy()
    def DesktopColorOrange(ColorMenu):
        Desktop.config(bg="orange")
        ColorMenu.destroy()
    
    #destroys the right window after use
    def RightWindowDestroy(event):
        RightWindow.destroy()

    #Main Right Window
    RightWindow = Toplevel(Desktop) #create new window
    
    Desktop.focus_set();
    RightWindowButton1 = Button(RightWindow, text="Color options", command=ChangeDesktopColor).grid(row=0)
    RightWindowButton2 = Button(RightWindow, text="Other options").grid(row=1)    
    RightWindow.overrideredirect(1) #get rid of min/max buttons
    #set position
    x = root.winfo_x()
    y = root.winfo_y()
    RightWindow.geometry("+%d+%d" % (x + event.x, y + event.y))
     #Destory TopLevel on leftclick
    #RightWindow.bind('<Leave>', RightWindowDestroy);


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
FilesButton = Button(toolbar, text="Files", borderwidth=0);
FilesButton.pack(side=LEFT, padx=4,pady=2);
OtherButton = Button(toolbar, text="Button", borderwidth=0);
OtherButton.pack(side=LEFT, padx=4,pady=2);


#display toolbar
time.pack(side=RIGHT, fill=Y)
toolbar.pack(side=BOTTOM, fill=X);


#keep window running
root.mainloop()
