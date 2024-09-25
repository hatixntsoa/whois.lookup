import argparse
import tkinter as tk

# Determine if the script is being run as standalone or as a package
is_standalone = __name__ == "__main__"

# Import based on execution context
if is_standalone:
  from app.core import WhoisLookup
  from app.gui import WhoisGUI
else:
  from pylookup.app.core import WhoisLookup
  from pylookup.app.gui import WhoisGUI

def main():
    parser = argparse.ArgumentParser(description="WHOIS Lookup Tool made by h471x.")
    parser.add_argument("domain", nargs="?", help="Domain to lookup (e.g., example.com)")
    parser.add_argument("-b", "--batch", help="File containing a list of domains to lookup")
    parser.add_argument("--dns", action="store_true", help="Perform DNS record lookup")
    parser.add_argument("--gui", action="store_true", help="Launch the GUI version of the tool")
    args = parser.parse_args()
    
    lookup = WhoisLookup()

    if args.batch:
        lookup.batch_lookup(args.batch)
    elif args.gui:
        root = tk.Tk()
        gui = WhoisGUI(root)
        root.mainloop()
    elif args.domain:
        result = lookup.lookup(args.domain, dns=args.dns)  # Get the result of the lookup
        for key, value in result.items():  # Iterate through the result dictionary
            print(f"{key.capitalize()}: {value if value else 'Not Available'}")  # Print each key-value pair
    else:
        print("Please provide a domain or use the --batch option with a file.")

if __name__ == "__main__":
    main()
