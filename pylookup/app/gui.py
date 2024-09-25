import tkinter as tk
from tkinter import messagebox
from .core import WhoisLookup

class WhoisGUI:
    def __init__(self, master):
        self.master = master
        master.title("WHOIS Lookup Tool")

        self.label = tk.Label(master, text="Enter Domain:")
        self.label.pack()

        self.domain_entry = tk.Entry(master)
        self.domain_entry.pack()

        self.lookup_button = tk.Button(master, text="Lookup", command=self.lookup_domain)
        self.lookup_button.pack()

        self.results_text = tk.Text(master, height=15, width=50)
        self.results_text.pack()

    def lookup_domain(self):
        domain = self.domain_entry.get()
        if domain:
            lookup = WhoisLookup()
            try:
                result = lookup.lookup(domain, dns=False)
                self.display_results(result)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Input Error", "Please enter a domain.")

    def display_results(self, results):
        self.results_text.delete(1.0, tk.END)  # Clear previous results
        for key, value in results.items():
            self.results_text.insert(tk.END, f"{key.capitalize()}: {value if value else 'Not Available'}\n")

def main():
    root = tk.Tk()
    gui = WhoisGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
