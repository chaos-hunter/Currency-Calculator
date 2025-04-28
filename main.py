import tkinter as tk
import requests

# 1. Dictionary: Country -> Currency code
country_to_currency = {
    "united arab emirates": "AED",
    "afghanistan": "AFN",
    "albania": "ALL",
    "armenia": "AMD",
    "netherlands antilles": "ANG",
    "angola": "AOA",
    "argentina": "ARS",
    "australia": "AUD",
    "aruba": "AWG",
    "azerbaijan": "AZN",
    "bosnia": "BAM",
    "herzegovina": "BAM",
    "barbados": "BBD",
    "bangladesh": "BDT",
    "bulgaria": "BGN",
    "bahrain": "BHD",
    "burundi": "BIF",
    "bermuda": "BMD",
    "brunei": "BND",
    "bolivia": "BOB",
    "brazil": "BRL",
    "bahamas": "BSD",
    "bhutan": "BTN",
    "botswana": "BWP",
    "belarus": "BYN",
    "belize": "BZD",
    "canada": "CAD",
    "congo": "CDF",
    "switzerland": "CHF",
    "chile": "CLP",
    "china": "CNY",
    "colombia": "COP",
    "costa rica": "CRC",
    "cuba": "CUP",
    "cape verde": "CVE",
    "czech republic": "CZK",
    "djibouti": "DJF",
    "denmark": "DKK",
    "dominican Republic": "DOP",
    "algeria": "DZD",
    "egypt": "EGP",
    "eritrea": "ERN",
    "ethiopia": "ETB",
    "austria": "EUR",
    "belgium": "EUR",
    "croatia": "EUR",
    "cyprus": "EUR",
    "estonia": "EUR",
    "finland": "EUR",
    "france": "EUR",
    "germany": "EUR",
    "greece": "EUR",
    "ireland": "EUR",
    "italy": "EUR",
    "latvia": "EUR",
    "lithuania": "EUR",
    "luxembourg": "EUR",
    "malta": "EUR",
    "netherlands": "EUR",
    "portugal": "EUR",
    "slovakia": "EUR",
    "slovenia": "EUR",
    "spain": "EUR",
    "fiji": "FJD",
    "falkland islands": "FKP",
    "faroe islands": "FOK",
    "united kingdom": "GBP",
    "georgia": "GEL",
    "guernsey": "GGP",
    "ghana": "GHS",
    "gibraltar": "GIP",
    "the gambia": "GMD",
    "guinea": "GNF",
    "guatemala": "GTQ",
    "guyana": "GYD",
    "hong kong": "HKD",
    "honduras": "HNL",
    "haiti": "HTG",
    "hungary": "HUF",
    "indonesia": "IDR",
    "israel": "ILS",
    "isle of man": "IMP",
    "india": "INR",
    "iraq": "IQD",
    "iran": "IRR",
    "iceland": "ISK",
    "jersey": "JEP",
    "jamaica": "JMD",
    "jordan": "JOD",
    "japan": "JPY",
    "kenya": "KES",
    "kyrgyzstan": "KGS",
    "cambodia": "KHR",
    "kiribati": "KID",
    "comoros": "KMF",
    "south korea": "KRW",
    "kuwait": "KWD",
    "cayman islands": "KYD",
    "kazakhstan": "KZT",
    "laos": "LAK",
    "lebanon": "LBP",
    "sri lanka": "LKR",
    "liberia": "LRD",
    "lesotho": "LSL",
    "libya": "LYD",
    "morocco": "MAD",
    "moldova": "MDL",
    "madagascar": "MGA",
    "north macedonia": "MKD",
    "myanmar": "MMK",
    "mongolia": "MNT",
    "macau": "MOP",
    "mauritania": "MRU",
    "mauritius": "MUR",
    "maldives": "MVR",
    "Malawi": "MWK",
    "Mexico": "MXN",
    "Malaysia": "MYR",
    "Mozambique": "MZN",
    "Namibia": "NAD",
    "nigeria": "NGN",
    "Nicaragua": "NIO",
    "Norway": "NOK",
    "Nepal": "NPR",
    "New Zealand": "NZD",
    "Oman": "OMR",
    "Panama": "PAB",
    "Peru": "PEN",
    "Papua New Guinea": "PGK",
    "Philippines": "PHP",
    "Pakistan": "PKR",
    "Poland": "PLN",
    "Paraguay": "PYG",
    "Qatar": "QAR",
    "Romania": "RON",
    "Serbia": "RSD",
    "Russia": "RUB",
    "Rwanda": "RWF",
    "Saudi Arabia": "SAR",
    "Solomon Islands": "SBD",
    "Seychelles": "SCR",
    "Sudan": "SDG",
    "Sweden": "SEK",
    "Singapore": "SGD",
    "Saint Helena": "SHP",
    "Sierra Leone": "SLE",
    "Somalia": "SOS",
    "Suriname": "SRD",
    "South Sudan": "SSP",
    "São Tomé and Príncipe": "STN",
    "Syria": "SYP",
    "Eswatini": "SZL",
    "Thailand": "THB",
    "Tajikistan": "TJS",
    "Turkmenistan": "TMT",
    "Tunisia": "TND",
    "Tonga": "TOP",
    "Turkey": "TRY",
    "Trinidad and Tobago": "TTD",
    "Tuvalu": "TVD",
    "Taiwan": "TWD",
    "Tanzania": "TZS",
    "Ukraine": "UAH",
    "Uganda": "UGX",
    "united states": "USD",
    "uruguay": "UYU",
    "uzbekistan": "UZS",
    "venezuela": "VES",
    "vietnam": "VND",
    "vanuatu": "VUV",
    "samoa": "WST",
    "cemac": "XAF",
    "organisation of eastern caribbean states": "XCD",
    "international monetary fund": "XDR",
    "cfa": "XOF",
    "collectivités d'outre-mer": "XPF",  # CFP Franc
    "yemen": "YER",
    "south africa": "ZAR",
    "zambia": "ZMW",
    "zimbabwe": "ZWL"
}

country_to_currency = {
    country.lower(): code
    for country, code in country_to_currency.items()
}
country_aliases = {
    "uk":            "united kingdom",
    "gb":            "united kingdom",
    "usa":           "united states",
    "us":            "united states",
    "sa":            "south africa",
    "uae":           "united arab emirates",
    "korea":         "south korea",
    "saudi":          "saudi arabia",
    "trinidad":       "trinidad and tobago",
    "tobago":         "trinidad and tobago",
}
def resolve_currency_code(user_input: str):
    key = user_input.strip().lower()
    # direct match?
    if key in country_to_currency:
        return country_to_currency[key]
    # alias match?
    if key in country_aliases:
        canonical = country_aliases[key]
        return country_to_currency.get(canonical)
    return None

api_key = "ENTER YOUR API KEY"
link = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

def get_exchange_rate(base_currency_code, target_currency_code):
    response = requests.get(link + base_currency_code.upper())
    data = response.json()
    if response.status_code == 200 and "conversion_rates" in data:
        return data["conversion_rates"].get(target_currency_code.upper())
    else:
        print("Failed to retrieve exchange rates")
        return None

def convert():
    # Get user inputs
    user_base = base_country_entry.get()
    user_target = target_country_entry.get()

    base_code = resolve_currency_code(user_base)
    target_code = resolve_currency_code(user_target)

    if not base_code:
        result_label.config(text=f"Unknown base country: {user_base}")
        return
    if not target_code:
        result_label.config(text=f"Unknown target country: {user_target}")
        return

    # parse amount
    try:
        amount = float(amount_entry.get().strip())
    except ValueError:
        result_label.config(text="Please enter a valid numeric amount.")
        return

    # fetch & convert
    rate = get_exchange_rate(base_code, target_code)
    if rate is None:
        result_label.config(text="Conversion failed; check the API or currency codes.")
        return

    converted_amount = amount * rate
    result_label.config(
        text=f"{amount:.2f} {base_code} = {converted_amount:.2f} {target_code}"
    )

# Set up the GUI
root = tk.Tk()
root.title("Country Currency Converter")

amount_label = tk.Label(root, text="Amount")
amount_entry = tk.Entry(root)

base_country_label = tk.Label(root, text="Base Country")
base_country_entry = tk.Entry(root)

target_country_label = tk.Label(root, text="Target Country")
target_country_entry = tk.Entry(root)

convert_button = tk.Button(root, text="Convert", command=convert)
result_label = tk.Label(root, text="")

# Grid layout
amount_label.grid(row=0, column=0, padx=5, pady=5)
amount_entry.grid(row=0, column=1, padx=5, pady=5)

base_country_label.grid(row=1, column=0, padx=5, pady=5)
base_country_entry.grid(row=1, column=1, padx=5, pady=5)

target_country_label.grid(row=2, column=0, padx=5, pady=5)
target_country_entry.grid(row=2, column=1, padx=5, pady=5)

convert_button.grid(row=3, column=0, columnspan=2, pady=10)
result_label.grid(row=4, column=0, columnspan=2)

root.geometry("500x400")
root.mainloop()
