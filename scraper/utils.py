# scraper/utils.py

import re
from bs4 import BeautifulSoup


def find_emails(html):
    raw_emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", html)
    valid_emails = [email for email in raw_emails if validate_email_format(email)]
    return valid_emails

def validate_email_format(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None


def find_contact_links(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    contact_links = []
    for a_tag in soup.find_all("a", href=True):
        href = a_tag['href'].lower()
        if "contact" in href or "hubungi" in href:
            if href.startswith("http"):
                contact_links.append(href)
            else:
                contact_links.append(base_url.rstrip("/") + "/" + href.lstrip("/"))
    return contact_links

def find_title(html):
    match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else ""



def find_phones(html):
    phone_pattern = re.compile(r"\+?\d[\d\-\.\s()]{7,}\d")
    phones = phone_pattern.findall(html)
    return [phone.strip() for phone in phones]


def find_names(html):
    soup = BeautifulSoup(html, "html.parser")
    candidates = []

    for tag in ['h1', 'h2', 'title']:
        elements = soup.find_all(tag)
        for el in elements:
            text = el.get_text(strip=True)
            if text and len(text.split()) <= 3:  
                candidates.append(text)

    return list(set(candidates))

