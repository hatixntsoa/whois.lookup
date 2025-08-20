# Pylookup Tool

<p align="center">
 <img height="150" src="https://raw.githubusercontent.com/hatixntsoa/whois_lookup/master/imgs/pylookup.png"/>
</p>

<div align="center">

<p>

``pylookup-tool`` is a comprehensive Python-based WHOIS and DNS lookup utility that allows users to gather detailed information about domains, including WHOIS records and DNS details. It supports various TLDs, IDN domains, and provides batch processing capabilities. 

</p>

### Contents

[Features](#features) |
[Installation](#installation) |
[Install from PyPI](#option-1-install-from-pypi) |
[Build from Source](#option-2-build-from-source) |
[Usage](#usage) |
[Example Usage](#example-usage) |
[GUI Usage](#gui-usage) |
[Usage as a Package](#usage-as-a-package) |
[Development](#development)

</div>

## Features

- **Command-Line Interface (CLI)**: Perform WHOIS and DNS lookups directly from the terminal with simple command-line arguments.
- **WHOIS Lookup**: Retrieve WHOIS information for any given domain, including registrant details, registration dates, and more.
- **DNS Record Lookup**: Fetch DNS records (A, MX, NS, TXT) for any domain.
- **Batch Queries**: Perform WHOIS lookups for a list of domains from a file, making it easy to process multiple domains at once.
- **IDN Support**: Seamlessly handle Internationalized Domain Names (IDNs) using Punycode conversion.
- **Caching and Rate Limiting**: Utilize in-memory caching and rate limiting to optimize queries and prevent server overload.
- **Email Alerts**: Set up email notifications for specific WHOIS changes (requires additional configuration).
- **Extendable Functionality**: Add custom features like reverse WHOIS lookup and WHOIS data comparison.
- **Graphical User Interface (GUI)**: A user-friendly GUI to perform WHOIS lookups without using the command line.

## Installation

### Option 1: Install from PyPI

To install `pylookup-tool` directly from PyPI:

```bash
pip install pylookup-tool
```

### Option 2: Build from Source

For those who prefer to build it themselves:

1. Clone the repository and navigate to the project directory:

   ```bash
   git clone https://github.com/hatixntsoa/whois_lookup.git
   cd whois_lookup
   ```

2. Build the package:

   ```bash
   python setup.py sdist bdist_wheel
   ```

3. Install the package:

   ```bash
   pip install dist/*.whl
   ```

## Usage

Once the package is installed, you can use the `pylookup` command from the terminal. The script accepts the following command-line arguments:

- **Domain Lookup**:
  - `domain`: Specify the domain to perform a WHOIS lookup (e.g., `example.com`).

- **Batch Processing**:
  - `-b` or `--batch`: Specify a file containing a list of domains for batch processing.

- **DNS Records**:
  - `--dns`: Include this option to perform a DNS record lookup in addition to the WHOIS lookup.

- **Help Option**:
  - `-h` or `--help`: Display the help message with all available options.

### Example Usage

1. **Single Domain WHOIS Lookup**:
   ```bash
   pylookup example.com
   ```

2. **WHOIS Lookup with DNS Records**:
   ```bash
   pylookup example.com --dns
   ```

3. **Batch WHOIS Lookup**:
   ```bash
   pylookup -b domains.txt
   ```

4. **Help Option**:
   For help with command-line options, use:
   ```bash
   pylookup -h
   ```

### GUI Usage

You can also use the `pylookup-tool` with a graphical user interface (GUI). Here's how to launch the GUI and perform lookups:

1. **Launching the GUI**:
   To open the GUI, run the following command:
   ```bash
   pylookup --gui
   ```

2. **Using the GUI**:
   - Enter the domain you want to look up in the text field.
   - Click the "Lookup" button to perform the WHOIS lookup.
   - The results will be displayed in the text area below.

### Usage as a Package

You can also import `pylookup-tool` as a package in your own Python projects. Here's how to use it programmatically:

```python
# Import the WhoisLookup class from the pylookup package
from pylookup.app.core import WhoisLookup

# Create an instance of the WhoisLookup class
lookup = WhoisLookup()

# Perform a WHOIS lookup for a domain
response = lookup.lookup('example.com')
print(response)

# Perform a WHOIS lookup for a domain with DNS records
dns_response = lookup.lookup('example.com', dns=True)
print(dns_response)

# Batch lookup from a file
lookup.batch_lookup('domains.txt')
```

## Development

To modify or extend the functionality, ensure you have the required dependencies installed. You can add new features to the CLI or modify existing functionality as needed.

### Adding New Features

- **Support for More TLDs**: Add new WHOIS servers for additional TLDs in `pylookup/app/servers.py`.
- **Custom Parsing Logic**: Modify `pylookup/app/parser.py` to handle more complex or custom WHOIS data formats.
- **Integrate Third-Party APIs**: For features like reverse WHOIS, integrate with third-party APIs (e.g., WhoisXML API) in `pylookup/app/core.py`.

## Contributing

Feel free to fork this repository, open issues, or submit pull requests with improvements or bug fixes. Your contributions help make the `pylookup-tool` better!