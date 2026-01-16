def is_captcha_page(html: str) -> bool:
    captcha_keywords = [
        "captcha",
        "verify you are human",
        "unusual traffic",
        "robot check",
        "security check",
    ]

    html_lower = html.lower()
    return any(keyword in html_lower for keyword in captcha_keywords)
