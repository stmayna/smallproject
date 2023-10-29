import tkinter as tk
from tkinter import simpledialog, messagebox

# Define the function for choosing items
def PilihBarang():
    def choose_items():
        input_barang = int(entry_barang.get())
        if 1 <= input_barang <= 8:
            input_ukuran = entry_ukuran.get().upper()
            if input_ukuran in ["S", "M", "L", "XL"]:
                barang_dipilih.append(input_barang)
                harga_barang_dipilih.append(harga[input_barang])
                ukuran_dipilih.append(input_ukuran)
                update_item_list()
            else:
                error_label.config(text="Maaf, ukuran tidak tersedia. Silahkan pilih kembali ukuran yang ingin Anda pilih (S/M/L/XL).")
        else:
            error_label.config(text="Maaf, barang tidak tersedia. Silahkan pilih kembali barang yang ingin Anda beli (1-8).")


    def update_item_list():
        item_list.delete(0, tk.END)
        for i, item in enumerate(barang_dipilih, start=1):
            size = ukuran_dipilih[i-1] if i <= len(ukuran_dipilih) and ukuran_dipilih[i-1] in ["S", "M", "L", "XL"] else "Invalid size (S/M/L/XL only)"
            item_list.insert(tk.END, f"{i}. {barang[item]} ({size})")


    # Create a new Tkinter window
    item_window = tk.Toplevel()
    item_window.title("Pilih Barang")
    
    # Create a label and an entry for selecting items
    select_label = tk.Label(item_window, text="Silahkan masukkan nomor barang yang akan dibeli (1-8):")
    entry_barang = tk.Entry(item_window)
    
    # Create a label and an entry for selecting sizes
    size_label = tk.Label(item_window, text="Silahkan masukkan ukuran yang akan dipilih (S/M/L/XL):")
    entry_ukuran = tk.Entry(item_window)
    
    # Create a button to choose the item
    choose_button = tk.Button(item_window, text="Pilih Barang", command=choose_items)
    
    # Create a listbox to display selected items
    item_list = tk.Listbox(item_window, selectmode=tk.SINGLE, height=10, width=40)
    
    # Create a label for error messages
    error_label = tk.Label(item_window, text="", fg="red")
    
    # Create a button to continue or finish item selection
    continue_button = tk.Button(item_window, text="Lanjutkan Pilih Barang", command=item_window.destroy)
    
    # Pack or grid the widgets
    select_label.pack()
    entry_barang.pack()
    size_label.pack()
    entry_ukuran.pack()
    choose_button.pack()
    item_list.pack()
    error_label.pack()
    continue_button.pack()

# Define the function for payment confirmation
def confirm_payment():
    # Calculate the total price of selected items
    harga_total = sum(harga_barang_dipilih)

    # Display a dialogue for payment details
    alamat = simpledialog.askstring("Alamat", "Masukkan alamat yang ingin dituju pengiriman:")
    
    if alamat:
        payment_method = simpledialog.askstring("Pembayaran", "Masukkan metode pembayaran (BCA/Gopay/Dana):")
        if payment_method:
            payment_method = payment_method.upper()
            if payment_method in ["BCA", "GOPAY", "DANA"]:
                expected_amount = harga_total
                amount_paid = simpledialog.askinteger("Pembayaran", f"Masukkan jumlah uang yang ingin Anda bayarkan | Total (Rp {expected_amount}):")
                if amount_paid is not None:
                    if amount_paid == expected_amount:
                        confirmation_message = f"Transaksi Anda melalui {payment_method} sebesar {expected_amount} telah berhasil. Pesanan Anda akan segera diproses dan dikirimkan ke {alamat}. Terima kasih."
                        messagebox.showinfo("Konfirmasi Pembayaran", confirmation_message)
                    else:
                        messagebox.showerror("Error", "Maaf, uang yang dibayarkan harus merupakan uang pas.")
            else:
                messagebox.showerror("Error", "Maaf, metode pembayaran yang dimasukkan tidak valid.")

# Set up the window
window = tk.Tk()
window.title("Online Shop")

# Create a welcome message label
welcome_label = tk.Label(window, text="Selamat datang di Ten Shop!\nBerikut harga dan ukuran dari barang yang kami jual.")
welcome_label.pack()

# Create a frame for the product information
product_info_frame = tk.Frame(window)
product_info_frame.pack()

# Define the product information with images
product_info = [
    ("No", "Nama Barang", "Harga Barang (Rp)", "Ukuran", "Image Path"),
    (1, "Knit Cardigan", 100000, "S, M, L, XL", "images/knit_cardigan.png"),
    (2, "Longsleeve", 70000, "S, M, L, XL", "images/longsleeve.png"),
    (3, "Denim Jacket", 200000, "S, M, L, XL", "images/jeans_jacket.png"),
    (4, "Varsity Jacket", 350000, "S, M, L, XL", "images/varsity_jacket.png"),
    (5, "Midi Skirt", 90000, "S, M, L, XL", "images/midi_skirt.png"),
    (6, "Baggy Jeans", 185000, "S, M, L, XL", "images/baggy_jeans.png"),
    (7, "Jogger Pants", 150000, "S, M, L, XL", "images/jogger_pants.png"),
    (8, "Long Dress", 200000, "S, M, L, XL", "images/long_dress.png")
]

# Create a dictionary to map products to their image paths
image_paths = {product[1]: product[4] for product in product_info[1:]}

# Create and display labels for product information, including images
for row, data in enumerate(product_info):
    for col, value in enumerate(data):
        if col == 4:  # The image column
            product_name = product_info[row][1]
            image_path = image_paths.get(product_name)
            if image_path:
                image = tk.PhotoImage(file=image_path)
                image_label = tk.Label(product_info_frame, image=image)
                image_label.image = image  # Keep a reference to the image
                image_label.grid(row=row, column=col, padx=5, pady=5)
        else:
            label = tk.Label(product_info_frame, text=str(value))
            label.grid(row=row, column=col, padx=5, pady=5)

# Define the items
barang = ["Nama Barang", "Knit Cardigan", "Longsleeve", "Denim Jacket", "Varsity Jacket",
          "Midi Skirt", "Baggy Jeans", "Jogger Pants", "Long Dress"]
nomor = [i for i in range(1, len(barang))]
nomor.insert(0, "No")
harga = [100000, 70000, 200000, 350000, 90000, 185000, 150000, 200000]
harga.insert(0, "Harga Barang (Rp)")
size = ["S, M, L, XL" for i in range(1, len(barang) + 1)]
size.insert(0, "Ukuran")

# Create buttons for each function
choose_item_button = tk.Button(window, text="Pilih Barang", command=PilihBarang)
confirm_payment_button = tk.Button(window, text="Konfirmasi Pembayaran", command=confirm_payment)
choose_item_button.pack()
confirm_payment_button.pack()

# Create lists for selected items, prices, and sizes
barang_dipilih = []
harga_barang_dipilih = []
ukuran_dipilih = []

# Run the Tkinter application
window.mainloop()
