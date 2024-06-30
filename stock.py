#Stock Quote Translator (need libraries of tkinter, pandas & data from very famous companies in the NASDAQ composite)
#Medium Sized Project
import pandas as pd
from tkinter import *
from tkinter import ttk

def translate_ticker(stck:str):
    with open("words.txt", "r") as stocks:
        sp = [i.strip(" ").split("|") for i in stocks]
        new_sp = pd.DataFrame(sp)
        new_sp.dropna(how="any")
        stock_symbols = [new_sp[0][i] for i in range(1, len(new_sp[0])-1)]
        stock_tickers = [new_sp[1][x] for x in range(1, len(new_sp[1])-1)]
        new_stocks = {stock_symbols[i]:stock_tickers[i] for i in range(len(stock_tickers))}
        return new_stocks[stck]
        stocks.close()
        #translation of stocks


tk = Tk() #initialization
tk.title("Stock Ticker Translator")
entry = Entry(tk, width=50, borderwidth=5)
entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

#full name initialization:
output_label = Label(tk, text="Full Name of the stock:")
output_label.grid(row=1, column=0, sticky=W)

#creation of the label and the result
res = Label(tk, text="", width=50)
res.grid(row=1, column=1, sticky=W)

#function when input changes
def entry_change(*args):
    ticker = entry.get().upper()
    stck_name = translate_ticker(ticker)
    res.config(text=stck_name)

#linking the function to the input field
entry_var = StringVar()
entry_var.trace_add("write", entry_change)
entry.config(textvariable=entry_var)


tk.mainloop()
