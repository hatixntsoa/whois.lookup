import re

def parse_whois(response):
    """Parse WHOIS response and extract key information."""
    whois_data = {}
    patterns = {
        "domain_name": r"Domain Name:\s*(.+)",
        "registrar": r"Registrar:\s*(.+)",
        "creation_date": r"Creation Date:\s*(.+)",
        "expiration_date": r"Registry Expiry Date:\s*(.+)",
        "name_servers": r"Name Server:\s*(.+)"
    }
    for key, pattern in patterns.items():
        match = re.search(pattern, response, re.IGNORECASE)
        whois_data[key] = match.group(1).strip() if match else "Not Available"
    return whois_data

def compare_whois_data(old_data, new_data):
    """Compare two sets of WHOIS data and return differences."""
    differences = {}
    for key in old_data:
        if old_data[key] != new_data.get(key, None):
            differences[key] = {"old": old_data[key], "new": new_data.get(key, "Not Available")}
    return differences