#Import the required Libraries
from tkinter import *
from tkinter import ttk
import Browse


#Create an instance of Tkinter frame
top = Tk()

#Set the geometry and other Configurations of Tkinter frame
top.title("Get YouTube Views")
top.geometry("500x200")
top.resizable(0,0)
top.configure(background="red")
top.iconbitmap('youtube.ico')

#Create a Function to validate Entry Widgets
def submit():
    try:
        link = str(e1.get())
        views = int(e2.get())
        #l3=Label(top,text="", background="red",fg="white",font="bold", width=200)
        #l3.place(x=20,y=100)
        Browse.getView(link,views)
        top.quit()
    except:
        
        top.quit()


#Initialize a Label to display the Link Input Text
l1 = Label(top,text="Here your link")
l1.place(x=10,y=10)

#Create an Entry widget to accept YouTube Link as Input
e1 = Entry(top,width=65)
e1.focus_set()
e1.place(x=100,y=10)

#Initialize a Label to display the Views Input Text
l2 = Label(top,text="Number of views")
l2.place(x=10,y=40)

#Create an Entry widget to accept number of views as Input
e2 = Entry(top,width=20)
e2.focus_set()
e2.place(x=110,y=40)

#Create a Button to validate Entry Widgets
btn = Button(top,text="Submit Now",command=submit).place(x=200, y=70)

top.mainloop()