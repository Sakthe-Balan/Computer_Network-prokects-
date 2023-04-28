from tkinter import *
from scapy.all import *


def scan_ports():
    # Get the target IP address and port number from the entry widgets
    target_host = ip_entry.get()
    target_port = int(port_entry.get())

    # Use Scapy to send a SYN packet to the target host and port
    packet = IP(dst=target_host) / TCP(dport=target_port, flags="S")
    response = sr1(packet, timeout=2, verbose=0)

    # Clear previous results from the listbox
    result_listbox.delete(0, END)

    # Check if the response has a TCP layer and the SYN-ACK flag is set,
    # indicating that the port is open
    if response and response.haslayer(TCP) and response[TCP].flags & 0x12 == 0x12:
        result_listbox.insert(END, f"Port {target_port}: TCP Port OPEN")
    else:
        # If the TCP port is closed, send a UDP packet to the same port
        packet = IP(dst=target_host) / UDP(dport=target_port)
        response = sr1(packet, timeout=2, verbose=0)
        
        # Check if an ICMP message was received indicating that the UDP port is closed
        if response and response.haslayer(ICMP) and response[ICMP].type == 3 and response[ICMP].code in [1, 2, 3, 9, 10, 13]:
            result_listbox.insert(END, f"Port {target_port}: UDP Port CLOSED")
        else:
            result_listbox.insert(END, f"Port {target_port}: UDP Port OPEN")


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
result_listbox = Listbox(root, width=50, height=5)
result_listbox.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Run the main loop of the GUI
root.mainloop()
