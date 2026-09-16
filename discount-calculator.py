import tkinter as tk
from tkinter import messagebox
from pathlib import Path
from PIL import Image, ImageTk


def calculate_discount():
    try:
        nama = entry_nama.get()
        original_price = float(entry_price.get())

        if original_price < 0:
            messagebox.showerror("Error", "Total belanja tidak boleh negatif.")
            return

        # Hitung Diskon Berdasarkan Total Belanja
        if original_price < 100000:
            discount_percent = 0
        elif 100000 <= original_price <= 500000:
            discount_percent = 10
        else:
            discount_percent = 20

        discount_amount = original_price * (discount_percent / 100)
        price_after_belanja_discount = original_price - discount_amount

        # Hitung Diskon Tambahan Member (10% dari harga setelah diskon belanja)
        if is_member_var.get() == 1:
            member_discount_amount = price_after_belanja_discount * 0.10
            member_percent_str = "10%"
        else:
            member_discount_amount = 0
            member_percent_str = "0%"

        # Hitung Total Bayar Akhir
        final_price = price_after_belanja_discount - member_discount_amount

        # Format Tampilan Rincian Struk
        nama_str = nama if nama.strip() != "" else "-"
        rincian_text = (
            f"Nama Pembeli         : {nama_str}\n"
            f"Total Awal           : Rp {original_price:,.0f}\n"
            f"Diskon Belanja ({discount_percent}%) : Rp {discount_amount:,.0f}\n"
            f"Diskon Member  ({member_percent_str}) : Rp {member_discount_amount:,.0f}\n"
            f"{'-'*35}\n"
            f"TOTAL BAYAR          : Rp {final_price:,.0f}"
        )

        result_label.config(text=rincian_text)

    except ValueError:
        messagebox.showerror("Error", "Masukkan nominal belanja yang valid!")


# Window Utama
root = tk.Tk()
root.title("Store Calculator")
root.geometry("420x450")
root.minsize(420, 450)
root.resizable(True, True)

#background  
background_color = "#DCEEFF"
panel_color = "#FFFFFF"
button_color = "#2F75B5"
button_text_color = "#FFFFFF"
root.configure(bg=background_color)

def toggle_fullscreen(event=None):
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))

root.bind("<F11>", toggle_fullscreen)
root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))

# Logo toko 
logo_path = Path(__file__).with_name("logo.png")
if logo_path.exists():
    logo_source = Image.open(logo_path)
    logo_source.thumbnail((140, 140), Image.Resampling.LANCZOS)
    logo_image = ImageTk.PhotoImage(logo_source)
    logo_label = tk.Label(root, image=logo_image, bg=background_color)
    logo_label.pack(pady=(10, 0))

# Judul Aplikasi
title_label = tk.Label(root, text="STORE CALCULATOR", font=("Arial", 12, "bold"), bg=background_color)
title_label.pack(pady=10)

# Frame Input
frame = tk.Frame(root, bg=panel_color)
frame.pack(pady=5, padx=20, fill="x")

# Input Nama Pembeli
label_nama = tk.Label(frame, text="Nama Pembeli:", bg=panel_color)
label_nama.grid(row=0, column=0, sticky="w", padx=5, pady=5)
entry_nama = tk.Entry(frame, width=25, bg="#F7FBFF")
entry_nama.grid(row=0, column=1, padx=5, pady=5)

# Input Total Belanja
label_price = tk.Label(frame, text="Total Belanja:", bg=panel_color)
label_price.grid(row=1, column=0, sticky="w", padx=5, pady=5)
entry_price = tk.Entry(frame, width=25, bg="#F7FBFF")
entry_price.grid(row=1, column=1, padx=5, pady=5)

# Checkbox Member
is_member_var = tk.IntVar()
chk_member = tk.Checkbutton(
    frame, 
    text="Apakah Member? (Diskon tambahan 10%)", 
    variable=is_member_var,
    bg=panel_color,
    activebackground=panel_color
)
chk_member.grid(row=2, column=0, columnspan=2, sticky="w", padx=5, pady=10)

# Tombol Hitung
calc_button = tk.Button(
    root,
    text="HITUNG TOTAL",
    width=15,
    font=("Arial", 10, "bold"),
    command=calculate_discount,
    bg=button_color,
    fg=button_text_color,
    activebackground="#245A8A",
    activeforeground=button_text_color
)
calc_button.pack(pady=10)

# Frame Output/Rincian
output_frame = tk.LabelFrame(
    root,
    text="Rincian Pembayaran",
    padx=10,
    pady=10,
    bg=panel_color
)
output_frame.pack(padx=20, pady=10, fill="both", expand=True)

result_label = tk.Label(
    output_frame,
    text="Rincian akan muncul di sini.",
    font=("Consolas", 9),
    justify="left",
    bg=panel_color
)
result_label.pack(anchor="w")

root.mainloop()
