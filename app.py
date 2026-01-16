import streamlit as st
import asyncio
import pandas as pd

from scraper.engine import scrape

# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="Web Scraper",
    page_icon="🕷️",
    layout="wide"
)

# -------------------------
# Custom CSS
# -------------------------
st.markdown("""
<style>
.main-title {
    font-size: 2.4rem;
    font-weight: 700;
    color: #4F46E5;
}
.subtitle {
    color: #6B7280;
    margin-bottom: 1rem;
}

.badge {
    display: inline-block;
    background-color: #E0E7FF;
    color: #3730A3;
    padding: 0.2rem 0.6rem;
    border-radius: 8px;
    font-size: 0.8rem;
    margin-bottom: 0.4rem;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# Header
# -------------------------
st.markdown('<div class="main-title">🕷️ Web Scraper</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Scrape webpages, extract text & tables — fast and clean</div>',
    unsafe_allow_html=True
)

# -------------------------
# Input Section
# -------------------------
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    urls_input = st.text_area(
        "🌐 Enter URLs (one per line)",
        height=150,
        placeholder="https://example.com\nhttps://another-site.com"
    )

    scrape_btn = st.button("🚀 Start Scraping")

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# Async Wrapper
# -------------------------
async def scrape_all(urls):
    return await asyncio.gather(*(scrape(url) for url in urls))

# -------------------------
# Scraping Logic
# -------------------------
if scrape_btn:
    urls = [u.strip() for u in urls_input.splitlines() if u.strip()]

    if not urls:
        st.warning("⚠️ Please enter at least one URL.")
    else:
        progress = st.progress(0)
        status = st.empty()

        with st.spinner("Scraping websites..."):
            results = asyncio.run(scrape_all(urls))

        progress.progress(100)
        status.success("Scraping completed!")

        # -------------------------
        # Results
        # -------------------------
        for idx, result in enumerate(results, start=1):
            st.markdown("---")

            col1, col2 = st.columns([4, 1])

            with col1:
                st.subheader(f"🔗 {result['url']}")

            with col2:
                st.markdown('<span class="badge">Scraped</span>', unsafe_allow_html=True)

            text = result["text"]
            tables = result["tables"]

            # -------------------------
            # Text Section
            # -------------------------
            with st.expander("📄 Extracted Text"):
                st.write(text)

            # -------------------------
            # Tables Section
            # -------------------------
            if tables:
                st.markdown("### 📊 Extracted Tables")

                for i, table in enumerate(tables):
                    st.markdown(f"**Table {i+1}**")
                    st.dataframe(table, use_container_width=True)

                    csv = table.to_csv(index=False).encode("utf-8")
                    st.download_button(
                        label="⬇️ Download CSV",
                        data=csv,
                        file_name=f"table_{idx}_{i+1}.csv",
                        mime="text/csv"
                    )
            else:
                st.info("ℹ️ No tables found on this page.")
