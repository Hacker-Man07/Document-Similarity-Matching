import re
from typing import Dict

def extract_features(text: str) -> Dict[str, str]:

    features = {
        "invoice_number": extract_invoice_number(text),
        "date": extract_date(text),
        "amount": extract_amount(text),
        "items": extract_items(text),
        "addresses": extract_addresses(text),
        "phone_numbers": extract_phone_numbers(text),
        "email_addresses": extract_email_addresses(text)
    }
    return features

def extract_invoice_number(text: str) -> str:
    match = re.search(r'(Rechnung\s*Nr\.|Rechnungsnummer|invoice\s*number)\s*[:\-]?\s*(\d+)', text, re.IGNORECASE)
    return match.group(2) if match else ""

def extract_date(text: str) -> str:
    match = re.search(r'\d{2}/\d{2}/\d{4}', text) or re.search(r'\d{2}\.\d{2}\.\d{4}', text)
    return match.group(0) if match else ""

def extract_amount(text: str) -> str:
    match = re.search(r'(\d{1,3}(?:\.\d{3})*,\d{2}\s*EUR)', text) or re.search(r'(\d{1,3}(?:,\d{3})*\.\d{2}\s*EUR)', text)
    return match.group(0) if match else ""

def extract_items(text: str) -> str:
    items = re.findall(r'\d+\s+\w+(?:\s+\w+)*\s+\d+,\d+\s*EUR', text)
    return "\n".join(items) if items else ""

def extract_addresses(text: str) -> str:
    addresses = re.findall(r'\d{5}\s+\w+(?:\s+\w+)*\s+\w+(?:\s+\w+)*', text)
    return "\n".join(addresses) if addresses else ""

def extract_phone_numbers(text: str) -> str:
    phone_numbers = re.findall(r'\+?\d{1,3}?\s?-?\(?\d{1,4}?\)?\s?-?\d{1,4}\s?-?\d{1,4}\s?-?\d{1,9}', text)
    return "\n".join(phone_numbers) if phone_numbers else ""

def extract_email_addresses(text: str) -> str:
    email_addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    return "\n".join(email_addresses) if email_addresses else ""
