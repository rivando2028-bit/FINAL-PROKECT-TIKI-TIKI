import streamlit as st

st.title("Program Pengeluaran")

# Input saldo awal
saldo_awal = st.number_input("Masukkan saldo awal", min_value=0, step=1000)

# Tombol mulai
if st.button("Mulai"):
    
    if saldo_awal > 0:
        sisa = saldo_awal
        log_pengeluaran = []

        while sisa > 0:
            
            pengeluaran = st.number_input(
                "Masukkan pengeluaran (minimal 2000)",
                min_value=0,
                step=1000,
                key=sisa
            )

            if st.button("Tambah Pengeluaran", key="btn" + str(sisa)):

                if pengeluaran >= 2000:
                    sisa = sisa - pengeluaran
                    log_pengeluaran.append(pengeluaran)

                    st.write("Sisa saldo :", sisa)
                    st.write("Log pengeluaran :", log_pengeluaran)

                else:
                    st.write("Pengeluaran harus minimal 2000")

                break

    else:
        st.write("Saldo awal harus lebih dari 0")