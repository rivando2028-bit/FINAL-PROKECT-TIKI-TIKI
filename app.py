import streamlit as st
from datetime import datetime

def rupiah(amount):
    return f"Rp {amount:,.0f}".replace(",", ".")


def reset_app():
    st.session_state.saldo_awal = 0
    st.session_state.sisa_saldo = 0
    st.session_state.transaksi = []
    st.session_state.mulai = False


st.set_page_config(
    page_title="Uang Saku Cerdas",
    layout="centered",
)

if "saldo_awal" not in st.session_state:
    reset_app()

if not st.session_state.mulai:
    st.title("Uang Saku Cerdas")
    st.caption("Bank Syariah Modern - Kelola uang sakumu dengan mudah")

    with st.container(border=True):
        st.header("Uang Saku Cerdas")
        st.write("Bank Syariah Modern - Kelola uang sakumu dengan mudah")

        saldo_awal = st.number_input(
            "Saldo Awal Bulan Ini",
            min_value=0,
            step=1000,
            placeholder="Contoh: 500000",
        )

        if st.button("Mulai Kelola Uang Saku", use_container_width=True):
            if saldo_awal <= 0:
                st.warning("Saldo awal harus lebih dari Rp 0")
            else:
                st.session_state.saldo_awal = saldo_awal
                st.session_state.sisa_saldo = saldo_awal
                st.session_state.transaksi = []
                st.session_state.mulai = True
                st.rerun()

else:
    saldo_awal = st.session_state.saldo_awal
    sisa_saldo = st.session_state.sisa_saldo
    transaksi = st.session_state.transaksi
    total_pengeluaran = sum(item["jumlah"] for item in transaksi)
    transaksi_utama = [item for item in transaksi if item["jumlah"] >= 2000]
    receh_diabaikan = [item for item in transaksi if item["jumlah"] < 2000]
    persen_sisa = 0 if saldo_awal == 0 else int((sisa_saldo / saldo_awal) * 100)

    st.title("Uang Saku Cerdas")
    st.caption("Bank Syariah Modern")

    with st.container(border=True):
        st.subheader("Sisa Saldo")
        st.header(rupiah(sisa_saldo))
        st.progress(max(0, min(persen_sisa, 100)) / 100)
        st.write(f"{persen_sisa}% dari {rupiah(saldo_awal)}")

    with st.container(border=True):
        st.subheader("Catat Pengeluaran")

        with st.form("form_pengeluaran", clear_on_submit=True):
            jumlah = st.number_input(
                "Jumlah (Rp)",
                min_value=0,
                step=1000,
                placeholder="Contoh: 15000",
            )
            keterangan = st.text_input(
                "Keterangan (Opsional)",
                placeholder="Contoh: Makan siang",
            )
            tambah = st.form_submit_button(
                "Tambah Pengeluaran",
                use_container_width=True,
            )

        if tambah:
            if jumlah <= 0:
                st.warning("Jumlah pengeluaran harus lebih dari Rp 0")
            elif jumlah > sisa_saldo:
                st.error("Saldo tidak cukup")
            else:
                st.session_state.sisa_saldo -= jumlah
                st.session_state.transaksi.append(
                    {
                        "jumlah": jumlah,
                        "keterangan": keterangan.strip() or "Tanpa keterangan",
                        "waktu": datetime.now().strftime("%d %B %Y, %H:%M"),
                    }
                )
                st.success("Pengeluaran berhasil ditambahkan")
                st.rerun()

    kolom_total, kolom_utama, kolom_receh = st.columns(3)

    with kolom_total:
        with st.container(border=True):
            st.write("Total Pengeluaran")
            st.subheader(rupiah(total_pengeluaran))

    with kolom_utama:
        with st.container(border=True):
            st.write("Transaksi Utama")
            st.subheader(rupiah(sum(item["jumlah"] for item in transaksi_utama)))
            st.caption(f"{len(transaksi_utama)} dari {len(transaksi)} transaksi")

    with kolom_receh:
        with st.container(border=True):
            st.write("Receh Diabaikan")
            st.subheader(rupiah(sum(item["jumlah"] for item in receh_diabaikan)))
            st.caption(f"{len(receh_diabaikan)} transaksi kecil")

    with st.container(border=True):
        st.subheader("Riwayat Pengeluaran")
        st.caption("Transaksi di bawah Rp 2.000 disembunyikan")

        if transaksi_utama:
            for item in reversed(transaksi_utama):
                kolom_info, kolom_nominal = st.columns([3, 1])
                with kolom_info:
                    st.write(item["keterangan"])
                    st.caption(item["waktu"])
                with kolom_nominal:
                    st.write(f"-{rupiah(item['jumlah'])}")
                st.divider()
        else:
            st.info("Belum ada transaksi utama")

    if sisa_saldo <= 0:
        st.error("Saldo habis")
    elif sisa_saldo <= 10000:
        st.warning("Saldo mulai menipis")

    if st.button("Reset Semua Data", use_container_width=True):
        reset_app()
        st.rerun()
