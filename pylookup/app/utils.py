import time
import dns.resolver
from functools import wraps
import smtplib
from email.mime.text import MIMEText

_cache = {}

def cache(func):
    """Simple in-memory cache decorator."""
    @wraps(func)
    def wrapper(domain, *args, **kwargs):
        if domain in _cache:
            print(f"Fetching {domain} from cache.")
            return _cache[domain]
        result = func(domain, *args, **kwargs)
        _cache[domain] = result
        return result
    return wrapper

def rate_limit(interval):
    """Decorator to limit the rate of function calls."""
    def decorator(func):
        last_called = [0]
        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            wait = max(0, interval - elapsed)
            if wait > 0:
                time.sleep(wait)
            result = func(*args, **kwargs)
            last_called[0] = time.time()
            return result
        return wrapper
    return decorator

def get_dns_records(domain):
    """Get DNS records for a domain."""
    records = {}
    for record_type in ['A', 'MX', 'NS', 'TXT']:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            records[record_type] = [rdata.to_text() for rdata in answers]
        except dns.resolver.NoAnswer:
            records[record_type] = []
    return records

def send_email_alert(subject, message, to_email):
    """Send an email alert with the given subject and message."""
    from_email = "your.email@example.com"  # Replace with your email
    password = "yourpassword"  # Replace with your email password
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())