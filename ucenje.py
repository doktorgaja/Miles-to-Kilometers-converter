# TKINTER and GUI (Graphical user interface)

from tkinter import *

window = Tk()
# ovako pravimo window tj prozorcic naseg programa,
# pozivamo tkinter metodu i klasu Tk() da bismo napravili objekat
window.title("My First GUI program")
# menjanje naslova na prozoru
window.minsize(width=500, height=300)
# pocetna velicina ekrana tj prozora
window.config(padx=100, pady=200)
# padding dodat isto se radi i za vidget ne samo za window


# LABEL kreaicija
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# ovako kreiramo label na prozoru sa sve komandama za text, font, velicinu
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)
# my_label.place(x=100, y=200)
# my_label.pack()
# ovako postavaljamo label na prozor jer bez ovoga ne radi, stavlja ga na centar pri vrhu
# imamo expand za koriscenje ekrana i to je tip bool, imamo i side mozemo staviti bottom, top, left, right i on salje tekst u tom pravcu
my_label["text"] = "New text"
my_label.config(text="New text")
# ovako vrsimo izmene komponenti koje smo napravili

# BUTTON
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click me", command=button_clicked)
# kad radimo dugme kad pravimo command stavljamo ime funkcije a ne pozivamo je sa ()
# button.pack()
button.grid(column=1, row=1)
new_button = Button(text="Click me", command=button_clicked)
new_button.grid(column=2, row=0)
# ENTRY COMPONENT

input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)




window.mainloop()
# ovo je komanda za nas window, dozvoljava nam interakciju,
# bez da se zatvori na klik, i traje sve dok ga ne zatvorimo na X,
# uvek se nalazi na kraju programa koda.



# from tkinter import *
#
# #Creating a new window and configurations
# window = Tk()
# window.title("Widget Examples")
# window.minsize(width=500, height=500)
#
# #Labels
# label = Label(text="This is old text")
# label.config(text="This is new text")
# label.pack()
#
# #Buttons
# def action():
#     print("Do something")
#
# #calls action() when pressed
# button = Button(text="Click Me", command=action)
# button.pack()
#
# #Entries
# entry = Entry(width=30)
# #Add some text to begin with
# entry.insert(END, string="Some text to begin with.")
# #Gets text in entry
# print(entry.get())
# entry.pack()
#
# #Text
# text = Text(height=5, width=30)
# #Puts cursor in textbox.
# text.focus()
# #Adds some text to begin with.
# text.insert(END, "Example of multi-line text entry.")
# #Get's current value in textbox at line 1, character 0
# print(text.get("1.0", END))
# text.pack()
#
# #Spinbox
# def spinbox_used():
#     #gets the current value in spinbox.
#     print(spinbox.get())
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
# #Scale
# #Called with current scale value.
# def scale_used(value):
#     print(value)
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
# #Checkbutton
# def checkbutton_used():
#     #Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
# #variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()
#
# #Radiobutton
# def radio_used():
#     print(radio_state.get())
# #Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
#
# #Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#
# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
# window.mainloop()