# AI Webscraper

## Project Overview

AI Webscraper is a Python-based web scraping application with a **Streamlit-powered user interface** that enables users to scrape data from websites interactively. The project is designed with a modular backend architecture to handle real-world scraping challenges such as dynamic content, rate limiting, CAPTCHA detection, and fallback scraping strategies.

The application supports both static and JavaScript-rendered pages and is structured to be scalable and production-ready. Sensitive configuration files such as `config.py` are intentionally **excluded from the repository** to protect API keys and confidential credentials.

---

## Key Features

* Streamlit-based interactive UI for scraping operations
* Supports dynamic and static website scraping
* Bright Data / async request support for faster scraping
* CAPTCHA detection and handling logic
* Rate limiting to avoid blocking and throttling
* Intelligent scraping engine with fallback strategies
* Modular and extensible project structure
* Secure handling of API keys via local configuration

---

## Tech Stack

### Backend

* Python 3
* Async IO
* Selenium WebDriver
* Requests / HTTP Clients
* BeautifulSoup (for HTML parsing)

### Frontend

* Streamlit

### Tools & Utilities

* Chrome WebDriver
* Git & GitHub
* Virtual Environment (venv)

---

## Setup and Installation

### Prerequisites

* Python 3.9 or higher
* Google Chrome browser
* Chrome WebDriver (compatible version)
* Git

### Installation Steps

1. Clone the repository

```bash
git clone https://github.com/s-saqlain/AI-Webscraper.git
cd AI-Webscraper
```

2. Create and activate a virtual environment

```bash
python -m venv newenv
source newenv/bin/activate   # Linux / macOS
newenv\\Scripts\\activate      # Windows
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Configure API keys and secrets

* Create a `config.py` file locally
* Add required API keys and credentials
* Ensure `config.py` is listed in `.gitignore`

---

## Usage Instructions

1. Launch the Streamlit application

```bash
streamlit run app.py
```

2. Open the provided local URL in your browser

3. Enter the target website URL and scraping parameters

4. Trigger scraping and view results directly in the UI

---

## API Endpoints

Although the primary interface is Streamlit, the backend architecture supports API-style scraping logic internally.

### Example Internal Endpoint Logic

* Scrape Request

```json
{
  "url": "https://example.com",
  "method": "selenium | async | fallback"
}
```

* Scrape Response

```json
{
  "status": "success",
  "data": "extracted content"
}
```

---

## Frontend Overview

The Streamlit frontend provides:

* URL input fields
* Scraping mode selection
* Real-time scraping status
* Display of extracted content
* Error and warning notifications

The UI is designed for simplicity while supporting advanced scraping workflows.

---

## Backend Overview

The backend is organized into modular components:

* `engine.py` – Core scraping engine and workflow controller
* `async_brightdata.py` – Asynchronous scraping using proxy/API services
* `selenium_fallback.py` – Selenium-based scraping for JS-heavy sites
* `parser.py` – HTML parsing and data extraction logic
* `captcha_detector.py` – CAPTCHA detection mechanisms
* `rate_limiter.py` – Controls request frequency to prevent blocking
* `cache.py` – Caching layer for repeated requests

This architecture allows seamless fallback and performance optimization during scraping.

---

## Future Improvements

* Advanced CAPTCHA bypass integrations
* Proxy rotation and IP reputation management
* AI-powered data extraction and summarization
* Persistent storage using databases
* Export scraped data to CSV/JSON
* Enhanced Streamlit UI with dashboards and filters

---

## License

This project is licensed under the MIT License.

You are free to use, modify, and distribute this software with proper attribution.
