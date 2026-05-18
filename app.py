
import streamlit as st

st.title("Program Pengeluaran Saldo")

if "saldo_awal" not in st.session_state:
    st.session_state.saldo_awal = 0

if "sisa_saldo" not in st.session_state:
    st.session_state.sisa_saldo = 0

if "log_pengeluaran" not in st.session_state:
    st.session_state.log_pengeluaran = []

saldo_awal_input = st.number_input(
    "Masukkan saldo awal:",
    min_value=0,
    step=1000
)

if saldo_awal_input != st.session_state.saldo_awal:

    st.session_state.saldo_awal = saldo_awal_input
    st.session_state.sisa_saldo = saldo_awal_input
    st.session_state.log_pengeluaran = []

if st.session_state.saldo_awal > 0:

    st.subheader(
        f"Sisa Saldo: Rp {st.session_state.sisa_saldo:,}"
    )

    st.write("Daftar Pengeluaran")

    if len(st.session_state.log_pengeluaran) > 0:

        for i, item in enumerate(
            st.session_state.log_pengeluaran,
            start=1
        ):
            st.write(f"{i}. Rp {item:,}")

    else:
        st.write("Belum ada pengeluaran")

    if st.session_state.sisa_saldo > 0:

        pengeluaran = st.number_input(
            "Masukkan pengeluaran:",
            min_value=0,
            step=1000
        )

        if st.button("Tambah Pengeluaran"):

            if pengeluaran == 0:
                st.warning(
                    "Masukkan nominal pengeluaran"
                )

            elif pengeluaran < 2000:
                st.warning(
                    "Pengeluaran minimal Rp 2.000"
                )

            elif (
                pengeluaran >
                st.session_state.sisa_saldo
            ):
                st.error(
                    "Saldo tidak mencukupi"
                )

            else:

                st.session_state.sisa_saldo -= (
                    pengeluaran
                )

                st.session_state.log_pengeluaran.append(
                    pengeluaran
                )

                st.success(
                    "Pengeluaran berhasil ditambahkan"
                )

                if (
                    st.session_state.sisa_saldo == 0
                ):
                    st.error("Saldo habis")

    else:
        st.error("Saldo habis")

    st.write("---")

    total_pengeluaran = sum(
        st.session_state.log_pengeluaran
    )

    st.write(
        f"Total transaksi: "
        f"{len(st.session_state.log_pengeluaran)}"
    )

    st.write(
        f"Jumlah pengeluaran: "
        f"Rp {total_pengeluaran:,}"
    )

    st.write(
        f"Sisa saldo: "
        f"Rp {st.session_state.sisa_saldo:,}"
    )

else:
    st.info(
        "Masukkan saldo awal lebih dari 0"
    )
```
