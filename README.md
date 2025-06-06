# 🛠️ B2B Contact Scraper Project

## 📌 Project Overview

This project aims to automate the extraction of B2B contact information such as emails, phone numbers, and contact links from a list of domains. It is designed to save time and improve efficiency when gathering contact data from multiple websites.

---

## 🎯 Objective

- Automatically extract:
  - ✉️ Email addresses
  - ☎️ Phone numbers
  - 🔗 Contact page links
- Provide analytics and export results to CSV

---

## 🧠 Methodology

- **Input:** A CSV file containing domain names
- **Process:**
  1. Load each domain’s homepage
  2. Parse HTML with BeautifulSoup
  3. Use regex to extract contact data
- **Output:** Analytics preview and downloadable CSV

---

## 📊 Results

| Metric            | Count   |
|-------------------|---------|
| Domains processed | 7       |
| Emails found      | 380     |
| Phone numbers     | 1,349   |
| Contact links     | 8       |

**Example:**  
`https://qiscus.com` → 4 emails found

---

## ✅ Key Features

- Modular and scalable codebase
- Easily extendable to a full web app
- CLI interface with potential for UI integration
- Clean and structured CSV output

---

## 🚀 Future Improvements

- Build UI using **Streamlit**
- Add visual insights (charts, counts)
- Validate emails and phone number formats
- Handle blocked requests using proxies or retries

---

## 📁 Project Structure
b2b_scraper_project/
├── scraper/

│ ├── init.py

│ ├── extract.py # Core scraping logic

│ ├── utils.py # Helper functions (regex, etc.)

├── main.py # Entry point to run the scraper

├── requirements.txt # All required Python packages

├── README.md # Project documentation

├── example_output.csv # Sample output

└── report.pdf # Final report (optional)
