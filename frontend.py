from tkinter import *
import backend
interface = Tk()
interface.wm_title('CarInventory.sentas')

def selection(event):
   try:  
    global selected
    index=carlist.curselection()[0]
    selected=carlist.get(index)
    Entry1.delete(0,END)
    Entry1.insert(END,selected[1])
    Entry2.delete(0,END)
    Entry2.insert(END,selected[2])
    Entry3.delete(0,END)
    Entry3.insert(END,selected[3])
    Entry4.delete(0,END)
    Entry4.insert(END,selected[4])

   except IndexError:
     pass
 

def viewall_command():
   carlist.delete(0,END)
   for row in backend.view():
       carlist.insert(END,row)


def search_command():
   carlist.delete(0,END)
   for row in backend.search(cartype_var.get(),year_var.get(),price_var.get(),vin_var.get()):
      carlist.insert(END,row)

def insert_command():
   backend.insert(cartype_var.get(),year_var.get(),price_var.get(),vin_var.get())
   carlist.insert(END,(cartype_var.get(),year_var.get(),price_var.get(),vin_var.get()))

def delete_command():

   backend.delete(selected[0])

def update_command():

   backend.update(selected[0],cartype_var.get(),year_var.get(),price_var.get(),vin_var.get())


label1=Label(interface, text= "Car type:")
label1.grid(row=0, column=0)
   
label2=Label(interface, text= "Year:")
label2.grid(row=1, column=0)

label3=Label(interface, text= "Price:")
label3.grid(row=0, column=2)

label4=Label(interface, text= "VIN:")
label4.grid(row=1, column=2)

Viewall=Button(interface, text='View all',width=12,command=viewall_command)
Viewall.grid(row=2 , column=3, columnspan=2,sticky=W)

search=Button(interface, text='Search car',width=12,command=search_command)
search.grid(row=3 , column=3, columnspan=2,sticky=W)

add_car=Button(interface, text='Add car',width=12, command=insert_command)
add_car.grid(row=4 , column=3, columnspan=2,sticky=W)

update=Button(interface, text='Update selected',width=12, command=update_command)
update.grid(row=5 , column=3, columnspan=2,sticky=W)

delete=Button(interface, text='Delete selection',width=12,command=delete_command)
delete.grid(row=6 , column=3, columnspan=2,sticky=W)

close=Button(interface, text='Close',width=12, command=interface.destroy)
close.grid(row=7 , column=3, columnspan=2,sticky=W)


cartype_var=StringVar()
Entry1 = Entry(interface,textvariable=cartype_var)
Entry1.grid(row = 0 , column=1)

year_var=StringVar()
Entry2 = Entry(interface,textvariable=year_var)
Entry2.grid(row = 1 , column=1)

price_var=StringVar()
Entry3 = Entry(interface,textvariable=price_var)
Entry3.grid(row = 0 , column=3)

vin_var=StringVar()
Entry4 = Entry(interface,textvariable=vin_var)
Entry4.grid(row = 1 , column=3)

carlist = Listbox(interface, height=6 , width=35)
carlist.grid(row= 1, column=0 , rowspan=6,columnspan=2)
carlist.bind('<<ListboxSelect>>',selection)

sb=Scrollbar(interface)
sb.grid(row=2,column=2,rowspan=6,columnspan=1)

carlist.configure(yscrollcommand=sb.set)
sb.configure(command=carlist.yview)


interface.mainloop()