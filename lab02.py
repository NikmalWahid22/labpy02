tipe_tiket = input("Masukkan tipe tiket (Reguler/VIP): ")
status_member = input("Apakah Anda memiliki kartu member? (Ya/Tidak): ")

if tipe_tiket.lower() == "reguler":
    harga = 50000
else:
    if tipe_tiket.lower() == "vip":
        harga = 100000
    else:
        harga = 0
        print("Tipe tiket tidak valid.")

if harga != 0:
    total_harga = harga * 0.8 if status_member.lower() == "ya" else harga

    print(f"Tipe tiket: {tipe_tiket}")
    print(f"Status member: {status_member}")
    print(f"Total harga yang harus dibayar: Rp{total_harga}")
