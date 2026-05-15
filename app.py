import streamlit as st

st.title("Program Pengeluaran Saldo")

# INPUT SALDO AWAL
saldo_awal = st.number_input("Masukkan saldo awal", min_value=0, step=1000)

# Tombol mulai
if st.button("Mulai"):

    # IF SALDO > 0
    if saldo_awal > 0:

        sisa = saldo_awal
        log_pengeluaran = []

        # WHILE
        while sisa > 0:

            pengeluaran = st.number_input(
                f"Masukkan pengeluaran (Sisa saldo: {sisa})",
                min_value=0,
                step=1000,
                key=sisa
            )

            if st.button(f"Tambah Pengeluaran {sisa}"):

                # IF PENGELUARAN VALID
                if pengeluaran >= 2000 and pengeluaran <= sisa:

                    sisa = sisa - pengeluaran
                    log_pengeluaran.append(pengeluaran)

                    st.success(f"Pengeluaran berhasil ditambahkan: {pengeluaran}")
                    st.write("Sisa saldo:", sisa)
                    st.write("Log Pengeluaran:", log_pengeluaran)

                else:
                    st.error("Pengeluaran tidak valid")

                # STOP WHILE JIKA SALDO HABIS
                if sisa == 0:
                    st.warning("Saldo habis")

                break

    else:
        st.error("Saldo awal harus lebih dari 0")