import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk

def scrape_etsy():
    categories = category_entry.get().split(", ")
    pages = int(pages_entry.get())
    output_text.delete('1.0', tk.END)
    for category in categories:
        for i in range(1, pages+1):
            url = f'https://www.etsy.com/search?q={category}&ref=pagination&page={i}'
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            items = soup.find_all('div', {'class': 'v2-listing-card__info'})
            for item in items:
                title = item.find('h3', {'class': 'v2-listing-card__title'}).text.strip()
                price = item.find('span', {'class': 'currency-value'}).text.strip()
                output_text.insert(tk.END, f'{category}: {title} - {price}\n')

# Create the main window
root = tk.Tk()
root.title('Etsy Web Scraper')
root.config(bg="skyblue")

# Create Frame widgets
left_frame = tk.Frame(root, width=200, height=400)
left_frame.pack(side=tk.LEFT, padx=10, pady=5)

right_frame = tk.Frame(root, bg='white')
right_frame.pack(side=tk.RIGHT, padx=10, pady=5, fill=tk.BOTH, expand=True)

# Create the GUI elements
category_label = tk.Label(left_frame, text='Categories (separated by comma and space):')
category_entry = tk.Entry(left_frame)
pages_label = tk.Label(left_frame, text='Pages:')
pages_entry = tk.Entry(left_frame)
scrape_button = tk.Button(left_frame, text='Scrape', command=scrape_etsy)
output_text = tk.Text(right_frame)

# Add the GUI elements to the main window
category_label.pack()
category_entry.pack()
pages_label.pack()
pages_entry.pack()
scrape_button.pack()

# Add a scrollbar to the output frame
output_scroll = ttk.Scrollbar(right_frame, command=output_text.yview)
output_scroll.pack(side=tk.RIGHT, fill=tk.Y)

output_text.configure(yscrollcommand=output_scroll.set)
output_text.pack(fill='both', expand=True)

# Start the main loop
root.mainloop()
