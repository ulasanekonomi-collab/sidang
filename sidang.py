import streamlit as st
import pandas as pd
from datetime import date

# Konfigurasi Halaman Streamlit
st.set_page_config(
    page_title="Input Nilai Sidang Skripsi - UNISBA",
    page_icon="🎓",
    layout="centered"
)

# Header Instansi
st.markdown("""
<div style="text-align: center;">
    <h3>PROGRAM STUDI EKONOMI PEMBANGUNAN</h3>
    <h4>FAKULTAS EKONOMI DAN BISNIS UNISBA</h4>
    <hr style="border: 1px solid #1E3A8A; margin-bottom: 20px;">
    <h3 style="color: #1E3A8A;">NILAI UJIAN SKRIPSI KOMPREHENSIF</h3>
</div>
""", unsafe_allow_html=True)

# --- FORM IDENTITAS ---
st.subheader("📋 Identitas Ujian")
col1, col2 = st.columns(2)

with col1:
    nama = st.text_input("Nama Mahasiswa", value="Alinda Mutiara Salwa")
    npm = st.text_input("NPM / NIRM", value="10090222040")

with col2:
    nama_penguji = st.text_input("Nama Penguji", value="Yuhka Sundaya, SE., M.Si.")
    tgl_sidang = st.date_input("Tanggal Ujian", value=date.today())

judul_skripsi = st.text_area(
    "Judul Skripsi", 
    value="ANALISIS FAKTOR-FAKTOR EKONOMI PERILAKU YANG MEMPENGARUHI KETERLIBATAN SHARING KONTEN PRODUK DI TIKTOK",
    height=80
)

st.divider()

# --- PENILAIAN ---
st.subheader("📊 Kriteria Penilaian")

col_nilai1, col_nilai2, col_nilai3 = st.columns([3, 2, 2])

with col_nilai1:
    st.write("**Kriteria**")
    st.write("1. Penyajian (Presentasi)")
    st.write("2. Metodologi")
    st.write("3. Materi")

with col_nilai2:
    st.write("**Bobot**")
    st.write("20%")
    st.write("30%")
    st.write("50%")

with col_nilai3:
    st.write("**Nilai Angka (0-100)**")
    val_penyajian = st.number_input("Penyajian", min_value=0.0, max_value=100.0, value=80.0, step=1.0, label_visibility="collapsed")
    val_metodologi = st.number_input("Metodologi", min_value=0.0, max_value=100.0, value=82.0, step=1.0, label_visibility="collapsed")
    val_materi = st.number_input("Materi", min_value=0.0, max_value=100.0, value=85.0, step=1.0, label_visibility="collapsed")

# Kalkulasi Nilai Dibobot
bobot_penyajian = val_penyajian * 0.20
bobot_metodologi = val_metodologi * 0.30
bobot_materi = val_materi * 0.50

total_nilai = bobot_penyajian + bobot_metodologi + bobot_materi
status_lulus = "LULUS" if total_nilai >= 60 else "TIDAK LULUS"

# Tabel Ringkasan Penilaian
df_nilai = pd.DataFrame({
    "No": [1, 2, 3],
    "Kriteria Penilaian": ["Penyajian (Presentasi)", "Metodologi", "Materi"],
    "Nilai Angka": [val_penyajian, val_metodologi, val_materi],
    "Bobot": ["20%", "30%", "50%"],
    "Nilai Dibobot": [f"{bobot_penyajian:.2f}", f"{bobot_metodologi:.2f}", f"{bobot_materi:.2f}"]
})

st.table(df_nilai)

# Display Hasil Akhir
col_hasil1, col_hasil2 = st.columns(2)
with col_hasil1:
    st.metric(label="JUMLAH NILAI (RATA-RATA DIBOBOT)", value=f"{total_nilai:.2f}")
with col_hasil2:
    if status_lulus == "LULUS":
        st.success(f"STATUS: **{status_lulus}** (Minimal 60)")
    else:
        st.error(f"STATUS: **{status_lulus}** (Minimal 60)")

st.divider()

# --- LEMBARAN REVISI DAN PERBAIKAN ---
st.subheader("📝 Lembaran Revisi dan Perbaikan")

catatan_revisi = st.text_area(
    "Revisi, Perbaikan, dan Catatan Skripsi", 
    placeholder="Tuliskan poin-poin revisi/catatan penguji di sini...",
    height=120
)

tgl_revisi = st.text_input("Tanggal Selesai Revisi (Opsional)", value=".......................2026")

# --- TOMBOL SIMPAN / EXPORT ---
st.divider()
if st.button("💾 Simpan Ringkasan Evaluasi", type="primary"):
    st.balloons()
    st.success("Data berhasil diolah dan siap diproses!")
    
    # Pratinjau Output Teks Formulir
    st.markdown("### Ringkasan Berita Acara")
    st.code(f"""
===================================================================
PROGRAM STUDI EKONOMI PEMBANGUNAN - FAKULTAS EKONOMI DAN BISNIS UNISBA
===================================================================
NAMA           : {nama}
NPM/NIRM       : {npm}
JUDUL SKRIPSI  : {judul_skripsi}
PENGUJI        : {nama_penguji}
TANGGAL        : {tgl_sidang.strftime('%d %B %Y')}

[PENILAIAN UJIAN SKRIPSI]
1. Penyajian (20%) : {val_penyajian} -> Dibobot: {bobot_penyajian:.2f}
2. Metodologi (30%): {val_metodologi} -> Dibobot: {bobot_metodologi:.2f}
3. Materi (50%)    : {val_materi} -> Dibobot: {bobot_materi:.2f}-------------------------------------------------------------------
JUMLAH NILAI TOTAL : {total_nilai:.2f}
STATUS KELULUSAN   : {status_lulus}

[CATATAN REVISI & PERBAIKAN]
{catatan_revisi if catatan_revisi else '- Tidak ada catatan khusus -'}
Tanggal Selesai Revisi: {tgl_revisi}
===================================================================
    """)
