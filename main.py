import tkinter as tk
import requests

api_key = "API KEY"
link = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

def get_exchange_rate(base_currency, target_currency):
    """
    Retrieves the exchange rate that converts from base_currency to target_currency.
    """
    response = requests.get(link + base_currency.upper())
    data = response.json()

    if response.status_code == 200 and "conversion_rates" in data:
        return data["conversion_rates"][target_currency.upper()]
    else:
        print("Failed to retrieve exchange rates")
        return None

def convert():
    """
    Reads user input, fetches exchange rate, and updates the result label with the converted amount.
    """
    base_currency = currency_entry.get().upper()
    target_currency = new_currency_entry.get().upper()
    try:
        amount = float(amount_entry.get())
    except ValueError:
        result_label.config(text="Please enter a valid numeric amount.")
        return

    rate = get_exchange_rate(base_currency, target_currency)
    if rate is not None:
        converted_amount = amount * rate
        result_label.config(text=f"{converted_amount:.2f} {target_currency}")
    else:
        result_label.config(text="Conversion failed. Check the currency codes.")

# Set up the main window
root = tk.Tk()
root.title("Currency Calculator")

# Create widgets
amount_label = tk.Label(root, text="Amount:")
amount_entry = tk.Entry(root)

currency_label = tk.Label(root, text="Base Currency code(eg: USD):")
currency_entry = tk.Entry(root)

new_currency_label = tk.Label(root, text="New Currency:")
new_currency_entry = tk.Entry(root)

button = tk.Button(root, text="Convert", command=convert)

result_label = tk.Label(root, text="", fg="blue")

# Lay out widgets using the grid geometry manager
amount_label.grid(row=0, column=0, padx=5, pady=5, sticky="E")
amount_entry.grid(row=0, column=1, padx=5, pady=5)

currency_label.grid(row=1, column=0, padx=5, pady=5, sticky="E")
currency_entry.grid(row=1, column=1, padx=5, pady=5)

new_currency_label.grid(row=2, column=0, padx=5, pady=5, sticky="E")
new_currency_entry.grid(row=2, column=1, padx=5, pady=5)

button.grid(row=3, column=0, columnspan=2, pady=10)
result_label.grid(row=4, column=0, columnspan=2)

root.geometry("500x400")
root.mainloop()
