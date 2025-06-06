import streamlit as st
from scraper.extract import scrape_domains
import pandas as pd
import tempfile
import os
from deep_translator import GoogleTranslator 

st.set_page_config(page_title="B2B Scraper", layout="centered")

st.title("🔎 B2B Lead Generation Scraper")
st.write("Upload a list of domains to extract business contact data.")

uploaded_file = st.file_uploader("Upload .txt file with one domain per line", type=["txt"])


manual_input = st.text_area("Or paste domains (one per line)", "")

domains = []

if uploaded_file:
    domains = [line.strip() for line in uploaded_file.readlines() if line.strip()]
elif manual_input:
    domains = [line.strip() for line in manual_input.splitlines() if line.strip()]

if domains:
    st.success(f"{len(domains)} domains loaded.")

    if st.button("🚀 Start Scraping"):
        with st.spinner("Scraping in progress..."):
            data = scrape_domains(domains)
            df = pd.DataFrame(data)

          
            df['title_en'] = df['title'].apply(
                lambda x: GoogleTranslator(source='auto', target='en').translate(x) if pd.notnull(x) else ""
            )

            st.subheader("🔎 Preview of Results")
            st.dataframe(df[['domain', 'title', 'title_en', 'emails', 'phones', 'contact_links']])

  
            st.subheader("📊 Analytics Dashboard")

            total_domains = len(df)
            total_emails_found = df['emails'].apply(lambda x: len(x) if isinstance(x, list) else 0).sum()
            total_phones_found = df['phones'].apply(lambda x: len(x) if isinstance(x, list) else 0).sum()
            total_contact_pages = df['contact_links'].apply(lambda x: len(x) if isinstance(x, list) else 0).sum()

            col1, col2, col3, col4 = st.columns(4)
            col1.metric("🔢 Total Domains", total_domains)
            col2.metric("📧 Emails Found", total_emails_found)
            col3.metric("📞 Phones Found", total_phones_found)
            col4.metric("🔗 Contact Links", total_contact_pages)

            st.markdown("### 📌 Domain with Most Emails")
            df['email_count'] = df['emails'].apply(lambda x: len(x) if isinstance(x, list) else 0)
            top_email_domain = df.sort_values(by='email_count', ascending=False).head(1)
            st.dataframe(top_email_domain[['domain', 'emails']])

      
            tmp_download = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
            df.to_csv(tmp_download.name, index=False)
            tmp_download.close()

            with open(tmp_download.name, "rb") as f:
                csv_data = f.read()

            os.remove(tmp_download.name)

            st.download_button(
                "📥 Download CSV",
                data=csv_data,
                file_name="b2b_leads.csv",
                mime="text/csv"
            )
else:
    st.info("Please upload a file or enter domains manually.")
