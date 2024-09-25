import socket
import idna
from .parser import parse_whois
from .utils import cache, rate_limit, get_dns_records

class WhoisLookup:
    def __init__(self):
        self.default_server = "whois.verisign-grs.com"
        self.default_port = 43

    @rate_limit(1)  # Enforce a 1-second delay between calls
    @cache  # Cache the results
    def lookup(self, domain, server=None, port=None, dns=False):
        """Perform a WHOIS query for a given domain and return the response."""
        server = server or self.default_server
        port = port or self.default_port
        
        # Convert the domain to Punycode if necessary
        try:
            domain = idna.encode(domain).decode('utf-8')
        except idna.IDNAError:
            raise ValueError(f"Invalid domain name: {domain}")
        
        # Perform WHOIS lookup
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server, port))
            query = f"{domain}\r\n"
            s.sendall(query.encode("utf-8"))
            response = b""
            while True:
                data = s.recv(4096)
                if not data:
                    break
                response += data
        
        # Parse WHOIS response
        parsed_data = parse_whois(response.decode("utf-8"))

        # If dns is True, fetch and append DNS records
        if dns:
            dns_records = get_dns_records(domain)
            parsed_data['dns_records'] = dns_records  # Add DNS records to parsed data

        return parsed_data  # Return parsed data with or without DNS records

    def batch_lookup(self, file_path):
        """Perform WHOIS lookups for a batch of domains from a file."""
        with open(file_path) as file:
            domains = file.read().splitlines()

        for domain in domains:
            response = self.lookup(domain, dns=True)  # Optionally fetch DNS records
            print(f"\nWHOIS data for {domain}:")
            for key, value in response.items():
                print(f"{key.capitalize()}: {value if value else 'Not Available'}")
