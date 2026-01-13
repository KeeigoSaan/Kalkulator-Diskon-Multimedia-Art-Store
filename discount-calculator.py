import tkinter as tk
from tkinter import messagebox

def calculate_discount():
    try:
        original_price = float(entry_price.get())
        discount_percent = float(entry_discount.get())

        if original_price < 0 or discount_percent < 0:
            messagebox.showerror("Error", "Values cannot be negative.")
            return

        if discount_percent > 100:
            messagebox.showerror("Error", "Discount cannot be more than 100%.")
            return

        discount_amount = original_price * (discount_percent / 100)
        final_price = original_price - discount_amount

        result_label.config(text=f"Final Price: Rp. {final_price:,.2f}".replace(",", "."))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Window
root = tk.Tk()
root.title("Discount Calculator")
root.geometry("420x260")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="Discount Calculator", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# Frame for inputs
frame = tk.Frame(root)
frame.pack(pady=10)

# Original Price
label_price = tk.Label(frame, text="Original Price:")
label_price.grid(row=0, column=0, sticky="w", padx=10, pady=5)
entry_price = tk.Entry(frame, width=25)
entry_price.grid(row=0, column=1, padx=10, pady=5)

# Discount
label_discount = tk.Label(frame, text="Discount (%):")
label_discount.grid(row=1, column=0, sticky="w", padx=10, pady=5)
entry_discount = tk.Entry(frame, width=25)
entry_discount.grid(row=1, column=1, padx=10, pady=5)

# Button
calc_button = tk.Button(root, text="Calculate", width=12, command=calculate_discount)
calc_button.pack(pady=10)

# Result
result_label = tk.Label(root, text="Final Price: Rp. 0.00", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()