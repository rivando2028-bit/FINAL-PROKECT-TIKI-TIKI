# INPUT Saldo_awal
saldo_awal = float(input("Masukkan Saldo Awal: "))

# IF Saldo_awal > 0 THEN
if saldo_awal > 0:
    sisa = saldo_awal
    log_pengeluaran = []

    # WHILE Sisa > 0 DO
    while sisa > 0:
        pengeluaran = float(input("Masukkan Pengeluaran: "))
        
        # IF Pengeluaran >= 2000 THEN
        if pengeluaran >= 2000:
            sisa = sisa - pengeluaran
            log_pengeluaran.append(pengeluaran) # TAMBAHKAN ke Log
        
        # OUTPUT Sisa, Log_Pengeluaran
        print("Sisa Saldo:", sisa)
        print("Catatan Pengeluaran:", log_pengeluaran)

print("Program Selesai.")