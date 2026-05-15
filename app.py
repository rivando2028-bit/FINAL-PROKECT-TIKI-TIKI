import streamlit as st

st.title("Program Pengeluaran Saldo")

# INPUT saldo awal
saldo_awal = st.number_input("Masukkan saldo awal:", min_value=0, step=1000)

# IF saldo_awal > 0
if saldo_awal > 0:

    # Inisialisasi session state
    if "sisa" not in st.session_state:
        st.session_state.sisa = saldo_awal

    if "log_pengeluaran" not in st.session_state:
        st.session_state.log_pengeluaran = []

    st.subheader(f"Sisa Saldo: Rp {st.session_state.sisa}")
    st.write("Log Pengeluaran:", st.session_state.log_pengeluaran)

    # WHILE sisa > 0
    if st.session_state.sisa > 0:

        pengeluaran = st.number_input(
            "Masukkan pengeluaran:",
            min_value=0,
            step=1000
        )

        if st.button("Tambah Pengeluaran"):

            # IF pengeluaran >= 2000
            if pengeluaran >= 2000:

                st.session_state.sisa = (
                    st.session_state.sisa - pengeluaran
                )

                st.session_state.log_pengeluaran.append(pengeluaran)

                st.success("Pengeluaran berhasil ditambahkan")

            else:
                st.warning("Pengeluaran minimal Rp 2000")

    # OUTPUT
    st.write("Sisa saldo sekarang:", st.session_state.sisa)
    st.write("Daftar pengeluaran:", st.session_state.log_pengeluaran)

    # Jika saldo habis
    if st.session_state.sisa <= 0:
        st.error("Saldo habis")

else:
    st.info("Masukkan saldo awal lebih dari 0")