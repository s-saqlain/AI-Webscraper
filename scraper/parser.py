from bs4 import BeautifulSoup
import pandas as pd

def extract_text_and_tables(html: str):
    soup = BeautifulSoup(html, "html.parser")

    # Remove noisy tags
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    # Extract text
    text = soup.get_text(separator=" ", strip=True)

    # Extract tables
    tables = []
    for table in soup.find_all("table"):
        try:
            df = pd.read_html(str(table))[0]
            tables.append(df)
        except Exception:
            continue

    return text[:6000], tables
