from tkinter import *

def miles_to_kilometer():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    km_converted_label.config(text=f"{km}")

window = Tk()
window.minsize(width=400, height=400)
window.title("Mile to Km Converter")
window.config(pady=20, padx=20)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles", font="Arial")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to", font="Arial")
is_equal_to_label.grid(column=0, row=1)

km_converted_label = Label(text="0",font="Arial")
km_converted_label.grid(column=1, row=1)

km_label = Label(text="Km", font="Arial")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", font="Arial", command=miles_to_kilometer)
calculate_button.grid(column=1, row=2)


window.mainloop()
