import tkinter as tk
from tkinter import *
import tkinter.messagebox
import trends



# GUI
root = tk.Tk()

root.title("Currency converter")

Tops = Frame(root, bg='#42adf5', pady=2, width=1850, height=100, relief="ridge")
Tops.grid(row=0, column=5)

headlabel = tk.Label(Tops, font=('red', 19, 'bold'), text='Currency converter ',
                     bg='#42adf5', fg='black')
##42adf5
headlabel.grid(row=1, column=0, sticky=W)

variable1 = tk.StringVar(root)
variable2 = tk.StringVar(root)

variable1.set(" CURRENCY ")
variable2.set(" CURRENCY ")



# Function To For Real Time Currency Conversion

def RealTimeCurrencyConversion():
    from forex_python.converter import CurrencyRates

    c = CurrencyRates()

    from_currency = variable1.get()
    to_currency = variable2.get()

    if (Amount1_field.get() == ""):
        tkinter.messagebox.showinfo("Error !!", "Amount Not Entered.\n Please a valid amount.")

    elif (from_currency == "currency" or to_currency == "currency"):
        tkinter.messagebox.showinfo("Error !!",
                                    "Currency Not Selected.\n Please select FROM and TO Currency form menu.")

    else:
        new_amt = c.convert(from_currency, to_currency, float(Amount1_field.get()))
        new_amount = float("{:.4f}".format(new_amt))
        Amount2_field.insert(0, str(new_amount))


# clearing all the data entered by the user
def clear_all():
    Amount1_field.delete(0, tk.END)
    Amount2_field.delete(0, tk.END)


CurrenyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR"]

##42adf5
root.configure(background='#42adf5')
root.geometry("700x400")

Label_1 = Label(root, font=('lato black', 27, 'bold'), text="", padx=2, pady=2, bg="#42adf5", fg="black")
Label_1.grid(row=1, column=0, sticky=W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    Amount  :  ", bg="#42adf5", fg="black")
label1.grid(row=2, column=0, sticky=W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    From Currency  :  ", bg="#42adf5", fg="black")
label1.grid(row=3, column=0, sticky=W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    To Currency  :  ", bg="#42adf5", fg="black")
label1.grid(row=4, column=0, sticky=W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    Converted Amount  :  ", bg="#42adf5", fg="black")
label1.grid(row=8, column=0, sticky=W)

Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#42adf5", fg="black")
Label_1.grid(row=5, column=11, sticky=W)

Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#42adf5", fg="black")
Label_1.grid(row=7, column=11, sticky=W)

FromCurrency_option = tk.OptionMenu(root, variable1, *CurrenyCode_list)
ToCurrency_option = tk.OptionMenu(root, variable2, *CurrenyCode_list)

# FromCurrency_option.grid(row=3, column=0, ipadx=45, sticky=E)
FromCurrency_option.grid(row=3, column=5, ipadx=45, sticky=E)
ToCurrency_option.grid(row=4, column=5, ipadx=45, sticky=E)

Amount1_field = tk.Entry(root)
Amount1_field.grid(row=2, column=0, sticky=E)
# Amount1_field.grid(row=2, column=0, ipadx=28, sticky=E)

Amount2_field = tk.Entry(root)
Amount2_field.grid(row=8, column=0, sticky=E)
# Amount2_field.grid(row=8, column=0, ipadx=31, sticky=E)

Label_9 = Button(root, font=('arial', 15, 'bold'), text="   Convert  ", padx=2, pady=2, bg="blue", fg="red",
                 command=RealTimeCurrencyConversion)
Label_9.grid(row=6, column=0)



Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#42adf5", fg="black")
Label_1.grid(row=9, column=0, sticky=W)

Label_9 = Button(root, font=('arial', 15, 'bold'), text="   Clear All  ", padx=2, pady=2, bg="lightblue", fg="red",
                 command=clear_all)
Label_9.grid(row=10, column=0)

def close():
   #win.destroy()
   root.quit()

# Create a Button to call close()
Label_10 = Button(root, font=('arial', 15, 'bold'), text="   Show Stats  ", padx=2, pady=2, bg="blue", fg="red",
                 command=close)
Label_10.grid(row=9, column=5)



root.mainloop()

root.mainloop()









# base currency or reference currency
base="USD"

# required currency for plot
out_curr="INR"

# exchange data from a date
start_date="2021-01-01"

# exchange data till a date
end_date="2021-03-04"



trends.trends()