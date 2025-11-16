# python-network-scanner
Simple muti-threaded network scanner with Python, to discover live hosts on a network and their MAC addresses on a network
---

## 🌟 Key Features

* **Multi-Threaded:** Uses the `kthread` library to ping all 254 possible IPs in a /24 subnet simultaneously, making it very fast.
* **Live Host Discovery:** Scans a given IP range and identifies all live hosts that respond to a ping.
* **MAC Address Resolution:** Uses `getmac` to find the hardware MAC address for each live host.
* **File Output:** Saves the list of live IPs and their corresponding MAC addresses to a `.txt` file for easy logging.

---

## 🚀 Usage

1.  Clone the repository:
    ```bash
    git clone https://github.com/MaroFarouk6/python-network-scanner.git
    cd python-network-scanner
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the script:
    * **Scan a specific subnet (e.g., 192.168.1.0/24):**
        ```bash
        python host_scanner.py 192.168.1.1
        ```
    * **Scan and save to a custom file:**
        ```bash
        python host_scanner.py 192.168.1.1 my_scan.txt
        ```

---

## ⚠️ Disclaimer

**This tool is for educational purposes and for use on authorized networks only.** I am not responsible for any misuse of this code.

---

## 📄 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.
