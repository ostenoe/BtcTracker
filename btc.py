import requests
import tkinter as tk
from datetime import datetime

def trackBitcoin():
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
    response = requests.get(url).json()  #Grabs btc data

    # updates label with Btc price in USD
    price_in_usd = response['USD']
    labelPrice.config(text=f"${price_in_usd} USD")

    # updates label with time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    labelTime.config(text=current_time)

    # refresh data every second
    canvas.after(600, trackBitcoin)

#makes tkinter window
canvas = tk.Tk()
canvas.geometry("400x500")
canvas.title("Bitcoin Tracker")

#ez acess fonts
f1 = ("Helvetica", 26, "bold")
f2 = ("Arial", 22, "bold")
f3 = ("Courier", 20, "normal")

#place widgets to the window
label = tk.Label(canvas, text="Bitcoin Price", font=f1)
label.pack(pady=20)

labelPrice = tk.Label(canvas, font=f2)
labelPrice.pack(pady=20)

labelTime = tk.Label(canvas, font=f3)
labelTime.pack(pady=20)


trackBitcoin()

#loops the page 
canvas.mainloop()