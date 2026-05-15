# FINAL-PROKECT-TIKI-TIKI
saldo_awal = float(input(""))

if saldo_awal > 0:
    sisa = saldo_awal
    log_pengeluaran = []

    while sisa > 0:
        pengeluaran = float(input(""))
        
        if pengeluaran >= 2000:
            sisa = sisa - pengeluaran
            log_pengeluaran.append(pengeluaran)
        
        print(sisa, log_pengeluaran)
