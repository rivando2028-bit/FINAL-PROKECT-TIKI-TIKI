while sisa > 0:
    pengeluaran = float(input(""))
    
    if pengeluaran >= 2000:
        sisa = sisa - pengeluaran
        log_pengeluaran.append(pengeluaran)
    
    print(sisa, log_pengeluaran)