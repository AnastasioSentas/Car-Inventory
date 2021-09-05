from tkinter import *

interface = Tk()

def Kg_Converter():
   Kg= E1.get()
   Pounds_Convert = float(Kg) * 2.20462
   grams_Convert = float(Kg) * 1000
   ounces_convert = float(Kg) * 35.274
   pounds.delete('1.0',END)
   pounds.insert(END, Pounds_Convert)
   grams.delete('1.0',END)
   grams.insert(END, grams_Convert)
   ounces.delete('1.0',END)
   ounces.insert(END, ounces_convert)

label1=Label(interface, text= "Car type:")
label1.grid(row=0, column=0)
   
label2=Label(interface, text= "Year:")
label2.grid(row=1, column=0)

label3=Label(interface, text= "Price:")
label3.grid(row=0, column=2)

label4=Label(interface, text= "VIN:")
label4.grid(row=1, column=2)

Viewall=Button(interface, text='View all',width=12)
Viewall.grid(row=2 , column=3, columnspan=2,sticky=W)

search=Button(interface, text='Search car',width=12)
search.grid(row=3 , column=3, columnspan=2,sticky=W)

add_car=Button(interface, text='Add car',width=12)
add_car.grid(row=4 , column=3, columnspan=2,sticky=W)

update=Button(interface, text='Update',width=12)
update.grid(row=5 , column=3, columnspan=2,sticky=W)

delete=Button(interface, text='delete',width=12)
delete.grid(row=6 , column=3, columnspan=2,sticky=W)

close=Button(interface, text='Close',width=12)
close.grid(row=7 , column=3, columnspan=2,sticky=W)

Entry1 = Entry(interface)
Entry1.grid(row = 0 , column=1)

Entry2 = Entry(interface)
Entry2.grid(row = 1 , column=1)

Entry3 = Entry(interface)
Entry3.grid(row = 0 , column=3)

Entry4 = Entry(interface)
Entry4.grid(row = 1 , column=3)

carlist = Listbox(interface, height=6 , width=35)
carlist.grid(row= 1, column=0 , rowspan=6,columnspan=2)

sb=Scrollbar(interface)
sb.grid(row=2,column=2,rowspan=6,columnspan=1)

carlist.configure(yscrollcommand=sb.set)
sb.configure(command=carlist.yview)


interface.mainloop()