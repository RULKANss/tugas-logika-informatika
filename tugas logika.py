def hitung_biaya_pengiriman(nama_perusahaan, nama_barang, berat, jarak, express=False, member=False, asuransi=False, packing_khusus=False):
   
    biaya = 10000
    
    if berat > 5:
        biaya += 5000
    
    if jarak > 10:
        biaya += 8000
    
    if express:
        biaya += 20000
    
    if asuransi:
        biaya += 5000
    
    if packing_khusus:
        biaya += 3000
    
    if member:
        biaya *= 0.9  
    
    return nama_perusahaan, nama_barang, int(biaya) 

if __name__ == "__main__":
    nama_perusahaan = input("Masukkan nama perusahaan pengiriman: ")
    nama_barang = input("Masukkan nama barang yang akan dikirim: ")
    berat = float(input("Masukkan berat barang (kg): "))
    jarak = float(input("Masukkan jarak pengiriman (km): "))
    express = input("Apakah ingin menggunakan layanan express? (ya/tidak): ").strip().lower() == "ya"
    member = input("Apakah Anda member? (ya/tidak): ").strip().lower() == "ya"
    asuransi = input("Apakah ingin menambahkan asuransi? (ya/tidak): ").strip().lower() == "ya"
    packing_khusus = input("Apakah ingin menggunakan packing khusus? (ya/tidak): ").strip().lower() == "ya"
    
    perusahaan, barang, biaya = hitung_biaya_pengiriman(nama_perusahaan, nama_barang, berat, jarak, express, member, asuransi, packing_khusus)
    print(f"\nPerusahaan: {perusahaan}\nBarang: {barang}\nBiaya Pengiriman: Rp {biaya}")
