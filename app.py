import streamlit as st

st.title("Program Pengeluaran Saldo")

# SESSION STATE
if "sisa" not in st.session_state:
    st.session_state.sisa = 0

if "log_pengeluaran" not in st.session_state:
    st.session_state.log_pengeluaran = []

# INPUT SALDO AWAL
saldo_awal = st.number_input(
    "Masukkan saldo awal",
    min_value=0,
    step=1000
)

# TOMBOL MULAI
if st.button("Mulai"):
    if saldo_awal > 0:
        st.session_state.sisa = saldo_awal
        st.session_state.log_pengeluaran = []

# JIKA PROGRAM SUDAH DIMULAI
if st.session_state.sisa > 0:

    st.write("Sisa saldo:", st.session_state.sisa)

    pengeluaran = st.number_input(
        "Masukkan pengeluaran",
        min_value=0,
        step=1000
    )

    # TOMBOL TAMBAH
    if st.button("Tambah Pengeluaran"):

        if (
            pengeluaran >= 2000
            and pengeluaran <= st.session_state.sisa
        ):

            st.session_state.sisa -= pengeluaran
            st.session_state.log_pengeluaran.append(pengeluaran)

            st.success("Pengeluaran berhasil ditambahkan")

        else:
            st.error("Pengeluaran tidak valid")

    # OUTPUT
    st.write("Log Pengeluaran:")
    st.write(st.session_state.log_pengeluaran)

    # JIKA SALDO HABIS
    if st.session_state.sisa == 0:
        st.warning("Saldo habis")