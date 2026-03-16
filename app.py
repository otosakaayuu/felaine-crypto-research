import streamlit as st
import os
from pathlib import Path

st.set_page_config(page_title="Felaine | 24/7 Crypto Research", page_icon="📈", layout="wide")

# ================== SIDEBAR ==================
st.sidebar.image("https://via.placeholder.com/150x150/000000/F0B90B?text=Felaine", width=150)
st.sidebar.title("FelaineXZX7")
st.sidebar.markdown("**24/7 Crypto Research Analyst**")
st.sidebar.markdown("---")

page = st.sidebar.selectbox("Pilih Halaman", [
    "🏠 Home", 
    "📰 24H News Engine", 
    "🔧 Pro Tools Dashboard", 
    "💰 Institutional Sum Chart", 
    "📥 Download Reports", 
    "👤 About Me"
])

# ================== DOWNLOAD REPORTS PAGE ==================
if page == "📥 Download Reports":
    st.title("📥 Download All My Research Reports")
    st.markdown("**Transparan 100%.** Lihat sendiri hasil kerja saya (Project Listing, Monthly, Quarterly, Yearly, dll).")

    col1, col2 = st.columns(2)

    reports = {
        "Project Listing Report": "project-listing.pdf",
        "Project Performance Report": "project-performance.pdf",
        "Weekly Macro Report": "weekly-macro.pdf",
        "Monthly Market Report": "monthly-report.pdf",
        "Quarterly Crypto Macro Report": "quarterly-report.pdf",
        "Yearly Full Review & Themes": "yearly-report.pdf"
    }

    for i, (name, filename) in enumerate(reports.items()):
        pdf_path = Path("pdfs") / filename
        if pdf_path.exists():
            with open(pdf_path, "rb") as f:
                bytes_data = f.read()
            
            col = col1 if i % 2 == 0 else col2
            with col:
                st.subheader(name)
                st.caption(f"{filename} • {len(bytes_data)/1024:.1f} KB")
                st.download_button(
                    label="⬇️ Download PDF",
                    data=bytes_data,
                    file_name=filename,
                    mime="application/pdf",
                    use_container_width=True
                )
        else:
            st.warning(f"{filename} belum di-upload")

    # Bonus: Download semua sekaligus (ZIP)
    st.markdown("---")
    st.subheader("📦 Download Semua Report Sekaligus")
    if st.button("Generate ZIP All Reports"):
        import zipfile
        import io
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w") as zip_file:
            for filename in reports.values():
                path = Path("pdfs") / filename
                if path.exists():
                    zip_file.write(path, filename)
        zip_buffer.seek(0)
        st.download_button(
            label="⬇️ Download ZIP (All Reports)",
            data=zip_buffer,
            file_name="Felaine-All-Research-Reports.zip",
            mime="application/zip"
        )

# ================== HALAMAN LAIN (contoh sederhana) ==================
elif page == "🏠 Home":
    st.title("FelaineXZX7 — Crypto Never Sleeps. Neither Do I.")
    st.markdown("**24/7 Research Analyst** untuk Exchange, VC, dan Fund")
    st.image("https://via.placeholder.com/1200x400/000000/F0B90B?text=24H+CRYPTO+RESEARCH", use_column_width=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Reports Created", "150+")
    with col2:
        st.metric("Tools Aggregated", "Messari + Kaiko + Glassnode + Delphi")
    with col3:
        st.metric("Response Time", "< 15 menit")

elif page == "📰 24H News Engine":
    st.title("📰 24H News & Sentiment Engine")
    st.info("Nanti di sini live feed dari X + CryptoPanic + custom scraper")

# Sisanya bisa kamu tambah sendiri (Institutional Sum Chart pakai Plotly, dll)

else:
    st.title(page)
    st.info("Halaman ini sedang dibangun — kamu tinggal tambah code Plotly kamu di sini.")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by FelaineXZX7 • [X @felaineXZX7](https://x.com/felaineXZX7) • Not financial advice")
