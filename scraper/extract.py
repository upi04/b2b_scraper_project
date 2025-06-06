import requests
from .utils import (
    find_emails,
    find_names,
    find_phones,
    find_contact_links,
    find_title
)

def extract_from_domain(domain):
    try:
        if isinstance(domain, bytes):
            domain = domain.decode("utf-8")

        if not domain.startswith("http"):
            domain = "https://" + domain

        urls_to_try = [domain, domain.rstrip("/") + "/contact"]

        html = ""
        for url in urls_to_try:
            try:
                response = requests.get(url, timeout=5)
                response.raise_for_status()
                html = response.text
                break  
            except Exception:
                continue  

        if not html:
            raise Exception("No valid page found.")

        return {
            "domain": domain,
            "title": find_title(html),
            "emails": find_emails(html),
            "phones": find_phones(html),
            "contact_links": find_contact_links(html, domain),
            "names": find_names(html),
        }

    except Exception as e:
        print(f"❌ Error processing {domain!r}: {e}")
        return {
            "domain": domain,
            "title": "",
            "emails": [],
            "phones": [],
            "contact_links": [],
            "names": []
        }


def scrape_domains(domains):
    results = []
    for domain in domains:
        result = extract_from_domain(domain)
        results.append(result)
    return results
