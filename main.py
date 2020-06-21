from tkinter import *
#       ~~~~~~~~~~~~~~~setup stuff~~~~~~~~~~~~~~~
root = Tk(); #create window


#create window size
root.geometry("512x512")

#name window
root.title("NathOS");

#set bgcolor
root.configure(bg="#0059b3")


#       ~~~~~~~~~~~~~~~toolbar~~~~~~~~~~~~~~~
toolbar = Frame(root, bg="red", height=25);
time = Frame(toolbar, bg="green", width=100, height=25);

#button placeholders

photo = PhotoImage(file=r"C:\Users\rnbra\Desktop\OS\icom.png")
insertButt = Button(toolbar, text="Insert Image", image=photo, height=20, width=20)
insertButt.pack(side=LEFT, padx=2,pady=2);
iButt = Button(toolbar, text="Insert Image")
iButt.pack(side=LEFT, padx=2,pady=2);


#display toolbar
time.pack(side=RIGHT)
toolbar.pack(side=BOTTOM, fill=X);


#keep window running
root.mainloop()
