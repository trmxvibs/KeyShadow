# 🎩 KeyShadow

> **An Educational, Open-Source, Cross-Platform Keylogger**  

```
 _  __           _____ _           _               
| |/ /___ _   _ /  ___| |__   __ _| |_ ___  _ __   
| ' // _ \ | | |\___ \| '_ \ / _` | __/ _ \| '__|  
| . \  __/ |_| | ___) | | | | (_| | || (_) | |     
|_|\_\___|\__, | |____/|_| |_|\__,_|\__\___/|_|     
         |___/                                  
```

---

##  ![Warning](https://img.icons8.com/color/48/000000/error--v1.png) **IMPORTANT ETHICAL NOTICE**

> **KeyShadow is for EDUCATIONAL and ETHICAL use only.**
>
> - 🚫 **Never use on devices you don't own or without clear, written permission!**
> - 🛑 **Unauthorized use is illegal and unethical.**
> - 👨‍💻 Authors and contributors assume NO responsibility for misuse.

---

## 🌈 Features

- 📝 **Local logging** to file (`local` mode)
- 🔗 **Network sending** to another device (`send` mode)
- 📥 **Network receiving** logs (`receive` mode)
- ⚙️ **Customizable:** IPs, ports, log file path via CLI
- 💻 **Works on:**  
  - **Kali Linux, Ubuntu, Other Linux**  
  - **Windows 10/11**  
  - **macOS**  
  - **Termux (limited)**
- 🐍 **Python 3.7+ required**
- 🔓 **No API keys or cloud dependencies**
- 📄 **Simple, plain-text log files**

---

## 🚀 Installation

### 1. Install Python 3.7+  
- [Download Python for Windows](https://www.python.org/downloads/windows/)  
- [Download Python for macOS](https://www.python.org/downloads/macos/)
- On Linux:  
  ```bash
  sudo apt update && sudo apt install python3 python3-pip
  ```

### 2. Install dependencies:
```bash
pip install pynput
```

### 3. Download `keyshadow.py` to your system.

---

## 🖥️ Supported Platforms

| Platform         | Supported? | Notes                                              |
|------------------|------------|----------------------------------------------------|
| 🐧 Kali Linux    | ✅         | Full support                                       |
| 🐧 Ubuntu        | ✅         | Full support                                       |
| 🐧 Other Linux   | ✅         | Full support                                       |
| 🪟 Windows 10/11 | ✅         | Full support (run in CMD or PowerShell)            |
| 🍏 macOS         | ✅         | Full support (Terminal; may need permissions)      |
| 📱 Termux        | ⚠️        | Only within Termux shell (no global key capture)   |

> **Tip:** On Windows/macOS, you may need to grant accessibility/input monitoring permissions for full keylogging.

---

## 🆘 Help Menu

```bash
python3 keyshadow.py --help
```

---

## 👾 Usage: Modes & Examples

### 1️⃣ Local Logging (Log to File)
```bash
python3 keyshadow.py --mode local --logfile mylogs.txt
```
Logs all keypresses to `mylogs.txt`.  
Press `ESC` to stop logging.

---

### 2️⃣ Send Mode (Send Logs to Remote Device)
```bash
python3 keyshadow.py --mode send --remote-ip <RECEIVER_IP> --remote-port 8080
```
Sends every keystroke to a receiver at `<RECEIVER_IP>:8080` **AND** saves locally.

---

### 3️⃣ Receive Mode (Listen for Logs)
```bash
python3 keyshadow.py --mode receive --listen-port 8080 --logfile received.txt
```
Listens for logs on port 8080 and writes them to `received.txt`.

---

## 🌐 Example: Logging Across the Network

**PC 1 (Receiver):**
```bash
python3 keyshadow.py --mode receive --listen-port 8080 --logfile logs_from_laptop.txt
```

**PC 2 (Sender):**
```bash
python3 keyshadow.py --mode send --remote-ip <PC1_IP> --remote-port 8080
```

- Both devices must be on the same local network.
- Use your PC's local IP (e.g., `192.168.1.5`) for `<PC1_IP>`.

---

## 🌍 Remote Logging (Outside Local Network)

- **Port Forwarding:**  
  - Forward port 8080 on your router to the receiver's local IP.
- **Firewall:**  
  - Allow inbound connections on port 8080.
- **Security:**  
  - Exposes your device to the internet—**use with extreme caution** and only for testing.
- **Never** use on devices/networks without explicit, legal permission.

---

## 💡 How It Works

- **local**: Records every keypress to a local file.
- **send**: Sends each keypress to a given IP:port, as well as logging locally.
- **receive**: Starts a simple TCP server to receive log entries and write them to a file.

---

## ⚠️ Limitations

- **No encryption** of logs or network data (for educational simplicity)
- **No cloud or email integration**
- **Key capture limited by OS permissions**
- **Not intended for stealth or malicious use**
- **On Windows/macOS:** May require running as Administrator or giving input monitoring permissions.

---

## 👨‍💻 Authors

- **Lokesh Kumar**
- ## **[Youtube](https://www.youtube.com/@termux2)**



---

## 📝 License

[MIT License](LICENSE)

---

## 🤝 Contributing

PRs and suggestions welcome for further educational features.

---

## ❗ Disclaimer

This software is provided “as is” for ethical and educational use.  
**You are responsible for your actions.**
