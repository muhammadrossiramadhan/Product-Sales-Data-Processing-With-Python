'''
    ========================================================================================
    |                                                                                      |
    |                           Pengolahan Data Penjualan Produk                           |
    |                                                                                      |
    |                                                                                      |
    |                                        OLEH:                                         |
    |                                                                                      |
    |                       Muhammad Rossi Ramadhan ( 250535625057 )                       |
    |                       Shofiyah La Amiri       ( 250535626476 )                       |
    |                       Nova Indriansyah        ( 250535602240 )                       |
    |                                                                                      |
    |                                                                                      |
    ========================================================================================
'''

# Inisialisasi data yang akan diolah
data_bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni"]
data_penjualan = [
    [120, 150, 130, 170, 200, 190],
    [80, 100, 90, 110, 130, 120],
    [200, 210, 190, 180, 220, 210]
]
# Menetapkan ambang batas untuk mendeteksi lonjakan, yaitu 20%
batasan_lonjakan = 20/100

# --- Bagian A: Menghitung total penjualan untuk setiap produk ---
print("\n---Bagian A---\n")
# Fungsi ini menghitung total per produk.
def total_penjualan_per_produk():
    # Menginisialisasi variabel untuk menyimpan total
    retval = []
    # Iterasi melalui setiap baris (produk)
    for baris in data_penjualan:
        #jumlah setiap produk A,B,C akan ditambahkan ke variabel retval 
        retval.append(sum(baris))

    # Mengembalikan banyaknya total penjualan untuk setiap produk A,B,C
    return f"Total Penjualan untuk setiap produk : Produk A = {retval[0]}, Produk B = {retval[1]}, Produk B = {retval[2]}"

# Fungsi ini menghitung total penjualan keseluruhan, bukan per produk.
def total_penjualan():
    # Menginisialisasi variabel untuk menyimpan total
    retval = 0
    # Iterasi melalui setiap baris (produk)
    for i in range(len(data_penjualan)):
        # Menambahkan total penjualan per baris ke total keseluruhan
        retval += sum(data_penjualan[i])
    return f"Total Penjualan untuk setiap produk : {retval}"

# Mencetak hasil total penjualan keseluruhan
print(total_penjualan_per_produk())
print("---")

# Mencetak hasil total penjualan keseluruhan
print(total_penjualan())
print("---")


# --- Bagian B: Menemukan bulan dengan penjualan tertinggi ---
print("\n---Bagian B---\n")
def maksimum():
    # List untuk menyimpan nilai penjualan tertinggi per produk
    retval = []
    # List untuk menyimpan nama bulan dengan penjualan tertinggi
    bulan = []
    # Iterasi setiap baris data penjualan
    for i in range(len(data_penjualan)):
        # Mengambil data satu baris (satu produk)
        baris = data_penjualan[i]
        # Menemukan nilai maksimum dari baris dan menyimpannya
        retval.append(max(baris))
        # Menemukan nama bulan berdasarkan indeks dari nilai maksimum
        bulan.append(data_bulan[baris.index(retval[i])])
    # Mengembalikan kedua list
    return retval, bulan

# Mencetak nilai dan bulan dengan penjualan tertinggi
retval_max, bulan_max = maksimum()
print(f"penjualan tertinggi A adalah {retval_max[0]} pada bulan {bulan_max[0]}, penjualan tertinggi A adalah {retval_max[1]} pada bulan {bulan_max[1]}, penjualan tertinggi A adalah {retval_max[2]} pada bulan {bulan_max[2]}")
print("---")

# --- Bagian B: Menemukan bulan dengan penjualan terendah ---
def minimum():
    # List untuk menyimpan nilai penjualan terendah per produk
    retval = []
    # List untuk menyimpan nama bulan dengan penjualan terendah
    bulan = []
    # Iterasi setiap baris data penjualan
    for i in range(len(data_penjualan)):
        # Mengambil data satu baris (satu produk)
        baris = data_penjualan[i]
        # Menemukan nilai minimum dari baris dan menyimpannya
        retval.append(min(baris))
        # Menemukan nama bulan berdasarkan indeks dari nilai minimum
        bulan.append(data_bulan[baris.index(retval[i])])
    return retval, bulan

# Mencetak nilai dan bulan dengan penjualan terendah
retval_min, bulan_min = minimum()
print(f"penjualan tertinggi A adalah {retval_max[0]} pada bulan {bulan_max[0]}, penjualan tertinggi A adalah {retval_max[1]} pada bulan {bulan_max[1]}, penjualan tertinggi A adalah {retval_max[2]} pada bulan {bulan_max[2]}")
print("---")

# --- Bagian C: Mengidentifikasi lonjakan penjualan ---
print("\n---Bagian C---\n")
def lonjakan():
    # List untuk menyimpan rata-rata penjualan per produk
    rata_rata_perbaris = []
    
    # Menghitung rata-rata penjualan untuk setiap produk
    for i in range(len(data_penjualan)):
        rata_rata = sum(data_penjualan[i]) / len(data_penjualan[i])
        rata_rata_perbaris.append(rata_rata)
    
    # List untuk menyimpan informasi lonjakan yang ditemukan
    lonjakan_info = []
    
    # Iterasi melalui setiap produk dan setiap bulan
    for i in range(len(data_penjualan)):
        for j in range(len(data_penjualan[i])):
            penjualan = data_penjualan[i][j]
            
            # Memeriksa apakah penjualan saat ini lebih besar dari ambang batas lonjakan
            # Rumus: rata-rata * (1 + batasan)
            if penjualan > rata_rata_perbaris[i] * (1 + batasan_lonjakan):
                # Menentukan nama produk (A, B, C, dst.) berdasarkan indeks
                nama_produk = f"Produk {chr(65 + i)}"
                bulan_lonjakan = data_bulan[j]
                
                # Menambahkan informasi lonjakan ke list
                lonjakan_info.append(f"  - {nama_produk} mengalami lonjakan di bulan {bulan_lonjakan} "
                                     f"dengan penjualan {penjualan} (Rata-rata: {rata_rata_perbaris[i]:.2f})")
                
    # Mengembalikan hasil. Jika tidak ada lonjakan, tampilkan pesan.
    if not lonjakan_info:
        return "\nTidak ada lonjakan penjualan yang signifikan terdeteksi."
    else:
        return "Lonjakan penjualan yang terdeteksi:\n" + "\n".join(lonjakan_info)

# Mencetak hasil identifikasi lonjakan
print(lonjakan())
print("---")