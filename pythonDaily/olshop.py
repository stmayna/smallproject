print("Selamat datang di Ten Shop!\nBerikut harga dan ukuran dari barang yang kami jual.") 

barang_dipilih = []  
jumlah_barang = []
harga_barang_dipilih = []
ukuran_dipilih = [] 

def PilihBarang(): 
    yes_or_no = True
    i = 1
    while (yes_or_no == True):
        input_barang = int(input("Silahkan masukkan nomor barang yang akan dibeli (1-8): "))
        if input_barang != 1 and input_barang != 2 and input_barang != 3 and input_barang != 4 and input_barang != 5 and input_barang != 6 and input_barang != 7 and input_barang != 8:
            print("Maaf, barang tidak tersedia. Silahkan pilih kembali barang yang ingin Anda beli.")
        else:
            barang_dipilih.append(input_barang)
            harga_barang_dipilih.append(harga[input_barang])
            input_ukuran = input("Silahkan masukkan ukuran yang akan dipilih: ")
            input_ukuran = input_ukuran.upper()
            while input_ukuran != "S" and input_ukuran != "M" and input_ukuran != "L" and input_ukuran != "XL":
                print("Maaf, ukuran tidak tersedia. Silahkan pilih kembali ukuran yang ingin Anda pilih.")
                input_ukuran = input("Silahkan masukkan ukuran yang akan dipilih: ")
                input_ukuran = input_ukuran.upper()
            ukuran_dipilih.append(input_ukuran)
            yes_or_no = input("Apakah mau lanjut pilih barang(Ya/Tidak): ")
            yes_or_no = yes_or_no.lower()
            i += 1
            while yes_or_no != "ya" and yes_or_no != "tidak":
                print("Maaf, silahkan jawab dengan ya atau tidak.")
                yes_or_no = input("Apakah mau lanjut pilih barang(Ya/Tidak): ")
            if yes_or_no == "ya":
                yes_or_no = True
            else:
                yes_or_no = False
    return barang_dipilih, harga_barang_dipilih, ukuran_dipilih

barang = ["Nama Barang", "Knit Cardigan", "Longsleeve", "Denim Jacket", "Varsity Jacket",
          "Midi Skirt", "Baggy Jeans", "Jogger Pants", "Long Dress"]
nomor = [i for i in range(1, len(barang))]
nomor.insert(0, "No")
harga = [100000, 70000, 200000, 350000, 90000, 185000, 150000, 200000]
harga.insert(0, "Harga Barang (Rp)")
size = ["S, M, L, XL" for i in range(1,len(barang)+1)]
size.insert(0, "Ukuran")

for baris in range (len(nomor)):
    isi = nomor[baris]
    print("|     ", isi, end="")
    for spasi_kanan_kolom_1 in range(7-len(str(isi))):
        print(" ", end="")
    isi1 = barang[baris]
    print("| ", isi1, end="")
    for spasi_kanan_kolom_2 in range(18-len(isi1)):
        print(" ", end="")
    isi2 = harga[baris]
    print("| ", isi2, end="")
    for spasi_kanan_kolom_3 in range(18-len(str(isi2))):
        print(" ", end="")
    isi3 = size[baris]
    print("| ", isi3, end="")
    for spasi_kanan_kolom_4 in range(14-len(isi3)):
        print(" ", end="")
    print("|")
        
PilihBarang()

i = 0
harga_total = 0
while (i < len(barang_dipilih)):
    harga_total += harga_barang_dipilih[i]
    i += 1

barang_dipilih.insert(0, "Nama Barang")
harga_barang_dipilih.insert(0, "Harga Barang")
ukuran_dipilih.insert(0, "Ukuran")
alamat = input("Masukkan alamat yang ingin dituju pengiriman: ")
alamat = alamat.upper()

print("-------------------------- KONFIRMASI PEMBAYARAN --------------------------")
print("Alamat pengiriman:", alamat)
for baris in range (len(barang_dipilih)):
    isi = nomor[baris]
    print("|     ", isi, end="")
    for spasi_kanan_kolom_1 in range(7-len(str(isi))):
        print(" ", end="")
    if barang_dipilih[baris] == "Nama Barang":
        isi1 = barang_dipilih[baris]
    else:
        isi1 = barang[barang_dipilih[baris]]
    print("| ", isi1, end="")
    for spasi_kanan_kolom_2 in range(18-len(isi1)):
        print(" ", end="")
    isi2 = ukuran_dipilih[baris]
    print("| ", isi2, end="")
    for spasi_kanan_kolom_3 in range(14-len(isi2)):
        print(" ", end="")
    isi3 = harga_barang_dipilih[baris]
    print("| ", isi3, end="")
    for spasi_kanan_kolom_4 in range(18-len(str(isi3))):
        print(" ", end="")
    print("|")
print("|                       Total                       |", end="")
isi4 = harga_total
print(" ", isi4, end="")
for spasi_kanan_kolom_5 in range(18-len(str(isi4))):
    print(" ", end="")
print("|")

yes_or_no = input("Silahkan cek barang belanjaan Anda. Apakah sudah benar? (Ya/Tidak): ")
yes_or_no = yes_or_no.lower()

while yes_or_no != "ya" and yes_or_no != "tidak":
    print("Maaf, silahkan jawab dengan ya atau tidak.")
    yes_or_no = input("Apakah mau lanjut pilih barang(Ya/Tidak): ")

if yes_or_no == "ya":
    metode = input("Masukkan metode pembayaran (BCA/Gopay/Dana): ")
    metode = metode.upper()
    while metode != "BCA" and metode != "GOPAY" and metode != "DANA":
        print("Maaaf, kami hanya menerima pembayaran melalui BCA, Gopay, atau Dana.")
        metode = input("Masukkan metode pembayaran (BCA/Gopay/Dana): ")
        metode = metode.upper()
    uang = int(input("Masukkan jumlah uang yang ingin Anda bayarkan: "))
    while uang != harga_total:
        print("Maaf, uang yang dibayarkan harus merupakan uang pas.")
        uang = int(input("Masukkan jumlah uang yang ingin Anda bayarkan: "))
    print(f"Transaksi Anda melalui {metode} telah berhasil. Pesanan anda akan segera diproses dan dikirimkan ke {alamat}. Terima kasih.")
else:
    print("Silahkan mulai ulang program.")