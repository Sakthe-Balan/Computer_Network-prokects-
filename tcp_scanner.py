from tkinter import *
from scapy.all import *


def scan_ports():
    # Get the target IP address and port number from the entry widgets
    target_host = ip_entry.get()
    target_port = int(port_entry.get())

    # Use Scapy to send three SYN packets to the target host and port
    results = []
    for i in range(3):
        packet = IP(dst=target_host) / TCP(dport=target_port, flags="S")
        response = sr1(packet, timeout=2, verbose=0)
        if response and response.haslayer(TCP) and response[TCP].flags & 0x12 == 0x12:
            results.append("TCP Port is OPEN")
        else:
            packet = IP(dst=target_host) / UDP(dport=target_port)
            response = sr1(packet, timeout=2, verbose=0)
            if response and response.haslayer(UDP):
                results.append("UDP Port is OPEN")
            else:
                results.append("Port is CLOSED")

    # Determine the final port status based on the results
    if "OPEN" in results:
        result_listbox.insert(END, f"Port {target_port}: {results[0]}")
    else:
        result_listbox.insert(END, f"Port {target_port}: {results[0]}")

    
    



# Create the main window and set its title
root = Tk()
root.title("Port Scanner")

# Create a label and entry widget for the target IP address
ip_label = Label(root, text="Target IP address:")
ip_label.grid(row=0, column=0, padx=5, pady=5)
ip_entry = Entry(root)
ip_entry.grid(row=0, column=1, padx=5, pady=5)

# Create a label and entry widget for the target port number
port_label = Label(root, text="Target port number:")
port_label.grid(row=1, column=0, padx=5, pady=5)
port_entry = Entry(root)
port_entry.grid(row=1, column=1, padx=5, pady=5)

# Create a button to initiate the port scan
scan_button = Button(root, text="Scan", command=scan_ports)
scan_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Create a listbox to display the results of the port scan
result_listbox = Listbox(root, font=("Arial", 14))
result_listbox.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Run the main loop of the GUI
root.mainloop()
