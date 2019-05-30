from tkinter import *
from OOPversionBackend import Database

database=Database("books.db")


#A function that select the desired row to be deleted
def get_selected_row(event):
    try:

        global selected_tuple  # creating a global variable
        index=list1.curselection()[0]   #this grabs the id of the selected_tuple
        selected_tuple=list1.get(index)
        e1.delete(0,END) # this deletes any item of row at index 0 only
        e1.insert(END,selected_tuple[1]) #this insert item at index 1 of selected rows
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2]) #this insert item at index 2 of selected rows
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3]) #this insert item at index 3 of selected rows
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4]) #this insert item at index 4 of selected rows
    except IndexError:
        pass


#A function that triggers the view function from the database
def view_command():
    list1.delete(0,END)
    for row in database.view():
        list1.insert(END,row)

#A function that triggers the search function from the database
def search_command():
    list1.delete(0,END)
    for row in database.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

# A function that triggers the add function in the database
def add_command():
    database.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

# A function that delete the row from get_selected_row
def delete_command():
    database.delete(selected_tuple[0])

#A function that trigers that update function of the database and takes in inputs
def update_command():
    database.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())

#Everything comes into the window object
window=Tk()
window.wm_title("Book Store")

#Creating the label for our desktop app
l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

#Creating Entry boxes for the Labels
title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

#Creating a listbox to output our Entries
list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

#Creating the ui for scrollbar
sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

#Configuring the listbox to move in y direction
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

#creating an object that help to select a desired rows
list1.bind('<<ListboxSelect>>',get_selected_row)

#Creating ui for the buttons
b1=Button(window,text="View all",width=12,command=view_command)
b1.grid(row=2,column=3)

b1=Button(window,text="Search entry",width=12, command=search_command)
b1.grid(row=3,column=3)

b1=Button(window,text="Add entry",width=12,command=add_command)
b1.grid(row=4,column=3)

b1=Button(window,text="Update selected",width=12, command=update_command)
b1.grid(row=5,column=3)

b1=Button(window,text="Delete selected",width=12, command=delete_command)
b1.grid(row=6,column=3)

b1=Button(window,text="Close",width=12, command=window.destroy)
b1.grid(row=7,column=3)


window=mainloop()
